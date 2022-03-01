import pytest
from helpers import process_file, get_value_with_highest_key

# tests for exception handling in process_file
def test_process_file_exceptions():
    filename = 'test_file'
    cookie_file = open(filename, 'r')

    # test invalid file format
    with pytest.raises(Exception) as exception:
        _, __ = process_file(cookie_file, '2090-30-10')
    assert exception.type == IndexError
    assert exception.value.args[0] == "File format incorrect."
    cookie_file.close()


# tests for exception handling in get_value_with_highest_key
def test_get_value_with_highest_key_exceptions():

    test_case = {
        'string1' : 5,
        'string2' : 5
    }

    with pytest.raises(Exception) as exception:
        get_value_with_highest_key(test_case)
    assert exception.type == ValueError
    assert exception.value.args[0] == "Input dictionary keys must be numerical"


# General tests for get_value_with_highest_key
def test_get_value_with_highest_key():

    test_cases = [
        {}, # case 1 empty dictionary (corner case)
        {1 : 1, 2 : 2, 3 : 3},  # case 2 normal case
    ]

    test_cases_expected_result = [
        None,
        3
    ]

    for i in range(len(test_cases)):
        assert get_value_with_highest_key(test_cases[i]) == test_cases_expected_result[i]


# general tests for process_file
def test_process_file():
    filename = 'cookie_log.csv'
    cookie_file = open(filename, 'r')

    # case 1 when date is not in the file
    same_occurences_sets1, cookie_occurences_count1 = process_file(cookie_file, '2090-30-10')
    cookie_file.close()

    cookie_file = open(filename, 'r')
    # case 2 
    same_occurences_sets2, cookie_occurences_count2 = process_file(cookie_file, '2018-12-07')
    cookie_file.close()

    test_cases = {
        # case 1 we can check if the length of the results are 0, then we know the result is correct
        len(same_occurences_sets1) + len(cookie_occurences_count1) : 0,

        # case 2
        len(same_occurences_sets2) + len(cookie_occurences_count2) : 2,
        cookie_occurences_count2['4sMM2LxV07bPJzwf'] : 1

    }

    for case, correct_result in test_cases.items():
        assert case == correct_result
    