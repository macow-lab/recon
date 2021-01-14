from faker import Faker
import requests

fake = Faker()

# Dictionary to keep track of available tests
modes = {
    "post-signup": "post-signup",
    "get-budget": "get-budget",
    "post-budget": "post-budget",
    "get-networth": "get-networth",
}

# Variables for testing
mode = modes["post-signup"]
baseurl = "http://localhost:5000"


if mode == modes["post-signup"]:
    print("Selected Test: {}".format(modes["post-signup"]))
    url = baseurl + "/signup"

    payload = {'username': fake.name().replace(" ", ""),
            'password': 'password',
            'email': '@recon.com'}
    payload["email"] = payload["username"] + payload["email"]
    
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload)
    
    print("Second test with duplicate email and username")
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload)

    print(response.text)
elif mode == modes["get-budget"]:
    print("Selected Test: {}".format(modes["get-budget"]))
    url = baseurl + "/budget"
    pass
elif mode == modes["post-budget"]:
    print("Selected Test: {}".format(modes["post-budget"]))
    url = baseurl + "/budget"
    pass
elif mode == modes["get-networth"]:
    print("Selected Test: {}".format(modes["get-networth"]))
    url = baseurl + "/networth"
    pass
elif mode == modes["post-networth"]:
    print("Selected Test: {}".format(modes["post-networth"]))
    url = baseurl + "/networth"
    pass
