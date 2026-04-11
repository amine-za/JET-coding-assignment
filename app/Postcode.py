import re

class Postcode:
    def __init__(self, postcode_input: str):
        self.value = postcode_input

    def is_uk_valid(self) -> bool:
        # UK postcode regex pattern
        pattern = r'^[A-Z]{1,2}\d{1,2}[A-Z]? ?\d[A-Z]{2}$'
        return re.match(pattern, self.value.upper()) is not None
