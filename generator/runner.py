import sys
from argparse import ArgumentParser
from subprocess import CalledProcessError

import generator.aws
import generator.data_storage
import generator.git

__version__ = "0.0.1"


def parse_commandline_arguments():
    parser = ArgumentParser(
        description="A project generator for serverless and headless projects.", prog="gen")
    parser.add_argument("-c", "--client",
                        dest="client", help="client name")
    parser.add_argument("-n", "--name",
                        dest="name", help="project name")
    parser.add_argument("-p", "--profile",
                        dest="profile", help="AWS profile")
    parser.add_argument("-v", "--verbose", action="store_true",
                        dest="verbose", default=False, help="Prints verbose output.")
    args = parser.parse_args()

    # print the usage message if no args are given
    if vars(args)["client"] is None or vars(args)["name"] is None:
        parser.print_help()
        sys.exit(1)

    return args


def create_project_name(local_data):
    client = local_data["client"]
    name = local_data["name"]

    if client is None or name is None:
        raise AssertionError("client or name are missing")

    project_name = client + "_" + name

    return project_name


def main():
    args = parse_commandline_arguments()

    print("Welcome to the *less generator!")
    print(f"Version {__version__}\n")
    print("Your arguments are:", args)

    proceed = input("Is this right? (y|n)")
    if "n" == proceed:
        print("\nGood by.\n")
        sys.exit(1)

    print("\nGenerating project...\n")
    local_data = {'client': vars(args)["client"], 'name': vars(args)["name"]}
    project_name = create_project_name(local_data)
    try:
        generator.git.create_git_repo(project_name)
        generator.data_storage.save_data_locally(project_name, local_data)
    except CalledProcessError:
        return 1

    try:
        generator.aws.aws_test(vars(args)["profile"])
    except AssertionError as e:
        print(e.args[0])
        return 1

    print("\nProject %s successfully generated.\n" % project_name)
    return 0


if __name__ == '__main__':
    sys.exit(main())
