#!/usr/bin/env python

import unittest

from password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    """
    A class for testing PasswordGenerator

    """
    def test_only_escaped_hyphen(self):
        """
        A test with '\-' as an alphabet

        """
        gen = PasswordGenerator(alphabet=r'\-', length=1)

        self.assertEqual(gen._processed_alphabet, ['-'])
        self.assertEqual(gen.generate_password(), '-')

    def test_escaped_hyphen(self):
        """
        A test for '\-' in an alphabet

        """
        gen = PasswordGenerator(alphabet=r'A-Ca\-z')

        self.assertEqual(sorted(gen._processed_alphabet),
                                                ['-', 'A', 'B', 'C', 'a', 'z'])

    def test_hyphen_at_begin(self):
        """
        A test if '-' in the begin of an alphabet

        """
        gen = PasswordGenerator(alphabet='-A-C')

        self.assertEqual(sorted(gen._processed_alphabet), ['-', 'A', 'B', 'C'])

    def test_hyphen_at_end(self):
        """
        A test if '-' in the end of an alphabet

        """
        gen = PasswordGenerator(alphabet='A-C-')

        self.assertEqual(sorted(gen._processed_alphabet), ['-', 'A', 'B', 'C'])

    def test_two_hyphens(self):
        """
        A test with '--' as an alphabet

        """
        gen = PasswordGenerator(alphabet='--')

        self.assertEqual(gen._processed_alphabet, ['-', '-'])


if __name__ == '__main__':
    unittest.main()

