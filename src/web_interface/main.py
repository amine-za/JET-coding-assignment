from pathlib import Path
import logging
import time

ROOT_DIR = Path(__file__).resolve().parents[1]

import requests
from models import Postcode, Restaurant
import streamlit as st

# Format restaurant details for display in the Streamlit UI.
class RestaurantWebView:
    def format_name(self, restaurant_obj: Restaurant) -> str:
        return f"**Name       :** {restaurant_obj.name}"

    def format_cuisines(self, restaurant_obj: Restaurant) -> str:
        return f"**Cuisines   :** {restaurant_obj.cuisines}"

    def format_rating(self, restaurant_obj: Restaurant) -> str:
        return f"**Rating     :** {restaurant_obj.rating} {'★' * int(restaurant_obj.rating)}"

    def format_address(self, restaurant_obj: Restaurant) -> str:  
        return f"**Address    :** {restaurant_obj.address} \n"

    def print_details(self, restaurant_obj: Restaurant, index: int) -> None:
        st.markdown(
            f"<h2 style='color:#ff8000;'>"
            f"🍽 Restaurant #{index + 1:02d}</h2>",
            unsafe_allow_html=True
        )
        st.write(self.format_name(restaurant_obj))
        st.write(self.format_cuisines(restaurant_obj))
        st.write(self.format_rating(restaurant_obj))
        st.write(self.format_address(restaurant_obj))
        st.divider()


# Fetch restaurant data from the Just Eat API for the given postcode.
def fetch_restaurants(postcode_value: str) -> dict:
    logging.info(f"Fetching data for {postcode_value}")
    url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/" + postcode_value
    
    headers = {
        "User-Agent": "Mozilla",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return (response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} Please try again.")


# Display the first 10 restaurants returned by the API.
def display_restaurants(json_data: dict) -> None:
    view = RestaurantWebView()
    restaurants = json_data.get("restaurants", [])
    
    if not restaurants: # empty or no results
        st.write("No restaurants found for the given postcode.")
    
    # Loop through the first 10 restaurants and print their details
    for index, restaurant_data in enumerate(restaurants[:10]):
        restaurant_obj = Restaurant(restaurant_data)
        view.print_details(restaurant_obj, index)


# Render the homepage banner and introduction text.
def display_homepage():
    time.sleep(0.1) # Small delay to ensure Streamlit loads static assets correctly on first render
    st.image(ROOT_DIR / "web_interface" / "assets" / "JET-banner.jpg")

    # Put Title and description and Subtitle
    st.markdown("<h1 style='color: rgb(255, 128, 0);'>Restaurant Finder</h1>", unsafe_allow_html=True)
    st.markdown(
        """ <p style='font-size:16px; margin-bottom: 10px;'>
        This project was built as part of the <a href="https://justeattakeaway.com" target="_blank">Just Eat Takeaway</a> coding assignment to explore their restaurant API and present the data in a clean interface.
        It allows users to search for restaurants using a UK postcode and view key details like cuisines, ratings, and address.
        You can view the source code on <a href="https://github.com/amine-za/JET-coding-assignment" target="_blank">GitHub</a>.
        </p> """, unsafe_allow_html=True
    )
    st.markdown("<h3 >Enter your postcode to find the best restaurants near you</h3>", unsafe_allow_html=True)


# Run the Streamlit app flow: input postcode, validate it, and display results.
def main():
    display_homepage()

    # Input box with placeholder
    st.write("*ps: This service is available only in the UK for UK postcodes. __Example: B263QJ__*")
    postcode_input = st.text_input(label="Postcode", placeholder="Enter postcode", label_visibility="collapsed")

    postcode_input = postcode_input.strip() #  remove all whitespace characters from the start and end of the input
    if not postcode_input:
        st.stop()

    postcode_obj = Postcode(postcode_input)

    # If the postcode is uk valid, fetch the restaurant json data from the API
    if postcode_obj.is_uk_valid():
        with st.spinner("Fetching Restaurants..."):
            try:
                json_data = fetch_restaurants(postcode_obj.value)
                display_restaurants(json_data)
            except Exception as e:
                st.error(str(e))
                st.stop()

    else:
        st.error("Invalid UK postcode, please try again.")

# Start the program
main()
