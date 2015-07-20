import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', dest="verbose", default=False, action="store_true")
parser.add_argument('-s', '--serial-numbers', dest="serial_num", default=False, action="store_true")
args = parser.parse_args()
if args.verbose:
    print "verbose is ON"
else:
    print "verbose is OFF"
if args.serial_num:
    print "some sn here"
