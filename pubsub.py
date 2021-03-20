import requests

subsciption = 'projects/beaming-key-305009/subscriptions/test-sub'
url = 'https://pubsub.googleapis.com/v1/' + subsciption + ':pull'
headers = {"Authorization": "Bearer *******************************************"}
myobj = {"maxMessages": 1}

x = requests.post(url, data=myobj, headers=headers)
print(x.text.strip() == '{}')
print(type(x.text))
print(x.text)
