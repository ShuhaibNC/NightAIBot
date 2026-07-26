import requests
import random
import string
import bs4
import re

def gen_pass():
        adjresp = requests.get("https://gist.githubusercontent.com/hugsy/8910dc78d208e40de42deb29e62df913/raw/eec99c5597a73f6a9240cab26965a8609fa0f6ea/english-adjectives.txt")
        adj = random.choice(adjresp.text.split('\n'))
        nounresp = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
        noun = random.choice(nounresp.text.split("\n"))
        num = str(random.randrange(100))
        punct = random.choice(string.punctuation)
        passw = adj + noun + num + punct
        return passw


async def msonescrap(query, key):
    resultlist = []

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://google.com"
    }

    print("\n========== MSONE SCRAPER DEBUG ==========")
    print(f"[DEBUG] Original query : {query!r}")
    print(f"[DEBUG] Requested key  : {key!r}")

    if " " in query:
        query = query.replace(" ", "+")

    print(f"[DEBUG] Modified query : {query!r}")

    url = f"https://malayalamsubtitles.org/?s={query}"
    print(f"[DEBUG] Request URL    : {url}")

    try:
        resp = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        print(f"[DEBUG] Status code    : {resp.status_code}")
        print(f"[DEBUG] Final URL      : {resp.url}")
        print(f"[DEBUG] Response size : {len(resp.content)} bytes")
        print(f"[DEBUG] Content-Type  : {resp.headers.get('Content-Type')}")
        print(f"[DEBUG] Encoding      : {resp.encoding}")

        # Useful for detecting 403/404/500/etc.
        resp.raise_for_status()

        soup = bs4.BeautifulSoup(resp.text, "html.parser")

        print(f"[DEBUG] Page title     : {soup.title.string.strip() if soup.title and soup.title.string else 'NO TITLE'}")

    except requests.exceptions.Timeout as e:
        print(f"[ERROR] Request timed out: {e}")
        print("[DEBUG] Returning: Nothing")
        return "Nothing"

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {type(e).__name__}: {e}")
        print("[DEBUG] Returning: Nothing")
        return "Nothing"

    except Exception as e:
        print(f"[ERROR] Parsing/request unexpected error: {type(e).__name__}: {e}")
        print("[DEBUG] Returning: Nothing")
        return "Nothing"

    try:
        if key == "link":
            title_links = soup.select("h2.entry-title a")

            print(f"[DEBUG] Found title links: {len(title_links)}")

            resultlist = [
                link.get("href")
                for link in title_links
                if link.get("href")
            ]

            print(f"[DEBUG] Extracted links: {len(resultlist)}")
            print(f"[DEBUG] Links: {resultlist}")

            if not resultlist:
                print("[WARNING] No links found")
                print("[DEBUG] Selector used: h2.entry-title a")
                print("[DEBUG] Returning: Nothing")
                return "Nothing"

            return resultlist

        elif key == "title":
            total_titles = soup.select("h2.entry-title a")

            print(f"[DEBUG] Found title elements: {len(total_titles)}")

            resultlist = [
                title.text.strip()
                for title in total_titles
            ]

            print(f"[DEBUG] Extracted titles: {len(resultlist)}")
            print(f"[DEBUG] Titles: {resultlist}")

            if not resultlist:
                print("[WARNING] No titles found")
                print("[DEBUG] Selector used: h2.entry-title a")
                print("[DEBUG] Returning: Nothing")
                return "Nothing"

            return resultlist

        elif key == "thumb":
            articles = soup.select("article.entry")

            print(f"[DEBUG] Found articles: {len(articles)}")

            image_links = []

            for i, article in enumerate(articles):
                img = article.select_one("img")

                if img:
                    src = img.get("src")
                    print(f"[DEBUG] Article #{i}: img src={src!r}")

                    if src:
                        image_links.append(src)
                else:
                    print(f"[DEBUG] Article #{i}: No <img> found")

            print(f"[DEBUG] Extracted thumbnails: {len(image_links)}")
            print(f"[DEBUG] Thumbnails: {image_links}")

            if not image_links:
                print("[WARNING] No thumbnails found")
                print("[DEBUG] Returning: Nothing")
                return "Nothing"

            return image_links

        else:
            print(f"[ERROR] Unknown key: {key!r}")
            print("[DEBUG] Valid keys: link, title, thumb")
            print("[DEBUG] Returning: Nothing")
            return "Nothing"

    except Exception as e:
        print(f"[ERROR] Extraction failed: {type(e).__name__}: {e}")
        print("[DEBUG] Returning: Nothing")
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