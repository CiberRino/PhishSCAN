import re
import requests
import tldextract
from scoring import score


def analyzer(URL,H):

    sign = 0
    total_score = 0

    try:

        count_guion = URL.count("-")
        count_characters = len(tldextract.extract(URL).domain)
        ext = tldextract.extract(URL).subdomain
        domain = tldextract.extract(URL).registered_domain

        pattern = f"https?://({domain})/[a-zA-Z0-9]+"
        patternIp4 = r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b'

        if ext:
            lista_subdominios = ext.split('.')
            count_subdomain = len(lista_subdominios)

            if count_subdomain >= 4:
                total_score += 5
                sign += 1 
                print(f"[!] too much subdomains: {count_subdomain}")

        if count_characters >= 25:
            total_score += 5
            sign += 1
            print(f"[!] too much characters: {count_characters}") 

        if count_guion >= 4:
                total_score += 5
                sign += 1
                print(f"[!] too much - : {count_guion}")  

        if re.search(patternIp4, URL):
            total_score += 15
            sign += 1
            print("[!] detected ip4")

        if re.findall(pattern, URL):        
            total_score += 15
            sign += 1
            print("[!] shortener in the url")

        if "http://" in URL:
            total_score += 10
            sign += 1
            print("[!] http in the url")

        if H:
            try:
                response = requests.get(URL)

                if response.history:
                    total_score += 5
                    print("[!] there was a redirection")
                    for redirect in response.history:
                        print(redirect.status_code, redirect.url)

                    print("End:", response.status_code, response.url)
                else:
                    print(response.status_code)
                    print(response.text)
            except requests.exceptions.RequestException as s:
                print(f"error: {s}")

        score(sign,total_score)

    except requests.exceptions.RequestException as r:
        print(r)