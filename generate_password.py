#!/usr/bin/python3

import argparse
import random
import string
import sys

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-l", "--length", dest="length", type=int, required=True)
arg_parser.add_argument("-s", "--symbols", dest="symbols", required=False, action="store_true")
arg_parser.add_argument("--all-symbols", dest="all_symbols", required=False, action="store_true")

args = arg_parser.parse_args()

symbols = '!@#$%^&*'
all_symbols = set(range(ord('!'), ord('@') + 1))

chars = string.ascii_letters + string.digits

if args.symbols:
    chars += symbols

if args.all_symbols:
    chars += all_symbols

chars = list(chars)

password = random.choices(chars, k=args.length)
print("".join(password))
