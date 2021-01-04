import os
from collections.abc import Iterable

def prt(title, str):
    terminal_width = os.get_terminal_size().columns
    title_length = len(title)
    side_width = int((terminal_width - title_length) / 2)
    print("-" * side_width + title + "-" * side_width)
    print(str)
    print()


def format_prt(data):
    try:
        for d in data:
            for k,v in d.items():
                print(k,v)
    except:
        pass

def result_prt(data):
    try:
        for items in data:
            if isinstance(items, Iterable):
                for d in items:
                    for k,v in d.items():
                        print(k,v)
            else:
                print(items)
    except Exception as e:
        print(e)
