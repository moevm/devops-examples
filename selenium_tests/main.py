import unittest
import sys
from basic_selenium_test import BasicSeleniumTest
from test_page import TestPage


def main(host):
    suite = unittest.TestSuite()


    suite.addTest(
        BasicSeleniumTest.parametrize(
            TestPage,
            param=host))

    returnCode = not unittest.TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()

    BasicSeleniumTest.closeDriver()
    sys.exit(returnCode)


if __name__ == '__main__':
    host_arg = sys.argv[1]
    main(host_arg)

