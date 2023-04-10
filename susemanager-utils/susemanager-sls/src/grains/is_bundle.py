import sys

def is_bundle():
    return {'is_bundle' : sys.executable == '/usr/lib/venv-salt-minion/bin/python'}
