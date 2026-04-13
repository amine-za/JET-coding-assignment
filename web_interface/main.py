import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

import requests
from models import Postcode, Restaurant, JET_Orange, Tomato, Turmeric, BOLD, END
import streamlit as st


class RestaurantWebView:
    def format_name(self, restaurant_obj: Restaurant) -> str:
        return f"**Name       :** {restaurant_obj.name}"

    def format_cuisines(self, restaurant_obj: Restaurant) -> str:
        return f"**Cuisines   :** {restaurant_obj.cuisines}"

    def format_rating(self, restaurant_obj: Restaurant) -> str:
        return f"**Rating     :** {restaurant_obj.rating} {'★ ' * int(restaurant_obj.rating)}"

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
        raise Exception(f"Failed to fetch data: {response.status_code} Please try again.")


# Execution starts here
st.image(ROOT_DIR / "assets" / "JET-banner.jpg")

# Put Title and description and Subtitle
st.markdown("<h1 style='color: rgb(255, 128, 0);'>Restaurant Finder</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='font-size:16px; margin-bottom: 10px;'>
    This project was built as part of the <a href="https://justeattakeaway.com" target="_blank">Just Eat Takeaway</a> coding assignment to explore their restaurant API and present the data in a clean interface.
    It allows users to search for restaurants using a UK postcode and view key details like cuisines, ratings, and address.
    You can view the source code on <a href="https://github.com/amine-za/JET-coding-assignment" target="_blank">GitHub</a>.
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("<h3 >Enter your postcode to find the best restaurants near you</h3>", unsafe_allow_html=True)

# Input box with placeholder
st.write("*ps: This service is available only in the UK for UK postcodes. __Example: B263QJ__*")
postcode_input = st.text_input(label="Postcode", placeholder="Enter postcode", label_visibility="collapsed")


if not postcode_input:
    st.stop()

postcode_obj = Postcode(postcode_input)

# If the postcode is uk valid, fetch the restaurant json data from the API
if postcode_obj.is_uk_valid():
    try:
        json_data = get_data(postcode_obj.value)
    except Exception as e:
        st.error(str(e))
        st.stop()

    # empty results
    if not json_data["restaurants"]:
        st.write("No restaurants found for the given postcode.")
    
    # Loop through the first 10 restaurants and print their details
    for index, restaurant_data in enumerate(json_data["restaurants"][:10]):
        restaurant_obj = Restaurant(restaurant_data)
        view = RestaurantWebView()
        view.print_details(restaurant_obj, index)

else:
    st.error("Invalid UK postcode, please try again.")

# Handle any exceptions that occur during the process

