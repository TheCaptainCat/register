import sys

from register import bolinette

app = bolinette.app

if __name__ == '__main__':
    bolinette.run_command(sys.argv[1])
