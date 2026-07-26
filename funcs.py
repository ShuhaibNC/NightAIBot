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


async def msonescrap(query, key):
    resultlist = []

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://google.com"
    }

    logging.debug("========== MSONE SCRAPER ==========")
    logging.debug("Original query: %r", query)
    logging.debug("Requested key: %r", key)

    if " " in query:
        query = query.replace(" ", "+")

    logging.debug("Modified query: %r", query)

    url = f"https://malayalamsubtitles.org/?s={query}"
    logging.debug("Request URL: %s", url)

    try:
        resp = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        logging.debug("Status code: %s", resp.status_code)
        logging.debug("Final URL: %s", resp.url)
        logging.debug("Response size: %d bytes", len(resp.content))
        logging.debug("Content-Type: %s", resp.headers.get("Content-Type"))
        logging.debug("Encoding: %s", resp.encoding)

        resp.raise_for_status()

        soup = bs4.BeautifulSoup(resp.text, "html.parser")

        page_title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "NO TITLE"
        )

        logging.debug("Page title: %s", page_title)

    except requests.exceptions.Timeout:
        logging.exception(
            "MSONE request timed out | query=%r | url=%s",
            query,
            url
        )
        logging.debug("Returning: Nothing")
        return "Nothing"

    except requests.exceptions.RequestException:
        logging.exception(
            "MSONE HTTP request failed | query=%r | url=%s",
            query,
            url
        )
        logging.debug("Returning: Nothing")
        return "Nothing"

    except Exception:
        logging.exception(
            "Unexpected MSONE request/parsing error | query=%r | url=%s",
            query,
            url
        )
        logging.debug("Returning: Nothing")
        return "Nothing"

    try:
        if key == "link":
            title_links = soup.select("h2.entry-title a")

            logging.debug(
                "Found %d elements using selector: h2.entry-title a",
                len(title_links)
            )

            resultlist = [
                link.get("href")
                for link in title_links
                if link.get("href")
            ]

            logging.debug("Extracted %d links", len(resultlist))
            logging.debug("Links: %s", resultlist)

            if not resultlist:
                logging.warning(
                    "No MSONE links found | query=%r | status=%s | url=%s",
                    query,
                    resp.status_code,
                    resp.url
                )
                return "Nothing"

            return resultlist

        elif key == "title":
            total_titles = soup.select("h2.entry-title a")

            logging.debug(
                "Found %d title elements",
                len(total_titles)
            )

            resultlist = [
                title.text.strip()
                for title in total_titles
            ]

            logging.debug("Extracted %d titles", len(resultlist))
            logging.debug("Titles: %s", resultlist)

            if not resultlist:
                logging.warning(
                    "No MSONE titles found | query=%r | status=%s",
                    query,
                    resp.status_code
                )
                return "Nothing"

            return resultlist

        elif key == "thumb":
            articles = soup.select("article.entry")

            logging.debug("Found %d article elements", len(articles))

            image_links = []

            for i, article in enumerate(articles):
                img = article.select_one("img")

                if img:
                    src = img.get("src")

                    logging.debug(
                        "Article #%d image src: %r",
                        i,
                        src
                    )

                    if src:
                        image_links.append(src)
                else:
                    logging.debug(
                        "Article #%d has no image",
                        i
                    )

            logging.debug(
                "Extracted %d thumbnails",
                len(image_links)
            )
            logging.debug("Thumbnails: %s", image_links)

            if not image_links:
                logging.warning(
                    "No MSONE thumbnails found | query=%r | status=%s",
                    query,
                    resp.status_code
                )
                return "Nothing"

            return image_links

        else:
            logging.error(
                "Invalid MSONE scraper key: %r | query=%r",
                key,
                query
            )
            return "Nothing"

    except Exception:
        logging.exception(
            "MSONE extraction failed | query=%r | key=%r | url=%s",
            query,
            key,
            resp.url
        )
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