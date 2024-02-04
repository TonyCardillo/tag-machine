import unittest
from two_tag_machine import two_tag_system

class TwoTagSystemTest(unittest.TestCase):
    def test_normal_halt(self):
        # This should halt naturally after applying rules sequentially
        production_rules = [
            ('a', 'bc'),
            ('b', 'a'),
            ('c', 'aaa')
        ]
        initial_str = "aaa"
        result = two_tag_system(production_rules, initial_str)
        self.assertEqual(result, 'aaaa')  # Expected final state

    def test_infinite_loop(self):
        # This set of rules creates an infinite loop: a -> bc, b -> a...
        production_rules = [
            ('a', 'bc'),
            ('b', 'a')
        ]
        initial_str = "aa"

        # We cannot actually run this as it would create an infinite loop,
        # but we can discuss what would happen or how to modify the code
        # to detect and handle such loops.

    def test_empty_initial_string(self):
        production_rules = [
            ('a', 'bc'),
            ('b', 'a'),
            ('c', 'aaa')
        ]

        # An empty string should return immediately without modification
        result = two_tag_system(production_rules, '')
        self.assertEqual(result, '')

    def test_no_applicable_rule(self):
        production_rules = [
            ('x', 'y'),  # No rule for symbol 'a'
        ]
        initial_str = "aa"

        result = two_tag_system(production_rules, initial_str)
        self.assertEqual(result, "aa")  # Should remain unchanged

    def test_invalid_input_type(self):
        production_rules = [('a', 123)]  # Invalid rule value type (not a string)
        initial_str = "aa"

        with self.assertRaises(TypeError):  # Expecting TypeError due to invalid input type
            two_tag_system(production_rules, initial_str)

if __name__ == '__main__':
   unittest.main()
