import requests
import unittest

#Test cases to test gitlab repos' availability
#You always create  a child class derived from unittest.TestCase

class TestGithub(unittest.TestCase):
    #Each test method starts with the keyword test_
    def test_public_repo(self):
        resp=requests.get('https://github.com/moevm/devops-examples')
        self.assertEqual(resp.status_code, 200)
    def test_private_repo(self):
        resp=requests.get('https://github.com/anchud/closed_repository')
        self.assertEqual(resp.status_code, 404)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
