import re
import requests
from scoring import score

def analyzer(URL,H):

    sign = 0
    scor = 0
    count = 0

    shorteners = r"bit\.ly|tinyurl\.com|goo\.su|t\.co"
    pattern = f"https?://({shorteners})/[a-zA-Z0-9]+"
    patternIp4 = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b'


    for search in URL:
        if "-" in search:
            count += 1

    if count >= 4:
            scor += 5
            sign += 1
            print("[!] too much -")   

    if re.search(patternIp4, URL):
        scor += 10
        sign += 1
        print("[!] detected ip4")

    if re.findall(pattern, URL):        
        scor += 15
        sign += 1
        print("[!] shortener in the url")

    if "http://" in URL:
        scor += 10
        sign += 1
        print("[!] http in the url")
    
    if H:
        response = requests.get(URL)
        print(response.text)
        print(response.status_code)   

    score(sign,scor)
