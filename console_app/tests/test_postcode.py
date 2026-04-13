from models import Postcode


def test_uk_postcodes():
    """
    Test valid UK postcodes. These should pass the UK validation.
    """
    # List of valid UK postcodes - postcodes from the subject
    valid_postcodes = ["EC4M7RF", "CT1 2EH", "BS1 4DJ", "L4 0TH", "NE9 7TY", "SW1A 1AA", \
            "CF11 8AZ", "M16 0RA", "EH1 1RE", "BN1 1AE",  "CB7 4DL",  "LS2 7HY", \
            "G3 8AG", "PL4 0DW", "B26 3QJ",  "DH4 5QZ", "BT7 1NN"]

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
