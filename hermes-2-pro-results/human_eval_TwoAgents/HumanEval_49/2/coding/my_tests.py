# filename: my_tests.py

def run_tests(func, *args):
    succeeded = True
    try:
        for arg in args:
            print(*map(str, func(*arg))) # use map to apply str() function to each item in the list returned by the func
    except AssertionError as e:
        print(f'Test failed: {e}')
        succeeded = False
    if succeeded:
        print('All tests passed')