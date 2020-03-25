# -*- coding: utf-8 -*-

import argparse
import unittest

from generator import runner


class BasicTest(unittest.TestCase):
    """Basic test cases."""

    def test_foo(self):
        assert True

    def test_create_project_name(self):
        
        args = argparse.Namespace()
        args.client = "client"
        args.name = "name"
        test_name = runner.create_project_name(args)
        self.assertEqual(test_name, "client_name")

if __name__ == '__main__':
    unittest.main()