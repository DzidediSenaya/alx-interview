#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(file_size, status_codes):
    """Prints the file size and status code statistics."""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, status_codes):
    """Parses a log line and extracts status code and file size."""
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            return status_code, file_size
    except (ValueError, IndexError):
        pass
    return None, None


def main():
    """Main function to read log lines and calculate statistics."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line, status_codes)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_codes[status_code] += 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
