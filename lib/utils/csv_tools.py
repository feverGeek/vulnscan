import csv

header = ['ID', '网站地址', '漏洞']

def csv_generate(filename, data):
    with open(filename, 'w+') as fd:
        writer = csv.writer(fd)
        writer.writerow(header)
        writer.writerows(data)