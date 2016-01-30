## This script extracts single fields from the ATOM section of a pdb.
## 
## COLUMNS        DATA  TYPE    FIELD        DEFINITION
## -------------------------------------------------------------------------------------
##  1 -  6        Record name   "ATOM  "
##  7 - 11        Integer       serial       Atom  serial number.
## 13 - 16        Atom          name         Atom name.
## 17             Character     altLoc       Alternate location indicator.
## 18 - 20        Residue name  resName      Residue name.
## 22             Character     chainID      Chain identifier.
## 23 - 26        Integer       resSeq       Residue sequence number.
## 27             AChar         iCode        Code for insertion of residues.
## 31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
## 39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
## 47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
## 55 - 60        Real(6.2)     occupancy    Occupancy.
## 61 - 66        Real(6.2)     tempFactor   Temperature  factor.
## 77 - 78        LString(2)    element      Element symbol, right-justified.
## 79 - 80        LString(2)    charge       Charge  on the atom.

import sys
import argparse
parser = argparse.ArgumentParser()

## INPUT FILE (default: stdin)
parser.add_argument('infile', nargs='?', help="input PDB file (default = stdin)", type=argparse.FileType('r'), default=sys.stdin)

## OUTPUT FILE (default: stdout)
parser.add_argument('outfile', nargs='?', help="output file (default = stdout)", type=argparse.FileType('w'), default=sys.stdout)

## POSITIONAL ARGUMENTS 
## (if type is not specified, by default they are treated as strings)
# parser.add_argument("arg1", help="insert the argument description here", type=int)

## OPTIONAL ARGUMENTS
# parser.add_argument("-o", "--option",  help="optional argument (followed by a value)")
parser.add_argument("-A", "--cAlpha",  help="select only CA atom",                action="store_true")
parser.add_argument("-P", "--parse",   help="print a parsed version of input",    action="store_true")
parser.add_argument("-C", "--xyz",     help="print XYZ coordinates",              action="store_true")
parser.add_argument("-s", "--serial",  help="print atom serial number",           action="store_true")
parser.add_argument("-n", "--name",    help="print atom name",                    action="store_true")
parser.add_argument("-l", "--altLoc",  help="print alternate location indicator", action="store_true")
parser.add_argument("-r", "--resName", help="print residue name",                 action="store_true")
parser.add_argument("-c", "--chain",   help="print chain identifier",             action="store_true")
parser.add_argument("-i", "--resSeq",  help="print residue sequence number",      action="store_true")
parser.add_argument("-d", "--iCode",   help="print code for residue insertion",   action="store_true")
parser.add_argument("-x",              help="print X coordinate",                 action="store_true")
parser.add_argument("-y",              help="print Y coordinate",                 action="store_true")
parser.add_argument("-z",              help="print Z coordinate",                 action="store_true")
parser.add_argument("-o", "--occup",   help="print occupancy",                    action="store_true")
parser.add_argument("-b", "--beta",    help="print temperature (beta) factor",    action="store_true")
parser.add_argument("-e", "--element", help="print element symbol",               action="store_true")
parser.add_argument("-q", "--charge",  help="print charge on the atom",           action="store_true")
# parser.add_argument("-f", "--file", help="additional optional input file", type=argparse.FileType('r'))

## CONFLICTING OPTIONS
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")

## parse the arguments in a namespace
args = parser.parse_args()
## the arguments can now be accessed with args.arg1, args.arg2, etc.
## By default, each variable as 'None' value:
# if args.verbose:
#     print "verbosity turned on"

## print all input arguments and options
# print args

## To allow for an interactive shell (prompt), comment this line: 
if args.infile.isatty() : sys.exit()


## MAIN PROGRAM starts here


f = args.infile


## if there are no selection, the whole line will be printed
flag = False
if args.serial 	or args.name 	or args.altLoc 	or args.resName or \
   args.chain 	or args.resSeq 	or args.iCode 	or args.xyz 	or \
   args.x 	or args.y 	or args.z 	or args.occup   or \
   args.beta   	or args.element or args.charge  or args.parse	: flag = True 



## if verbose, print first a comment with column content
if args.verbose and not flag :
    print "#         s  n  l  r c  i d      x       y       z      o     b              e q"
if args.verbose and flag :
    if args.parse : sys.stdout.write( "#    " )
    else :          sys.stdout.write( "#" ) 
    if args.serial  or args.parse : sys.stdout.write( "    s "    )
    if args.name    or args.parse : sys.stdout.write( " n   "     ) 
    if args.altLoc  or args.parse : sys.stdout.write( "l "        )
    if args.resName or args.parse : sys.stdout.write( " r  "      )
    if args.chain   or args.parse : sys.stdout.write( "c "        )
    if args.resSeq  or args.parse : sys.stdout.write( "   i "     )
    if args.iCode   or args.parse : sys.stdout.write( "d "        )
    if args.xyz	                  : sys.stdout.write( "   x       y       z     ")
    if args.x	    or args.parse : sys.stdout.write( "   x     " )
    if args.y       or args.parse : sys.stdout.write( "   y     " )
    if args.z	    or args.parse : sys.stdout.write( "   z     " )
    if args.occup   or args.parse : sys.stdout.write( "  o    "   )
    if args.beta    or args.parse : sys.stdout.write( "  b    "   )
    if args.element or args.parse : sys.stdout.write( " e "       )
    if args.charge  or args.parse : sys.stdout.write( " q "       ) 
    print


## print selected columns
for line in f :
    if not line[:6] == "ATOM  " :
        continue 
    if args.cAlpha and not line[12:16].strip() == "CA" :
        continue
    if not flag :
        sys.stdout.write( line )
        continue
    if args.parse : sys.stdout.write( "ATOM " )
    else :          sys.stdout.write( " " ) 
    if args.serial  or args.parse : sys.stdout.write( line[6 :11]+" " )
    if args.name    or args.parse : sys.stdout.write( line[12:16]+" " ) 
    if args.altLoc  or args.parse : sys.stdout.write( line[16:17]+" " )
    if args.resName or args.parse : sys.stdout.write( line[17:20]+" " )
    if args.chain   or args.parse : sys.stdout.write( line[21:22]+" " )
    if args.resSeq  or args.parse : sys.stdout.write( line[22:26]+" " )
    if args.iCode   or args.parse : sys.stdout.write( line[26:27]+" " )
    if args.xyz	                  : sys.stdout.write( line[30:54]+" " )
    if args.x	    or args.parse : sys.stdout.write( line[30:38]+" " )
    if args.y       or args.parse : sys.stdout.write( line[38:46]+" " )
    if args.z	    or args.parse : sys.stdout.write( line[46:54]+" " )
    if args.occup   or args.parse : sys.stdout.write( line[54:60]+" " )
    if args.beta    or args.parse : sys.stdout.write( line[60:66]+" " )
    if args.element or args.parse : sys.stdout.write( line[76:78]+" " )
    if args.charge  or args.parse : sys.stdout.write( line[78:80]+" " ) 
    print

 
f.close()

