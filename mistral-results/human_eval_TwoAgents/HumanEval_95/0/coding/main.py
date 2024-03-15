# filename: main.py

def check_dict_case(input):
    return (len(input) > 1 and len(set(input.keys())) == len(input))

def test_check_dict_empty():
    assert check_dict_case({}) is False

def test_check_dict_single_key():
    assert check_dict_case({"a":"apple"}) is True

def run_tests(check_dict_case):
    test_cases = [
        {'input': {}, 'expected_output': False},
        {'input': {"a": "apple"}, 'expected_output': True},
        {'input': {"A": "apple", "B": "banana"}, 'expected_output': False},
        {'input': {"Name": "John", "Age": "36", "City": "Houston"}, 'expected_output': False},
        {'input': {"STATE": "NC", "ZIP": "12345"}, 'expected_output': True},
        {'input': {"a": "apple", 8: "banana", "a": "apple"}, 'expected_output': False},
        {'input': {}, 'expected_output': None}, # new test case for empty dictionary
    ]

    for test in test_cases:
        result = check_dict_case(test['input'])
        if test['expected_output'] is not None and result != test['expected_output']:
            print("Test failed")
            exit() # terminate the script in case of failure

if __name__ == "__main__":
    run_tests(check_dict_case)