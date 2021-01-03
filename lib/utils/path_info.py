import os

def get_path_info(path):
    pathinfo = os.path.split(path)
    tail = pathinfo[1]
    pathinfo = os.path.split(pathinfo[0])
    vuln = pathinfo[1]
    return vuln + "/" + tail