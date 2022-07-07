import datetime
import os


def make_time_from_file_timestamp(file_string: str):
    if not isinstance(file_string, str):
        file_string = ""
    split = file_string.split("_")
    isoformat = ".".join(split[-2:])
    try:
        time = datetime.datetime.fromisoformat(isoformat)
    except ValueError:
        time = datetime.datetime.fromtimestamp(0)
    return time


def make_file_timestamp(now=None):
    if now is None:
        now = datetime.datetime.now()
    return now.isoformat().replace(".", "_")


def list_subdirectories(dir_name):
    subs = []
    for name in os.listdir(dir_name):
        dname = os.path.join(dir_name, name)
        if os.path.isdir(dname):
            subs.append(dname)
    return subs
