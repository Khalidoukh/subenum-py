import datetime
import json
import re
import subprocess
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



    command = f"/home/xsh4dow/Bug-Bounty/1-Recon/SubEnum/subenum.sh -d {domain_name} -o {domain_name}-subenum-subdomains.txt"
    subprocess.run(command,shell=True)
else : print("error ")