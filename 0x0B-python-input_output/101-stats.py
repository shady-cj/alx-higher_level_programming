#!/usr/bin/python3
"""
This module prints stats from standard input
"""

import sys


def stats():
    stat_codes = (
            200,
            301,
            400,
            401,
            403,
            404,
            405,
            500
            )
    i = 0
    stats = {}
    file_size = 0
    for line in sys.stdin:
        if i == 10:
            print(f"File Size: {file_size}")
            for s in stat_codes:
                if stats.get(s) is not None:
                    print(f"{s}: {stats[s]}\n")
            stats = {}
            i = 0
            continue
        split = line.split()
        file_size += int(split[-1])
        code = int(split[-2])
        stats[code] = stats.get(code, 0) + 1
        i += 1


if __name__ == "__main__":
    stats()
