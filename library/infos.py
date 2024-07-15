"""
Infos Modul (infos.py)
"""

import platform


def computer_name():
    """The networkname of the computer."""
    return platform.node()


def operating_system():
    """operating system of machine."""
    return platform.platform()


def cpu():
    return platform.processor()


def machine():
    return platform.machine()


def version():
    return platform.python_version_tuple()


def implementation():
    return platform.python_implementation()


def system():
    return platform.system(), platform.version()
