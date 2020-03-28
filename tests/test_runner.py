# -*- coding: utf-8 -*-

import unittest

from generator import runner


class BasicTest(unittest.TestCase):
    """Basic test cases."""

    def test_foo(self):
        assert True

    def test_create_project_name(self):
        args = {'client': "client", 'name': "name"}
        test_name = runner.create_project_name(args)
        self.assertEqual(test_name, "client_name")


if __name__ == '__main__':
    unittest.main()
