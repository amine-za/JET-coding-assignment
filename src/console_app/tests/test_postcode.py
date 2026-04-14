from models import Postcode


def test_subject_postcodes():
    """
    Test valid UK postcodes. These should pass the UK validation.
    """
    # List of valid UK postcodes from the assignment subject
    valid_postcodes = ["EC4M7RF", "CT1 2EH", "BS1 4DJ", "L4 0TH", "NE9 7TY", "SW1A 1AA", \
            "CF11 8AZ", "M16 0RA", "EH1 1RE", "BN1 1AE",  "CB7 4DL",  "LS2 7HY", \
            "G3 8AG", "PL4 0DW", "B26 3QJ",  "DH4 5QZ", "BT7 1NN"]

    for postcode in valid_postcodes:
        assert Postcode(postcode).is_uk_valid() == True


def test_web_postcodes():
    """
    Test valid UK postcodes. These should pass the UK validation.
    """
    # List of valid UK postcodes from the web
    valid_postcodes = [
        "AB10 6DN", "WA14 2PU", "SP10 1PB", "KA7 1UB", "OX16 0BW", "BA1 2FJ", \
        "MK40 1ZL", "BT7 1JJ", "B3 2EW", "BH1 1SA", "BH2 5RR", "CM15 9GB", "BN1 2NW",\
        "BS8 4BF", "BS9 3UJ", "BS8 1ES", "GU15 3PQ", "CB2 1FD", "CF24 3DG",\
        "CM1 1TB", "GL52 2LY", "CH1 2HR", "SN15 2AB", "W4 4HH", "CO2 7NN", \
        "CV1 1ED", "CR9 1DF", "M20 6UG", "DD1 4BG", "EH1 1DD", "EH10 4BF", "EH2 4AT", \
        "EH7 4RR", "TW20 9HN", "KT17 1HX",  "GU14 6EW", "GU16 7JQ", "G12 8QZ",\
        "G2 1QX", "G3 6HB", "G41 3JA", "GL1 1TA", "GU1 2AG", "CM20 2AG", "HA1 2RH",\
        "RH12 1EH", "IV1 1LD", "KT1 1DN", "V32 4RB", "LS1 3AJ", "SG6 3BX", "L2 3PQ",\
        "EC1V 9LT", "NW3 6BT", "SW10 0BB", "SW1V 1BZ", "SW1W 0RH", "SW5 9FE", "SW7 1EE", \
        "SW7 3SS", "SW7 4UB", "W11 3JE", "W1F 9DB", "W1J 7QE", "W1T 1JY", "W1H 1PJ", \
        "W2 1NS", "WC2R 0DZ", "W1F 8QB", "SK11 7QJ", "SL6 1JN", "M14 5TD", "M3 4EL", \
        "M1 2HX", "OX2 7DL", "OX3 9FN", "PL1 1SB", "PO1 2SB", "PR1 2EF", "RG1 4QD", \
        "HA4 8JN", "S1 4NR", "SY1 1HN", "SO14 2BT", "AL1 1DT", "FK8 1BJ", "KT6 4JX", \
        "B72 1AB", "SN1 5BD", "TA1 1TD", "WD24 4AS", "KT13 8NA", "SK9 5AJ", "SO23 9AT", \
        "SL4 3BB", "GU21 5AH", "WV1 3AP", "WR1 2NT", "YO1 9RA"
    ]

    for postcode in valid_postcodes:
        assert Postcode(postcode).is_uk_valid() == True
    

def test_dutch_postcodes():
    """
    Test Dutch postcodes. These should fail the UK validation as they are not valid UK postcodes.
    """
    # List of invalid Dutch postcodes
    unvalid_postcodes1 = ["5667 PR", "9853 RC", "6336 WJ", "9461 HW", "8506 BG", "5583 XA", "7742 EE",\
                    "1073 HX", "7326 HB", "6524 DH", "9034 GZ", "8255 KJ", "1211 HX", "7031 WC"]

    for postcode in unvalid_postcodes1:
        assert Postcode(postcode).is_uk_valid() == False


def test_german_postcodes():
    """
    Test German postcodes. These should also fail the UK validation since they are not valid UK postcodes.
    """
    # List of invalid German postcodes
    unvalid_postcodes2 = ["10435", "91245", "27616", "56206", "84547", "84385", "89207", "67434", \
                    "84012", "37434", "24570", "33104", "49406", "31552", "91596", "59427"]

    for postcode in unvalid_postcodes2:
        assert Postcode(postcode).is_uk_valid() == False


def test_edge_case_postcodes():
    """
    Test edge cases for UK postcode validation.
    """
    # Invalid edge cases (should FAIL)
    invalid_edge_cases = ["", ".", "123456", "ABCDE", "EC1A 1B", "EC1A 111", "EC@1A 1BB",\
                            "EC1A-1BB", "EC1A 1BBB", "E C1A 1BB", " s3 2ss", "hello world", \
                            "JUST EAT TAKEAWAY", "EC4\nM7RF", "EC1A  1BB"]

    for postcode in invalid_edge_cases:
        assert Postcode(postcode).is_uk_valid() == False


def test_white_spaces():
    """
    Test a specific edge case with a tab character in the postcode. This should fail the UK validation.
    """
    assert Postcode("EC1A 1BB").is_uk_valid() == True
    assert Postcode("EC1A\t1BB").is_uk_valid() == False
    assert Postcode("EC1A\n1BB").is_uk_valid() == False
    assert Postcode("EC1A\f1BB").is_uk_valid() == False
    assert Postcode("EC1A\v1BB").is_uk_valid() == False
    assert Postcode("EC1A\r1BB").is_uk_valid() == False
