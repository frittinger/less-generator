"""An action mechanism to run arbitrary actions according to a set of rules"""


class Action:
    def __init__(self, name):
        self.name = name

    def run(self):
        # print("Running action \"{0}\"".format(self.name))
        raise NotImplementedError()

    @staticmethod
    def run_sequential(action_list):
        for action in action_list:
            action.run()
