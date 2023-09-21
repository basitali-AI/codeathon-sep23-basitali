import unittest
from code3 import validate_ip_address

class TestValidateIPAddress(unittest.TestCase):
    def test_valid_ip_address(self):
        # Test that the function returns True for a valid IP address
        self.assertTrue(validate_ip_address('255.255.0.0'))
        
    def test_invalid_ip_address(self):
        # Test that the function returns False for an invalid IP address
        self.assertFalse(validate_ip_address('555.555.555.555'))
        
    def test_out_of_range_component(self):
        # Test that the function returns False for an IP address with a component out of range
        self.assertFalse(validate_ip_address('256.255.0.0'))
        
    def test_missing_components(self):
        # Test that the function returns False for an IP address with missing components
        self.assertFalse(validate_ip_address('255.255.0'))
        
    def test_non_numeric_component(self):
        # Test that the function returns False for an IP address with a non-numeric component
        self.assertFalse(validate_ip_address('255.255.0.a'))
