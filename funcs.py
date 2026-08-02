import requests
import random
import string
import bs4
import re
import logging

def gen_pass():
        adjresp = requests.get("https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt")
        adj = random.choice(adjresp.text.split('\n'))
        nounresp = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
        noun = random.choice(nounresp.text.split("\n"))
        num = str(random.randrange(100))
        punct = random.choice(string.punctuation)
        passw = adj + noun + num + punct
        return passw

def msonescrap(query, key):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    session = requests.Session()
    session.headers.update(headers)

    logging.debug("========== MSONE SCRAPER ==========")
    logging.debug("Query: %s", query)
    logging.debug("Key: %s", key)

    url = "https://malayalamsubtitles.org/"
    params = {"s": query}

    try:
        resp = session.get(
            url,
            params=params,
            timeout=15,
            allow_redirects=True,
        )

        logging.debug("Status: %s", resp.status_code)
        logging.debug("URL: %s", resp.url)
        logging.debug("Server: %s", resp.headers.get("Server"))
        logging.debug("Content-Type: %s", resp.headers.get("Content-Type"))

        # Save HTML for debugging
        # with open("debug.html", "w", encoding="utf-8") as f:
        #     f.write(resp.text)

        if resp.status_code != 200:
            logging.error("HTTP %s", resp.status_code)
            logging.debug(resp.text[:1000])
            return "Nothing"

        soup = bs4.BeautifulSoup(resp.text, "html.parser")

    except requests.exceptions.RequestException:
        logging.exception("Request failed")
        return "Nothing"

    try:
        if key == "link":
            results = [
                a["href"]
                for a in soup.select("h2.entry-title a[href]")
            ]

        elif key == "title":
            results = [
                a.get_text(strip=True)
                for a in soup.select("h2.entry-title a")
            ]

        elif key == "thumb":
            results = []

            for article in soup.select("article.entry"):
                img = article.select_one("img")

                if not img:
                    continue

                src = (
                    img.get("src")
                    or img.get("data-src")
                    or img.get("data-lazy-src")
                )

                if src:
                    results.append(src)

        else:
            logging.error("Invalid key: %s", key)
            return "Nothing"

        logging.debug("Found %d results", len(results))

        if not results:
            return "Nothing"

        return results

    except Exception:
        logging.exception("Parsing failed")
        return "Nothing"    
    
async def remove_duplicates(titles, links):
    unique_titles = []
    unique_links = []
    for i, title in enumerate(titles):
        if title not in unique_titles:  
            unique_titles.append(title)
            unique_links.append(links[i])
    return unique_titles, unique_links   

async def sanitize_filename(filename):
    # Replace invalid characters with an underscore or remove them
    return re.sub(r'[\/:*?"<>|]', '_', filename)

async def get_filename_from_cd(response):
    """
    Extracts filename from Content-Disposition header if present.
    """
    if 'Content-Disposition' in response.headers:
        cd = response.headers['Content-Disposition']
        filename = re.findall('filename="(.+)"', cd)
        if filename:
            return filename[0]
    return None 