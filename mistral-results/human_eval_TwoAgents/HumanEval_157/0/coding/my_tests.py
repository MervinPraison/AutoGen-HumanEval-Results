# filename: my_tests.py
def run_tests(function):
    suite = unittest.TestSuite()

    # Add each test method in the class to the test suite individually
    for name in dir(TestRightAngleTriangle):
        if not name.startswith('__'):
            method = getattr(TestRightAngleTriangle, name)
            suite.addTest(unittest.FunctionTest(method))

    runner = unittest.TextTestRunner()
    return [test for test in runner.run(suite).tests if not test.wasSuccessful()]