from argparse import ArgumentParser
import sys

__version__ = "0.0.1"

def parse_commandline_arguments():
    parser = ArgumentParser(
        description="A project generator for serverless and headless projects.", prog="gen")
    parser.add_argument("-c", "--client",
                        dest="client", help="client name")
    parser.add_argument("-n", "--name",
                        dest="name", help="project name")
    parser.add_argument("-v", "--verbose", action="store_true",
                        dest="verbose", default=False, help="Prints verbose output.")
    args = parser.parse_args()

# print the usage message if no args are given
    if None == vars(args)["client"] or None == vars(args)["name"]:
        parser.print_help()
        sys.exit(1)

    return args


def create_project_name(args):
    client = vars(args)["client"] 
    name = vars(args)["name"]

    if None == client or None == name:
        raise AssertionError("client or name are missing")

    project_name = client + "_" + name

    return project_name


def main():

    args = parse_commandline_arguments()

    print("Welcome to the *less generator!")
    print("Version %s\n" % (__version__))
    print("Your arguments are:", args)
 
    proceed = input("Is this right? (y|n)")
    if "n" == proceed:
        print("\nGoodby.\n")
        sys.exit(1)

    print("\nGenerating project...\n")
    project_name = create_project_name(args)
    print("Project %s successfully generated.\n" % project_name)

if __name__ == '__main__':
    main()