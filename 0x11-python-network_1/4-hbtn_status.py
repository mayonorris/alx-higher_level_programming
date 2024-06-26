#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status using the requests package and displays the body of the response."""
import requests


if __name__ == "__main__":
    request = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
