#!/usr/bin/env python3.6


import argparse
import sys
import moogle


def main():

    parser = argparse.ArgumentParser(
        description="Crawler module for the µoogle project",
        epilog=moogle.authors(),
    )

    parser.add_argument("-u", "--url", type=str, help="starting url", default=5)
    parser.add_argument("-m", "--maxdist", type=int, help="maximum distance", default=5)
    parser.add_argument("-d", "--database", type=str, help="filename of the database", default="moogle.dat")

    args = parser.parse_args(sys.argv[1:])

    db = moogle.crawler(args.url, args.maxdist)
    moogle.store(db, args.database)


if __name__ == "__main__":
    main()
