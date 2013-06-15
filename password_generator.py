#!/usr/bin/env python


class PasswordGenerator:
    """
    A class for generating passwords with giving alphabet and length

    """
    def _generate_sequence(self, b, e):
        """
        Returns iterator to the sequence [b, e] if b >= e,
        raises ValueError otherwise

        """
        if ord(b) > ord(e):
            raise ValueError('begin must be less/equal than end')
        return map(chr, range(ord(b), ord(e) + 1))

    def _process_alphabet(self, alphabet):
        """
        Returns the given alphabet processed.
        Raises ValueError if can't process something

        """
        import re

        processed_alphabet = []
        pattern = re.compile(r'.\-.')
        for s in pattern.finditer(alphabet):
            try:
                processed_alphabet.extend(self._generate_sequence(
                                                s.group(0)[0], s.group(0)[2]))
            except ValueError:
                raise ValueError('Error while processing {}'.format(s))
        processed_alphabet.extend(pattern.sub('', alphabet))
        return processed_alphabet

    def __init__(self, alphabet='A-Za-z0-9', length=16):
        self.alphabet, self.length = alphabet, length

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, a):
        self._alphabet = a
        self._processed_alphabet = self._process_alphabet(self.alphabet)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, l):
        if not l > 0:
            raise ValueError('length must be greater than zero')
        self._length = l

    def generate_password(self):
        import random

        return ''.join(random.choice(self._processed_alphabet)
                        for _ in range(self.length))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', metavar='ALPHABET',
                        help='set the alphabet for the generator '
                        '(default: A-Za-z0-9). For including a "-" use \- '
                        'or put it first or last like -A-Z or A-Z-',
                        type=str, default='A-Za-z0-9')
    parser.add_argument('-l', metavar='LENGTH',
                        help='set the length for the password (default: 16)',
                        type=int, default=16)
    args = parser.parse_args()
    generator = PasswordGenerator(args.a, args.l)
    print(generator.generate_password())
