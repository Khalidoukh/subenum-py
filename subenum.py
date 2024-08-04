import json
import re
import requests
import os 
from dotenv import *
def is_valid_domain(domain_name):
    # Regular expression for validating a domain name
    domain_regex = re.compile(
        r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.(?!-)[A-Za-z0-9-]{2,63}(?<!-)$'
    )
    return re.match(domain_regex, domain_name) is not None
load_dotenv()
domain_name=input("put your domain : ")
if is_valid_domain(domain_name) :

    api_key = os.getenv("security-trail-key")
    headers={"accept": "application/json","APIKEY": f"{api_key}"}

    r = requests.get(url=f"https://api.securitytrails.com/v1/domain/{domain_name}/subdomains?children_only=false&include_inactive=true",headers=headers)
    result = r.json()
    if "subdomains" in result:
        for subdomain in result["subdomains"] :
            domains = subdomain+"."+domain_name
            print(domains)
            with open(f"{domain_name}-sectrial-subdomains.txt", 'a') as file:
                  file.write(domains+ '\n')


    else:
        print("No subdomains found.")
        
else:
    print(f"{domain_name} is not a valid domain name. Please enter a valid one.")

