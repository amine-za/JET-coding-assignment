import requests, pyfiglet, shutil
# import my classes and JET Color palette that i got from: brand-box.marketing.just-eat.com
from app import Postcode, Restaurant, RestaurantView, JET_Orange, Tomato, Turmeric, BOLD, END


def get_data(postcode_value: str) -> dict:
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/" + postcode_value
    
    headers = {
        "User-Agent": "Mozilla",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        raise Exception(f"{Tomato}Failed to fetch data: {response.status_code}{END}")


def display_banner() -> None:
    text = pyfiglet.figlet_format("RESTAURANT\nFINDER", font="small")
    width = shutil.get_terminal_size().columns
    max_line_width = max(len(line) for line in text)

    # If the banner is wider than the terminal, print a simple text
    if max_line_width > width:
        print(f"{JET_Orange}RESTAURANT FINDER{END}")
    else:
        print(f"{JET_Orange}{text}{END}")
    
    print(f"Type {Turmeric}EXIT - QUIT - \q{END} anytime to quit the program{END}")


def main():    
    display_banner()
    try:
        while True:
            postcode_input = input(f"{BOLD}\n> Enter a UK postcode (e.g. EC4M7RF): {END}")
            postcode_obj = Postcode(postcode_input)
            
            # If the postcode is uk valid, fetch the restaurant json data from the API
            if postcode_obj.is_uk_valid():
                json_data = get_data(postcode_obj.value)

                # empty results
                if not json_data["restaurants"]:
                    print(f"{Turmeric}No restaurants found for the given postcode.{END}")
                
                # Loop through the first 10 restaurants and print their details
                for index, restaurant_arg in enumerate(json_data["restaurants"][:10]):
                    restaurant_obj = Restaurant(restaurant_arg)
                    view = RestaurantView()
                    view.print_details(restaurant_obj, index)
        
            elif postcode_input.lower() in ["exit", "quit", "\q"]:
                print(f"{Turmeric}\nGoodbye 👋{END}")
                return

            else:
                print(f"{Tomato}Invalid UK postcode, please try again.{END}")
        
    # Handle any exceptions that occur during the process
    except Exception as e:
        print(e)

try:
    main()
except KeyboardInterrupt:
    print(f"{Turmeric}\nGoodbye 👋{END}")


# TO-DO:
# - Add unit tests for the functions
# - Add more error handling (e.g. network errors, API errors, etc.)
