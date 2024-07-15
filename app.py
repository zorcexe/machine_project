"""
Einstiegs-Datei in das Machine-Projekt
Informationen über das Betriebssystem mit dem platform - Modul
"""

# import this  ZEN of Python
import sys
import random

import check

# Funktion hello_again aus dem Check-Modul importieren
from check import hello_again

# das infos-Modul aus Package library importieren
from library import infos


def main():
    # gebe die Infos für das OS aus
    print("*" * 40)
    print("System Infos")
    print(infos.computer_name())  # data
    print(infos.operating_system())
    print(infos.cpu())
    print(infos.machine())
    print(infos.version())  # ('3', '11', '3') major, minor, patch
    print(infos.implementation())  # CPython / Micropython / Pypy
    print(infos.system())
    print("*" * 40)


# random.randint(3, 4) # Zugriff über random-Namespace
# check Namespace via Dot-Notation
check.say_hello()
hello_again()

# an diesen Orten sucht Python nach einem Modul
print(sys.path)

# diese Module sind schon geladen, da Python diese
# Module z.b. benötigt werden:
print("*" * 40)
# for key, value in sys.modules.items():
#     print(key, value)


main()
