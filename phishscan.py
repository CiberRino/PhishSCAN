import argparse
from analyzer import analyzer

def main():
    parser = argparse.ArgumentParser(description="Tool for analizer url suspicious (educative)")
    parser.add_argument("url",help="Your url suspicious")
    parser.add_argument("-H",help="look HTML of the page",action="store_true")
    parser.add_argument("-ss",help="validate ssl certificate",action="store_true")

    args = parser.parse_args()

    analyzer(args.url,args.H,args.ss)


main()