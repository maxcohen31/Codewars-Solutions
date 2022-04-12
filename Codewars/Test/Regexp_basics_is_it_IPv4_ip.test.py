from Regexp_basics_is_it_IPv4_ip_6_kyu import ipv4_address
import unittest

class IPV4(unittest.TestCase):
    def test_1(self):
        data = '127.0.0.1'
        result = True
        self.assertEqual(ipv4_address(data), result)
    def test_1(self):
        data = ' 127.0.0.1'
        result = False
        self.assertEqual(ipv4_address(data), result)
    def test_1(self):
        data = '127.02.0.1'
        result = False
        self.assertEqual(ipv4_address(data), result)    
        
if __name__ == "__main__":
    unittest.main()        