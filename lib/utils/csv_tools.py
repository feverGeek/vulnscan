import csv


def csv_generate(filename, header, data):
    with open(filename, "w+") as fd:
        writer = csv.writer(fd)
        writer.writerow(header)
        writer.writerows(data)