# -*- coding: utf-8 -*-

import unittest

from generator import actions


class DerivedAction(actions.Action):
    def __init__(self, name):
        super().__init__(name)


class DerivedActionWithRun(actions.Action):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        pass


class BasicActionTest(unittest.TestCase):
    """Basic test cases for actions."""

    def test_action_name(self):
        action_name = "action_name"
        action = actions.Action(action_name)
        self.assertEqual(action_name, action.name)

    def test_subclassed_name(self):
        action_name = "action_name"
        action = DerivedAction(action_name)
        self.assertEqual(action_name, action.name)

    def test_subclassed_unimplemented_run(self):
        action_name = "action_name"
        action = DerivedAction(action_name)
        self.assertRaises(NotImplementedError, action.run)

    def test_run_sequential(self):
        action_list = [DerivedActionWithRun("one"), DerivedActionWithRun("two")]
        actions.Action.run_sequential(action_list)


if __name__ == '__main__':
    unittest.main()
