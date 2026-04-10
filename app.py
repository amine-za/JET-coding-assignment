import requests, re, pyfiglet, shutil

# The exact JET colors, source: brand-box.marketing.just-eat.com
JET_Orange = '\033[38;2;255;128;0m'
Tomato = '\033[38;2;247;94;40m'
Turmeric = '\033[38;2;246;194;67m'
BOLD = '\033[1m'
END = '\033[0m'
ITALIC = '\033[3m'
# Berry = '\033[38;2;242;166;176m'
# Aubergine = '\033[38;2;91;61;91m'
# WARNING = '\033[93m'


def get_data(input_postcode: str) -> dict:
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/" + input_postcode
    
    headers = {
        "User-Agent": "Mozilla",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        raise Exception(f"{Tomato}Failed to fetch data: {response.status_code}{END}")


def is_uk_postcode(postcode: str) -> bool:
    pattern = r"^[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}$"
    if re.match(pattern, postcode.upper()):
        return True
    return False


def put_separator_line(index: int) -> str:
    return (
        f"{JET_Orange}{'='*50}\n" +
        f"RESTAURANT #{index+1}".center(50) + "\n" +
        f"{'='*50}{END}\n"
    )


def format_name(restaurant: dict) -> str:
    return f"{BOLD}Name       :{END} {restaurant['name']}"


def format_cuisines(restaurant: dict) -> str:
    cuisines = ", ".join([cuisine['name'] for cuisine in restaurant['cuisines']])
    return f"{BOLD}Cuisines   :{END} {cuisines} "


def format_rating(restaurant: dict) -> str:        
    rating_num = float(restaurant['rating']['starRating']) # Convert the star rating to a number
    rating_num = int(rating_num) if rating_num.is_integer() else rating_num # Convert to int if it's a whole number, to remove the decimal point
    return f"{BOLD}Rating     :{END} {rating_num} {'★ ' * int(rating_num)}"


def format_address(restaurant: dict) -> str:  
    address = (
        restaurant['address']['firstLine']  + ', ' +
        restaurant['address']['city']       + ', ' +
        restaurant['address']['postalCode']
    )
    return f"{BOLD}Address    :{END} {address}"


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


def print_details(restaurant: dict, index: int) -> None:
    print (put_separator_line(index))
    print (format_name(restaurant))
    print (format_cuisines(restaurant))
    print (format_rating(restaurant))
    print (format_address(restaurant))


def main():    
    display_banner()
    try:
        while True:
            input_postcode = input(f"{BOLD}\n> Enter a UK postcode (e.g. EC4M7RF): {END}")
            if is_uk_postcode(input_postcode): # postcode is a valid UK postcode
                data = get_data(input_postcode) # Fetch the restaurant json data from the API

                if not data["restaurants"]: # if the restaurants list is empty, it means that there are no restaurants for the given postcode
                    print(f"{Turmeric}No restaurants found for the given postcode.{END}")
                
                # Loop through the first 10 restaurants and print their details
                for index, restaurant in enumerate(data["restaurants"][:10]):
                    print_details(restaurant, index)
        
            elif input_postcode.lower() in ["exit", "quit", "\q"]:
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
# - Use classes and OOP approach to make the code more modular and maintainable
# - Add more error handling (e.g. network errors, API errors, etc.)