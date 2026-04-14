# import my classes and JET Color palette that got from: brand-box.marketing.just-eat.com
from models import Postcode, Restaurant, RestaurantView, JET_Orange, Tomato, Turmeric, BOLD, END
import requests, pyfiglet, shutil


# Fetch restaurant data from the Just Eat API for a given postcode
def fetch_restaurant(postcode_value: str) -> dict:
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


# Print a terminal banner and the exit instructions.
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


# Display the first 10 restaurants returned by the API.
def display_restaurants(json_data: dict) -> None:
    view = RestaurantView()
    restaurants = json_data.get("restaurants", [])
    
    if not restaurants: # empty or no results
        print(f"{Turmeric}No restaurants found for the given postcode.{END}")
        return
    
    # Loop through the first 10 restaurants and print their details
    for index, restaurant_arg in enumerate(restaurants[:10]):
        restaurant_obj = Restaurant(restaurant_arg)
        view.print_details(restaurant_obj, index)


# Run the console application loop and handle user input.
def main():    
    display_banner()
    while True:
        # Safely read user input and handle termination signals (Ctrl+D / Ctrl+C)
        try:
            postcode_input = input(f"{BOLD}\n> Enter a UK postcode (e.g. B263QJ): {END}")
        except EOFError:
            print("\nExiting (EOF received)...")
            break
        except KeyboardInterrupt:
            print("\nInterrupted (Ctrl+C). Exiting...")
            break

        # remove all whitespace characters from the start and end of the input and check if empty
        postcode_input = postcode_input.strip()
        if not postcode_input:
            print(f"{Tomato}Postcode cannot be empty. Please try again.{END}")
            continue
        postcode_obj = Postcode(postcode_input)
        
        # If the postcode is uk valid, fetch the restaurant json data and print
        if postcode_obj.is_uk_valid():
            try:
                json_data = fetch_restaurant(postcode_obj.value)
                display_restaurants(json_data)

            except Exception as e: # Handle any exceptions that occur
                print(e)

        # Allow user to exit the application using common exit commands
        elif postcode_input.lower().strip() in ["exit", "quit", "\q"]:
            print(f"{Turmeric}\nGoodbye{END}")
            return
        else:
            print(f"{Tomato}Invalid UK postcode, please try again.{END}")
        

# Start the application.
try:
    main()
except KeyboardInterrupt:
    print(f"{Turmeric}\nGoodbye{END}")
