import sys

sys.argv.append('--python=application.tac')

from twisted.scripts import twistd
twistd.run()