from cl_api import dns

import requests

def getGip():
    res = requests.get('https://ifconfig.me')
    return res.text

nowIP = getGip()

print(nowIP)

zone_identifier = "your zone identifier"
identifier = "your domain identifier"
email = "your email"
token = "your token"
ddnsDomain = "DDNS Domain"

data = dns.record.details(
    zone_identifier=zone_identifier,
    identifier=identifier,
    email=email,
    token=token,
)

print(data)

for domain in data["result"]:
    if (domain["name"] == ddnsDomain and domain["content"] != nowIP):
        print(domain)
        res = dns.record.patch(
            zone_identifier=zone_identifier,
            identifier=domain["id"],
            email=email,
            token=token,
            content=nowIP
        )
        print(res)