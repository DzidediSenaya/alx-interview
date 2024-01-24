#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(file_size, status_codes):
    """Prints the file size and status code statistics."""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, status_codes):
    """Parses a log line and extracts status code and file size."""
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            return status_code, file_size
    except ValueError:
        pass
    return None, None


def main():
    """Main function to read log lines and calculate statistics."""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line, status_codes)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_codes[status_code] = (
                    status_codes.get(status_code, 0) + 1
                )

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
