# (c) ShuhaibNC

import io
from contextlib import redirect_stdout, redirect_stderr
import requests
import random
import string
import json
import bs4
from PIL import Image, ImageDraw, ImageFont

def msonescrap(query, key):
    resultlist = []
    if " " in query:
        query = query.replace(' ', '+')
    resp = requests.get('https://malayalamsubtitles.org/?s='+query)
    soup = bs4.BeautifulSoup(resp.content, 'html.parser')
    if key == 'link':
        title_links = soup.find_all('a', class_='entry-title-link')
        for links in title_links:
            resultlist.append(links['href'])
        if not resultlist:
            return 'Nothing'
        else: return resultlist
    elif key == 'title':
        total_titles = soup.find_all('a', class_='entry-title-link')
        for titles in total_titles:
            resultlist.append(titles.get_text())
        if not resultlist:
            return 'Nothing'
        else:
            return resultlist

def run_code(code):
    output = io.StringIO()
    with redirect_stdout(output):
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
    
def catimage():
    image = ["https://i.imgur.com/IwRre0V.png","https://i.imgur.com/4aZlMPa.png","https://i.imgur.com/EEp2jtQ.png","https://i.imgur.com/ea7Ivps.png","https://i.imgur.com/CxouTiT.png","https://i.imgur.com/5ib8lL0.png","https://i.imgur.com/YhGnwKA.png","https://i.imgur.com/K8GphFQ.png","https://i.imgur.com/zrB3kwI.png","https://i.imgur.com/d4y82hH.png","https://i.imgur.com/lHZqKzi.png","https://i.imgur.com/dhuQljI.png","https://i.imgur.com/AXgK9eq.png","https://i.imgur.com/hbPAhtC.png","https://i.imgur.com/WZbiZJv.png","https://i.imgur.com/FCxTtOf.png","https://i.imgur.com/d4m4Grt.png","https://i.imgur.com/1gsmfoh.png","https://i.imgur.com/RKct0Qx.png","https://i.imgur.com/u4c59Fi.png","https://i.imgur.com/EYGlGQ7.png","https://i.imgur.com/JXiyghi.png","https://i.imgur.com/3WrDGrT.png","https://i.imgur.com/D3oeEc7.png","https://i.imgur.com/gnbOZIm.png","https://i.imgur.com/KPWWwvg.png","https://i.imgur.com/djmZiiV.png","https://i.imgur.com/pPlciN9.png","https://i.imgur.com/DZ8s0tR.png","https://i.imgur.com/s8NrwYk.png","https://i.imgur.com/s1RThQw.png","https://i.imgur.com/SiYCWY7.png","https://i.imgur.com/IF2ekZa.png","https://i.imgur.com/GqKwRlX.png","https://i.imgur.com/U5mWKSp.png","https://i.imgur.com/WkpTKit.png","https://i.imgur.com/3zssaMs.png","https://i.imgur.com/jvGOTYd.png","https://i.imgur.com/JBLdvSZ.png","https://i.imgur.com/7EN3mgz.png","https://i.imgur.com/sPQuJs4.png","https://i.imgur.com/1ASWQxy.png","https://i.imgur.com/k4sWdfU.png","https://i.imgur.com/cSujnZV.png","https://i.imgur.com/eF8ISdD.png","https://i.imgur.com/njxqsOx.png","https://i.imgur.com/ler9KmL.png","https://i.imgur.com/T5TDRf6.png","https://i.imgur.com/qf0Bh1S.png","https://i.imgur.com/BGakdjq.png","https://i.imgur.com/8yGY3uS.png","https://i.imgur.com/aNTZCgC.png","https://i.imgur.com/EaHQ3AJ.png","https://i.imgur.com/d1NKF7O.png","https://i.imgur.com/jnqHifF.png","https://i.imgur.com/2Ijm2qT.png","https://i.imgur.com/p94EP8r.png","https://i.imgur.com/TE3W4Mf.png","https://i.imgur.com/qMmZihq.png","https://i.imgur.com/RmltsiH.png","https://i.imgur.com/90X0ddu.png","https://i.imgur.com/yCM0LP3.png","https://i.imgur.com/K7lbNGj.png","https://i.imgur.com/TQZ7j77.png","https://i.imgur.com/bSTtPCC.png","https://i.imgur.com/jdl5vKy.png","https://i.imgur.com/0mkRAP2.png","https://i.imgur.com/vzWxTvr.png","https://i.imgur.com/E9daLGv.png","https://i.imgur.com/jKZUDfL.png","https://i.imgur.com/5vWvYfa.png","https://i.imgur.com/uMdaz5r.png","https://i.imgur.com/XpbV257.png","https://i.imgur.com/oNqBGLp.png","https://i.imgur.com/ksAR3IL.png","https://i.imgur.com/ixX65pT.png","https://i.imgur.com/ajgWdon.png","https://i.imgur.com/lbsHbJ2.png","https://i.imgur.com/OVJwKxB.png","https://i.imgur.com/UAuh6f5.png","https://i.imgur.com/zZPmOVS.png","https://i.imgur.com/WrjPpll.png","https://i.imgur.com/mKkfT5E.png","https://i.imgur.com/VOxAgdp.png","https://i.imgur.com/mR2bzw3.png","https://i.imgur.com/btEL6vw.png","https://i.imgur.com/oMA8Ww0.png","https://i.imgur.com/9jdcZRE.png","https://i.imgur.com/D472YrP.png","https://i.imgur.com/r6siMkJ.png","https://i.imgur.com/vUGwffT.png","https://i.imgur.com/EwFCsSt.png","https://i.imgur.com/veRARwD.png","https://i.imgur.com/HvdKI9R.png","https://i.imgur.com/XxJMwJE.png","https://i.imgur.com/TY2oiBR.png","https://i.imgur.com/LBif5wP.png","https://i.imgur.com/P7c3W9t.png","https://i.imgur.com/rVHg3Hz.png","https://i.imgur.com/ifrz9SL.png","https://i.imgur.com/TQGlu9y.png","https://i.imgur.com/eVGeRZn.png","https://i.imgur.com/K8Ovc2z.png","https://i.imgur.com/fHFFJQy.png","https://i.imgur.com/zhyzNyv.png","https://i.imgur.com/UwL7F78.png","https://i.imgur.com/w8eBYBq.png","https://i.imgur.com/mHi6BOk.png","https://i.imgur.com/JNsII8N.png","https://i.imgur.com/A3DcUzf.png","https://i.imgur.com/JnN8ijm.png","https://i.imgur.com/R8oLzFu.png","https://i.imgur.com/LWkQl8D.png","https://i.imgur.com/8YBKGt2.png","https://i.imgur.com/Oxt5xmg.png","https://i.imgur.com/9uKkH32.png","https://i.imgur.com/szmSQVV.png","https://i.imgur.com/hUsX3Ug.png","https://i.imgur.com/Jw9vOER.png","https://i.imgur.com/vjXHkJO.png","https://i.imgur.com/qMNS8ha.png","https://i.imgur.com/pepHYFI.png","https://i.imgur.com/KAqvYIP.png","https://i.imgur.com/2cOlHuI.png","https://i.imgur.com/4rWRqY9.png","https://i.imgur.com/y5lcVfN.png","https://i.imgur.com/ZADqXhQ.png","https://i.imgur.com/9j1JAW8.png","https://i.imgur.com/7xuVIZd.png","https://i.imgur.com/xEweZ9B.png","https://i.imgur.com/38EUjgJ.png","https://i.imgur.com/gekyrOS.png","https://i.imgur.com/5lqo6sg.png","https://i.imgur.com/QHZV150.png","https://i.imgur.com/9QXYxAt.png","https://i.imgur.com/vJFtYnY.png","https://i.imgur.com/FdyYRCM.png","https://i.imgur.com/ksKqA0a.png","https://i.imgur.com/18q5PYJ.png","https://i.imgur.com/1X4TVTv.png","https://i.imgur.com/bbLvCyz.png","https://i.imgur.com/iyd0yLW.png","https://i.imgur.com/DV92HR3.png","https://i.imgur.com/XiQO6gS.png","https://i.imgur.com/qEUMl9k.png","https://i.imgur.com/PwV3oA9.png","https://i.imgur.com/CK54Lpz.png","https://i.imgur.com/3Lbkw8v.png","https://i.imgur.com/VwTxVS2.png","https://i.imgur.com/v2pqqqf.png","https://i.imgur.com/WEqJddT.png","https://i.imgur.com/r2lDxqz.png","https://i.imgur.com/OzWRLde.png","https://i.imgur.com/PzvZSOS.png","https://i.imgur.com/KeIkeVy.png","https://i.imgur.com/9eZl8eU.png","https://i.imgur.com/MOWSuzE.png","https://i.imgur.com/zFjUk40.png","https://i.imgur.com/YS5CGEb.png","https://i.imgur.com/1k4Eji9.png","https://i.imgur.com/6YOFVkN.png","https://i.imgur.com/BaJD6Uq.png","https://i.imgur.com/o7yKPLM.png","https://i.imgur.com/610E0Bp.png","https://i.imgur.com/dGS6xm3.png","https://i.imgur.com/nqLeyqk.png","https://i.imgur.com/c1TEOsZ.png","https://i.imgur.com/7lwyzdf.png","https://i.imgur.com/Dm5v9vJ.png","https://i.imgur.com/kLFLXoY.png","https://i.imgur.com/8aame6S.png","https://i.imgur.com/sFdxoeV.png","https://i.imgur.com/uEOCCv5.png","https://i.imgur.com/vHUhZdD.png","https://i.imgur.com/KLSuEGi.png","https://i.imgur.com/rOuLKHi.png","https://i.imgur.com/Gm8ziKT.png","https://i.imgur.com/IMAppGQ.png","https://i.imgur.com/6neYZeB.png"]
    choice = random.choice(image)
    return choice
    
def get_thanosquote():
    thanos_quotes = [
    "Reality is often disappointing.",
    "I am inevitable.",
    "You're not the only one cursed with knowledge.",
    "Dread it. Run from it. Destiny still arrives.",
    "The hardest choices require the strongest wills.",
    "I ignored my destiny once, I can not do that again.",
    "The universe required correction. After that, the stones served no purpose beyond temptation.",
    "I thought by eliminating half of life, the other half would thrive, but you have shown me... that's impossible.",
    "The work is done. I won. What I'm about to do, I'm gonna enjoy it. Very, very much.",
    "Fun isn't something one considers when balancing the universe. But this... does put a smile on my face.",
]
    return random.choice(thanos_quotes)
    
def img_gen(text):
    image_width = 720
    image_height = 1080
    font_size = 50


    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('baloochettanm.ttf', font_size)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2
    draw.text((x, y), text, fill='black', font=font)
    image.save('img.png')