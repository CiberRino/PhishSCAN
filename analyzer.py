import re
import requests
from scoring import score

def analyzer(URL,H):

    founds = []
    scor = 0

    shorteners = r"bit\.ly|tinyurl\.com|goo\.su|t\.co"
    Pattern = f"https?://({shorteners})/[a-zA-Z0-9]+"

    if re.findall(Pattern, URL):        
        scor += 10
        founds.append("shorteners")

    if "http://" in URL:
        scor += 5
        founds.append("http")
    
    if H == True:
        response = requests.get(URL)
        print(response.status_code)
    

    score(founds,scor)