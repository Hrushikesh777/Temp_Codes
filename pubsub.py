import requests

subsciption = 'projects/beaming-key-305009/subscriptions/test-sub'
url = 'https://pubsub.googleapis.com/v1/' + subsciption + ':pull'
headers = {"Authorization": "Bearer ya29.c.KqYB9gfhPd-5BIAG2T5fagKTn2W9KUf5_ci26jaYfmIo6Bz2M48tMlNvV0TtsSt3PXYbWCjZdTQTMxfxpUVwilkpyslgCzcXFPfAtdG3MJAwYhZEp0OlhrRlLa691N4FrOAV2zMTDpx-Ac0_70dRbRbI8sdZoBBQbAyLUg_3dXcXzLr7bFnvioKq9t9PECNb49ET6_EHb3Gsr4g7R0Ov9f1n24wiV141_g"}
myobj = {"maxMessages": 1}

x = requests.post(url, data=myobj, headers=headers)
print(x.text.strip() == '{}')
print(type(x.text))
print(x.text)
