import unittest
from two_tag_machine import two_tag_system

class TwoTagSystemTest(unittest.TestCase):
    def test_normal_halt(self):
        production_rules = [
            ('a', 'bc'),
            ('b', 'a'),
            ('c', 'aaa')
        ]
        initial_str = "aaa"
        result = two_tag_system(production_rules, initial_str)
        self.assertEqual(result, 'aaaa')

    def test_empty_initial_string(self):
        production_rules = [
            ('a', 'bc'),
            ('b', 'a'),
            ('c', 'aaa')
        ]

        result = two_tag_system(production_rules, '')
        self.assertEqual(result, '')

    def test_no_applicable_rule(self):
        production_rules = [
            ('x', 'y'), 
        ]
        initial_str = "aa"

        result = two_tag_system(production_rules, initial_str)
        self.assertEqual(result, "aa")

    def test_invalid_input_type(self):
        production_rules = [('a', 123)]  # Invalid rule value type (not a string)
        initial_str = "aa"

        with self.assertRaises(TypeError): 
            two_tag_system(production_rules, initial_str)

if __name__ == '__main__':
   unittest.main()
