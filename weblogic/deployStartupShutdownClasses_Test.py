
import wl
import unittest
import mock
from my_package import *

class TestApplyStartupClass(unittest.TestCase):
	def setUp(self):
		raise 'not implemented'
	def test_applyInexistentStartupClassOffline(self):
		raise 'not implemented'
	def test_applyInexistentStartupClassOnline(self):
		raise 'not implemented'
	def test_applyExistentStartupClassOffline(self):
		raise 'not implemented'
	def test_applyExistentStartupClassOnline(self):
		raise 'not implemented'
	def tearDown(self):
		raise 'not implemented'


	

class TestStartupClassesAbstraction(unittest.TestCase):

	def setUp(self):
		self.test_domain=None
		self.newStartupClass=None
		self.alreadyExistentStartupClass=None
	def test_includeNewStartupClassArgument(self):
		listOfExpectedStartupClasses=None
		self.test_domain.add(self.newStartupClass)
		assert(test_domain.get)
		self.assertTrue(test_domain.getStartupClasses()==listOfExpectedStartupClasses)

	def test_updateStartupClassArgument(self):
		self.test_domain.add(self.alreadyExistentStartupClass)
		self.assertTrue

if __name__ == "__main__" or __name == "main":
	unittest.main()
