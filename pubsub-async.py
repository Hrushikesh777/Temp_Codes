import json
from google.api_core import retry
from google.cloud import pubsub_v1
from google.auth import jwt

project_id = "beaming-key-305009"
subscription_id = "test-sub"
timeout = 10


service_account_info = json.load(
    open("beaming-key-305009-ad8ad55c19af-pub-sub-sa.json"))
audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(
    service_account_info, audience=audience
)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
# subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)


def callback(message):
    print(f"Received {message}.")
    message.ack()


streaming_pull_future = subscriber.subscribe(
    subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except Exception as e:
        streaming_pull_future.cancel()
        print(
            f"Listening for messages on {subscription_path} threw an exception: {e}."
        )
