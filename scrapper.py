import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def fetch_page(url):
    """Download a page and return its HTML (or None if it fails)."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def parse_books(html):
    """Extract title, price, rating and availability from one page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for item in soup.find_all("article", class_="product_pod"):
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").get_text()
        rating_word = item.find("p", class_="star-rating")["class"][1]
        availability = item.find("p", class_="availability").get_text(strip=True)
        books.append({
            "title": title,
            "price": price,
            "rating": RATINGS.get(rating_word),
            "availability": availability,
        })
    return books


def main():
    print("Starting Web Scraping Project for CodeAlpha...")
    all_books = []

    for page in range(1, 51):  # pages 1 to 3 (change 4 to 51 for all 50 pages)
        url = BASE_URL.format(page)
        print(f"Scraping Page {page}: {url}")
        html = fetch_page(url)
        if html:
            books = parse_books(html)
            all_books.extend(books)
            print(f"-> Successfully extracted {len(books)} books.")
        time.sleep(1)  # be polite to the server

    df = pd.DataFrame(all_books)
    df.to_csv("books_data.csv", index=False)

    print(f"\nScraping complete! Total books scraped: {len(df)}")
    print("Data successfully saved to 'books_data.csv'.")


if __name__ == "__main__":
    main()