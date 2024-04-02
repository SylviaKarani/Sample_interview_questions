#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
from contextlib import suppress
from sys import stdin
from typing import Dict, List, Tuple


if __name__ == '__main__':
    StatusCodes = Dict[int, int]
    FileSize = List[int]

    def _print_stats(file_size: FileSize, status_codes: StatusCodes) -> None:
        """Private method to print stats."""
        print('File size: {}'.format(file_size[0]))
        for key, val in status_codes.items():
            if val != 0:
                print('{}: {}'.format(key, val))

    def _parse_line(
        line: str,
        status_codes: StatusCodes,
        file_size: FileSize
            ) -> Tuple[StatusCodes, FileSize]:
        """A private method to parse lines."""
        with suppress(BaseException):
            line = line[:-1]
            word = line.split(' ')
            file_size[0] += int(word[-1])
            status_code = int(word[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        return status_codes, file_size

    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_number = 1
    try:
        for line in stdin:
            status_codes, file_size = _parse_line(
                line, status_codes, file_size
                )
            if line_number % 10 == 0:
                _print_stats(file_size, status_codes)
            line_number += 1
    except KeyboardInterrupt:
        _print_stats(file_size, status_codes)
        raise
    _print_stats(file_size, status_codes)
