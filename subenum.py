import datetime
import json
import re
from bs4 import BeautifulSoup
import requests
import os 
from dotenv import *
from datetime import datetime

def is_valid_domain(domain_name):
    # Regular expression for validating a domain name
    domain_regex = re.compile(
        r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.(?!-)[A-Za-z0-9-]{2,63}(?<!-)$'
    )
    return re.match(domain_regex, domain_name) is not None
load_dotenv()
domain_name=input("put your domain : ")

if is_valid_domain(domain_name) :
    #securitytrails subdomain enumeration begin 

            api_key = os.getenv("security-trail-key")
            headers={"accept": "application/json","APIKEY": f"{api_key}"}

            r = requests.get(url=f"https://api.securitytrails.com/v1/domain/{domain_name}/subdomains?children_only=false&include_inactive=true",headers=headers)
            result = r.json()
            if "subdomains" in result:
                print(f"writing  security-trail subdomains to file : {domain_name}-sectrial-subdomains.txt ...")
                for subdomain in result["subdomains"] :
                    domains = subdomain+"."+domain_name
                    print(domains)
                    with open(f"{domain_name}-sectrial-subdomains.txt", 'a') as file:
                         file.write(domains+ '\n')


            else:
                print("No subdomains found.")
    #securitytrails subdomain enumeration end  
           
    #c99 subdomain enumeration begin 

headers = {
    "Cookie": "_ga_ZZYEJERZ89=GS1.1.1722817739.1.1.1722818739.0.0.0; _ga=GA1.1.1311909546.1722817739; _clck=35u5yt%7C2%7Cfo2%7C0%7C1678; _clsk=1ramcug%7C1722818742656%7C1%7C1%7Ch.clarity.ms%2Fcollect",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "same-origin",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "Connection": "close"
}
month = datetime.now().month # get the current month 

for n in range(month, 6, -1): 
    month = f"{month:02}"
    for i in range(10, 0, -1):
        day = f"{i:02}"  # Format the day as two digits

        url = f"https://subdomainfinder.c99.nl/scans/2024-{month}-{day}/{domain_name}"
        response =  requests.get(url, headers=headers)
        # Check if the response content  is bigger than  30000 (content len of not founding subs ) 
        if len(response.content) > 30000:
            soup = BeautifulSoup(response.content, 'html.parser')
            subdomains = soup.find_all('a', class_='link sd')  # Replace with the actual tag and class
            print(f"writing security-trail subdomains to file : {domain_name}-c99-subdomains.txt" ...")

            for subdomain in subdomains:
                print(subdomain.text)
                with open(f"{domain_name}-c99-subdomains.txt", 'a') as file:
                     file.write(subdomain.text + "\n")
            found = True 
            break            
            # Stop the loop once a successful response is found
        else:
            print(f"Failed to retrieve data for 2024-08-{i}. Status code: {response.status_code}")
    if found : 
         break

#c99 subdomain enumeration end 


           
        
else:
    print(f"{domain_name} is not a valid domain name. Please enter a valid one.")

