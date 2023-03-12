import io
from contextlib import redirect_stdout, redirect_stderr
import requests
import random
import string
import json

def run_code(code):
    output = io.StringIO()
    try:
        with redirect_stdout(output):
            exec(code)
            result = output.getvalue().strip()
    except Exception as e:
        with redirect_stderr(output):
            exec(code)
            result = output.getvalue().strip()
    return result
    
def gen_pass():
        adjresp = requests.get("https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt")
        adj = random.choice(adjresp.text.split('\n'))
        nounresp = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
        noun = random.choice(nounresp.text.split("\n"))
        num = str(random.randrange(100))
        punct = random.choice(string.punctuation)
        passw = adj + noun + num + punct
        return passw
        
def covid():
    url = 'https://api.covid19api.com/world/total'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total_cases = data['TotalConfirmed']
        return total_cases
    else:
        return 'Error retrieving data'
        
def eemoji(text):
    url = 'https://levanter.onrender.com/emoji?q='
    respo = requests.get(url + text)
    image = json.loads(respo.content)
    
    return image['url']
    
def emix(text):
    url = 'https://levanter.onrender.com/emix?q='
    response = requests.get(url+text)
    data = json.loads(response.content)
    return data['result']