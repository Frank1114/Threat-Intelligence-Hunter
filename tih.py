__author__ = '@abhinavbom a.k.a Darkl0rd'

#local imports
from bin.parse import *
from bin.md5vt import *

#stdlib imports
import argparse

banner = ''' Threat Intelligence Hunter framework Begins now '''

print banner

def main():
    print "Intel test"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-ip', type=str, nargs='+', help="Search for a single IP through OSINT threat feeds")
    parser.add_argument('-list', type=str, nargs='?', help="Search for a list of IP vectors. Accepted formats is .txt")
    parser.add_argument('-md5', type=str, nargs='?', help="Search for a single of space separated multiple MD5s. This search is performed on Virustotal. Please add your public key to bin/vt.py")
    args = parser.parse_args()
    if args.ip:
        parse_ip(args.ip)
        vt_ip(args.ip)
    if args.list:
        parse_ipList(list)
    if args.md5:
        vt_md5(args.md5)


if __name__ == '__main__':
    main()
