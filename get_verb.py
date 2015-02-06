from optparse import OptionParser
parser = OptionParser()
parser.add_option('-v', '--verbose', dest="verbose", default=False, action="store_true")
parser.add_option('-s', '--serial-numbers', dest="serial_num", default=False, action="store_true")
(opts, args) = parser.parse_args()
if opts.verbose:
    print "verbose is ON"
else:
    print "verbose is OFF"
if opts.serial_num:
    print "some sn here"
