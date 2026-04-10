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


def get_header_block(index) -> str:
    return (
        f"{ORANGE}{'='*50}\n" +
        f"RESTAURANT #{index+1}".center(50) + "\n" +
        f"{'='*50}{END}\n"
    )


def get_name(restaurant) -> str:
    return f"{BOLD}Name       :{END} {restaurant['name']}"


def get_cuisines(restaurant) -> str:
    cuisines = ", ".join([cuisine['name'] for cuisine in restaurant['cuisines']])
    return f"{BOLD}Cuisines   :{END} {cuisines} "


def get_rating(restaurant) -> str:        
    rating_num = int(restaurant['rating']['starRating'])
    return f"{BOLD}Rating     :{END} {rating_num} {'★ ' * rating_num}"


def get_address(restaurant) -> str:  
    address = (
        restaurant['address']['firstLine']  + ', ' +
        restaurant['address']['city']       + ', ' +
        restaurant['address']['postalCode']
    )
    return f"{BOLD}Address    :{END} {address} \n\n"


def main():
    try:
        data = get_data() # Fetch the restaurant json data from the API

        # Loop through the first 10 restaurants and print their details
        for index, restaurant in enumerate(data["restaurants"][:10]):
            print (get_header_block(index))
            print (get_name(restaurant))
            print (get_cuisines(restaurant))
            print (get_rating(restaurant))
            print (get_address(restaurant))
            
    # Handle any exceptions that occur during the process
    except Exception as e:
        print(e)

main()
        