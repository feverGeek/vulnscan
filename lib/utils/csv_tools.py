import csv
from collections.abc import Iterable


def csv_generate(filename, header, data):
    with open(filename, 'w+') as fd:
        writer = csv.writer(fd)
        writer.writerow(header)
        id = 1
        for item in data:
            if isinstance(item,Iterable):
                for d in item:
                    l = list(d.values())
                    l.insert(0, id)
                    writer.writerow(l)
                    id += 1
            else:
                pass