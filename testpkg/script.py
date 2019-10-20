import argparse


parser = argparse.ArgumentParser(
    # prefix_chars=''
    prog="TEST", description="THIS IS TEST DESCRIPTION", usage="%(prog)s [options]", epilog="END OF HELP INFO", allow_abbrev=False)

parser.add_argument('-a', '--analyze', type=str,
                    help='analyse command description', action='store', default='current path')


def test():
    print('main works with argparse')
    parsed = parser.parse_args()
    print(parsed)
