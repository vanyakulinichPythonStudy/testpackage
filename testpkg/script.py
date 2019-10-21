import argparse
import sys

positional_args_choices = ['login', 'logout', 'analyze', 'config']

parser = argparse.ArgumentParser(
    prog="TEST", description="THIS IS TEST DESCRIPTION", epilog="END OF HELP INFO", allow_abbrev=False)
# login
subparser = parser.add_subparsers()
#
user = parser.add_argument_group('user commands')
user.add_argument('-in', '--login', action='store_true',
                  help='login help')
user.add_argument('-out', '--logout', action='store_true',
                  help='logout help')
#
config = parser.add_argument_group('config commands')
config.add_argument('-c', '--config', action='store_true',
                    help='config help')
config.add_argument('-l', '--list', action='store_true',
                    help='list additional option')
#
analyze = parser.add_argument_group('analysis commands')
analyze.add_argument('-a', '--analyze', action='store_true',
                     help='analyze help')
analyze.add_argument('--json', action='store_true',
                     help='json format to view results')
analyze.add_argument('--txt', action='store_true',
                     help='text format to view results')

# options = parser.add_argument_group()
# options.add_argument('--json', action='store_true',
#                      help='json format to view results')

# options.add_argument('--txt', action='store_true',
#                      help='text format to view results')

# options.add_argument()


def test():
    if len(sys.argv) == 1:
        parser.print_help()
        return
    parsed = parser.parse_args()
    print(vars(parsed))
