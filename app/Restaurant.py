class Restaurant:
    def __init__(self, restaurant_data: dict):

        self.name = restaurant_data['name']

        self.cuisines = ", ".join([cuisine['name'] for cuisine in restaurant_data['cuisines']])

        self.rating = float(restaurant_data['rating']['starRating'])
        # (e.g. 4.0 -> 4) - Convert to int if it's a whole number to remove the decimal point
        self.rating = int(self.rating) if self.rating.is_integer() else self.rating

        self.address = (
            restaurant_data['address']['firstLine']  + ', ' +
            restaurant_data['address']['city']       + ', ' +
            restaurant_data['address']['postalCode']
        )
