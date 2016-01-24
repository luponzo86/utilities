import sys
import argparse
parser = argparse.ArgumentParser()

# INPUT FILE (default: stdin)
parser.add_argument('infile', nargs='?', help="input file (default = stdin)", type=argparse.FileType('r'), default=sys.stdin)

# OUTPUT FILE (default: stdout)
parser.add_argument('outfile', nargs='?', help="output file (default = stdout)", type=argparse.FileType('w'), default=sys.stdout)

# POSITIONAL ARGUMENTS 
# (if type is not specified, by default they are treated as strings)
parser.add_argument("arg1", help="insert the argument description here", type=int)

# OPTIONAL ARGUMENTS
parser.add_argument("-o", "--option", help="optional argument (followed by a value)")
parser.add_argument("-x", "--flag", help="optional flag (default = FALSE)", action="store_true")
parser.add_argument("-f", "--file", help="additional optional input file", type=argparse.FileType('r'))

# CONFLICTING OPTIONS
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# parse the arguments in a namespace
args = parser.parse_args()
# the arguments can now be accessed with args.arg1, args.arg2, etc.
# By default, each variable as 'None' value:
if args.verbose:
    print "verbosity turned on"

# print all input arguments and options
print args 


# MAIN PROGRAM starts here



