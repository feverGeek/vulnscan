import os


def prt(title, str):
    terminal_width = os.get_terminal_size().columns
    title_length = len(title)
    side_width = int((terminal_width - title_length) / 2)
    print("-" * side_width + title + "-" * side_width)
    print(str)
    print()
