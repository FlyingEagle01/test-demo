import requests


r = requests.get("https://coreyms.com")
print(r.status_code)


def greet(name):
    print("Greet {}".format(name))
    if name == "Ryan":
        print("Greet {}, You are the BEST!".format(name))
