import re


class Postcode:
    def __init__(self, postcode_input: str):
        self.value = postcode_input

    def is_uk_valid(self) -> bool:
        # UK postcode regex pattern
        pattern = r"^[A-Z]{1,2}[0-9][0-9A-Z]? ?[0-9][A-Z]{2}$"

        return re.fullmatch(pattern, self.value.upper()) is not None
