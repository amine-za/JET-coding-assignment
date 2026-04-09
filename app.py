import requests, cloudscraper

def get_data() -> dict:
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"

    scraper = cloudscraper.create_scraper() # use cloudscraper to bypass Cloudflare's anti-bot protection in the jet api
    response = scraper.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def main():
    try:
        data = get_data()
        print(data)
    except Exception as e:
        print(e)

main()
