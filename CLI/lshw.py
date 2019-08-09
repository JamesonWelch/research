
import argparse
import time

parser = argparse.ArgumentParser(description="Display lshw stdout in readable spead")

group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-f", "--file", action="store_true", help="Specify which file to send to stdout."
)

# .3 millisecond output
group.add_argument(
    "-n",
    "--normal",
    action="store_true",
    help="Output at human readable speed - 5000 miliseconds.",
)

# .05 millisecond output
group.add_argument(
    "-F", "--fast", action="store_true", help="Fast output at 3000 miliseconds."
)
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
group.add_argument(
    "-w",
    "--whitespace",
    action="store_true",
    help="Strip white space.",
)

args = parser.parse_args()


def file_selection(file_loc):
    with open(file_loc, "r") as f:
        files = f.read().splitlines()
    return files


def parse_file():
    def parse(speed):
        for line in file_selection("lshw.txt"):
            print(line.strip())
            time.sleep(speed)
    if args.single:
        start_time = time.time()
        parse(0.3)
        print("Duration: %s" % (time.time()-start_time))
    if args.repeat:
            while True:
                parse(0.03)
                    

if __name__ == '__main__':
    parse_file()