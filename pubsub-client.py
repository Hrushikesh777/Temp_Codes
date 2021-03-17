import json
from google.api_core import retry
from google.cloud import pubsub_v1
from google.auth import jwt

project_id = "beaming-key-305009"
subscription_id = "test-sub"


# service_account_info = json.load(
#     open("beaming-key-305009-ad8ad55c19af-pub-sub-sa.json"))
# audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

# credentials = jwt.Credentials.from_service_account_info(
#     service_account_info, audience=audience
# )

# subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

NUM_MESSAGES = 1

# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    # The subscriber pulls a specific number of messages. The actual
    # number of messages pulled may be smaller than max_messages.
    response = subscriber.pull(
        request={"subscription": subscription_path,
                 "max_messages": NUM_MESSAGES},
        retry=retry.Retry(deadline=300),
    )

    print(response)

    # ack_ids = []
    # for received_message in response.received_messages:
    #     print(f"Received: {received_message.message.data}.")
    #     ack_ids.append(received_message.ack_id)

    # # Acknowledges the received messages so they will not be sent again.
    # subscriber.acknowledge(
    #     request={"subscription": subscription_path, "ack_ids": ack_ids}
    # )

    # print(
    #     f"Received and acknowledged {len(response.received_messages)} messages from {subscription_path}."
    # )
