from .Restaurant import Restaurant

# The exact JET Color palette, source: brand-box.marketing.just-eat.com
JET_Orange = '\033[38;2;255;128;0m'
Tomato = '\033[38;2;247;94;40m'
Turmeric = '\033[38;2;246;194;67m'
BOLD = '\033[1m'
END = '\033[0m'
ITALIC = '\033[3m'
# Berry = '\033[38;2;242;166;176m'
# Aubergine = '\033[38;2;91;61;91m'
# WARNING = '\033[93m'


class RestaurantView:
    def format_name(self, restaurant_obj: Restaurant) -> str:
        return f"{BOLD}Name       :{END} {restaurant_obj.name}"

    def format_cuisines(self, restaurant_obj: Restaurant) -> str:
        return f"{BOLD}Cuisines   :{END} {restaurant_obj.cuisines}"

    def format_rating(self, restaurant_obj: Restaurant) -> str:
        return f"{BOLD}Rating     :{END} {restaurant_obj.rating} {'★ ' * int(restaurant_obj.rating)}"

    def format_address(self, restaurant_obj: Restaurant) -> str:  
        return f"{BOLD}Address    :{END} {restaurant_obj.address} \n"

    def print_details(self, restaurant_obj: Restaurant, index: int) -> None:
        separator_line = (
            f"{JET_Orange}{'='*50}\n" +
            f"RESTAURANT #{index+1}".center(50) + "\n" +
            f"{'='*50}{END}"
        )

        print (separator_line)
        print (self.format_name(restaurant_obj))
        print (self.format_cuisines(restaurant_obj))
        print (self.format_rating(restaurant_obj))
        print (self.format_address(restaurant_obj))
