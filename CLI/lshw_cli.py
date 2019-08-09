import os
import sys
import argparse
import time

parser = argparse.ArgumentParser(description="Display lshw stdout in readable spead")

group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-f", "--file", action="store_true", help="Specify which file to send to stdout."
)
group.add_argument(
    "-n",
    "--normal",
    action="store_true",
    help="Output at human readable speed - 5000 miliseconds.",
)
# group.add_argument(
#     "-f", "--fast", action="store_true", help="Fast output at 3000 miliseconds."
# )
group.add_argument(
    "-r",
    "--repeat",
    action="store_true",
    help="Repeat output indefinitely when list is exhausted.",
)
group.add_argument(
    "-s",
    "--single",
    action="store_true",
    help="Single loop through object and then stop.",
)

args = parser.parse_args()


def file_selection(file_loc):
    with open(file_loc, "r") as f:
        files = f.read()
    return files


print(file_selection("lshw.txt"))
