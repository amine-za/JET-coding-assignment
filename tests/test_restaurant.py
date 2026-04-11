from app import Restaurant

def test_restaurant_initialization():
    """
    Test the Restaurant initialization (constructore) with sample data.
    """
    sample_data = {
        'name': 'Testaurant',
        'cuisines': [{'name': 'Italian'}, {'name': 'Pizza'}],
        'rating': {'starRating': 4.5},
        'address': {
            'firstLine': '123 Test St',
            'city': 'Testville',
            'postalCode': 'TE1 2ST'
        }
    }

    restaurant = Restaurant(sample_data)

    assert restaurant.name == 'Testaurant'
    assert restaurant.cuisines == 'Italian, Pizza'
    assert restaurant.rating == 4.5
    assert restaurant.address == '123 Test St, Testville, TE1 2ST'


def test_restaurant_rating_formatting():
    """
    Test the formatting of the restaurant rating, ensuring that whole numbers are converted to integers
    """
    sample_data1 = {
        'name': 'Whole Star Restaurant',
        'cuisines': [{'name': 'French'}],
        'rating': {'starRating': 4.0},
        'address': {
            'firstLine': '456 Star Rd',
            'city': 'Star City',
            'postalCode': 'ST1 3AR'
        }
    }

    sample_data2 = {
        'name': 'Half Star Restaurant',
        'cuisines': [{'name': 'Mexican'}],
        'rating': {'starRating': 3.5},
        'address': {
            'firstLine': '789 Half St',
            'city': 'Halfville',
            'postalCode': 'HF1 4AL'
        }
    }

    restaurant1 = Restaurant(sample_data1)
    restaurant2 = Restaurant(sample_data2)

    assert restaurant1.rating == 4
    assert restaurant2.rating == 3.5


def test_restaurant_address_formatting():
    """
    Test the formatting of the restaurant address, ensuring that it combines the first line, city, and postal code correctly.
    """
    sample_data = {
        'name': 'Address Testaurant',
        'cuisines': [{'name': 'Japanese'}],
        'rating': {'starRating': 5.0},
        'address': {
            'firstLine': '321 Address Ln',
            'city': 'Addressville',
            'postalCode': 'AD1 5DR'
        }
    }

    restaurant = Restaurant(sample_data)

    assert restaurant.address == '321 Address Ln, Addressville, AD1 5DR'


def test_restaurant_empty_cuisines():
    """
    Test the handling of an empty cuisines list
    """
    sample_data = {
        'name': 'No Cuisine Restaurant',
        'cuisines': [],
        'rating': {'starRating': 2.0},
        'address': {
            'firstLine': '654 No Cuisine St',
            'city': 'Nocuisineville',
            'postalCode': 'NC1 6NO'
        }
    }

    restaurant = Restaurant(sample_data)

    assert restaurant.cuisines == ''


def test_restaurant_missing_fields():
    """
    Test the handling of all fields in the restaurant data are missing, ensuring that it raises appropriate exceptions or handles defaults.
    """
    incomplete_data = {
        'namew': 'Incomplete Restaurant',
        # 'cuisines' field is missing
        'ratinggg': {'starRating': 3.0},
        'addressss': {
            'firstLine': '987 Incomplete St',
            'city': 'Incompleteville',
            'postalCode': 'IC1 7IN'
        }
    }

    try:
        restaurant = Restaurant(incomplete_data)
        assert restaurant.name == ''
        assert restaurant.cuisines == ''
        assert restaurant.rating == ''
        assert restaurant.address == ''
        # assert False, "Expected an exception due to missing cuisines field"
    except KeyError:
        pass  # Expected exception due to missing field
