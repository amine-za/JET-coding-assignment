import requests


ORANGE = '\033[1m\033[38;5;214m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


def get_data():
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
    headers = {
        "User-Agent": "Mozilla",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


def main():
    try:
        data = get_data() # Fetch the restaurant json data from the API

        # Loop through the first 10 restaurants and print their details
        for index, restaurant in enumerate(data["restaurants"][:10]):
            cuisines = ", ".join([cuisine['name'] for cuisine in restaurant['cuisines']])
            rating_num = int(restaurant['rating']['starRating'])
            address = (
                restaurant['address']['firstLine']  + ', ' +
                restaurant['address']['city']       + ', ' +
                restaurant['address']['postalCode']
            )
            
            print(f"{ORANGE}{'='*55}{END}")
            print(f"{ORANGE} RESTAURANT #{index+1} {END}".center(55))
            print(f"{ORANGE}{'='*55}{END}")

            print(f"{BOLD}Name       :{END} {restaurant['name']}")
            print(f"{BOLD}Cuisines   :{END} {cuisines} ")
            print(f"{BOLD}Rating     :{END} {rating_num} {'★ ' * rating_num}")
            print(f"{BOLD}Address    :{END} {address}", end="\n\n\n")

    # Handle any exceptions that occur during the process
    except Exception as e:
        print(e)

main()
        