import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unitest.TestCase):
	def test_store_single_response(self):
		question = "What language did you first learn to speak"