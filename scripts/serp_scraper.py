import sys
import requests
from bs4 import BeautifulSoup
import json

def scrape_serp(keyword):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f"https://html.duckduckgo.com/html/?q={keyword.replace(' ', '+')}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for a in soup.find_all('a', class_='result__snippet', limit=5):
            results.append({'title': a.text, 'url': a['href']})
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"SERP research failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python serp_scraper.py '<keyword>'")
        sys.exit(1)
    scrape_serp(sys.argv[1])
