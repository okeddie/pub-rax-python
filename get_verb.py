from optparse import OptionParser
parser = OptionParser()
parser.add_option('-v', '--verbose', dest="verbose", default=False, action="store_true")
(options, args) = parser.parse_args()
if options.verbose:
    print "verbose is ON"
else:
    print "verbose is OFF"
