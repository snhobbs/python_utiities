def ReadKeyValueDataFile(string, header_char="#", delim=":") -> tuple:
    """
    Breakup lines into key value pairs
    Any value not in a key value pair and has none white space characters is added to a list
    :param Iterable string: Contents iterable by lines
    :param str header_char: Eyecatcher character for header lines.
    :param str delim: Separator between key and value in header
    :returns list key_value: list of key value tuples
    :returns list data: list of all lines not starting with the header_char as strings
    """
    lines = string.split("\n")
    key_value = list()
    data = list()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue  # skip line
        if line[0] == header_char:
            split = line.split(delim)
            key_sections = [pt.strip().lstrip(header_char).strip() for pt in split[:-1]]
            key = delim.join(key_sections)
            value = delim.join([pt.strip() for pt in split[-1:]])
            key_value.append((key, value))
        else:
            data.append(line)
    return key_value, data


def ReadHpFileFormat(data):
    """
    HP Data file is a new line delimited list.
    Header:
        ```
        NPoints-1
        Step Size
        ??
        ```
    returns: x, y array
    FIXME this is actually mathcad format
    """
    import numpy as np

    npoints, step_size, _ = data[:3]
    npoints = int(npoints)
    step_size = float(step_size)
    y = np.array(data[3:], dtype=float)
    assert len(y) == npoints + 1
    return [pt * step_size for pt in range(len(y))], y


def read_hp_spreadsheet(fname):
    """
    reads spreadsheet output from HP scopes with preamble.
    Generate these using the WFMCONVERT function.
    :params fname: file name
    :returns header, data
    """
    import pandas
    from io import StringIO

    with open(fname, "r") as f:
        text = f.read().lstrip().split(";")
        header_line, data_text = text[:-1], text[-1]
        header_array = [pt.split(" ", 1) for pt in header_line]
    header = dict(header_array)
    for key, value in header.items():
        header[key] = value.strip('"')
    data = pandas.read_csv(StringIO(data_text), names=["x", "y"])
    data[header["YUNIT"]] = data[
        "y"
    ]  # (data['y'] + float(header["YOFF"]))*float(header["YMULT"])
    data[header["XUNIT"]] = data["x"]
    return header, data


def generate_hp_header_string(header: dict) -> str:
    """
    generates hp format header from map
    """
    header_array = []
    for key, value in header.items():
        header_array.append(" ".join([key, value]))
    return ";".join(header_array)


def write_hp_spreadsheet(header, data, fname):
    import pandas
    from io import StringIO

    with open(fname, "w") as f:
        f.write(";".join())
        text = f.read().lstrip().split(";")
        header_line, data_text = text[:-1], text[-1]
        header_array = [pt.split(" ", 1) for pt in header_line]
    header = dict(header_array)
    for key, value in header.items():
        header[key] = value.strip('"')
    data = pandas.read_csv(StringIO(data_text), names=["x", "y"])
    data[header["YUNIT"]] = data[
        "y"
    ]  # (data['y'] + float(header["YOFF"]))*float(header["YMULT"])
    data[header["XUNIT"]] = data["x"]
    return header, data


def read_hp_asc(fname):
    import numpy as np

    delim = ";"
    with open(fname, "r") as f:
        sections = f.read().strip().split(delim)
    header = dict()
    for section in sections:
        key, value = section.split(" ", maxsplit=1)
        header[key] = value
    byte_data = np.array(header[":CURVE"].split(","), dtype=int)
    data = []
    for i in range(len(byte_data) // 2):
        data.append(int.from_bytes(data[2 * i : 2 * i + 2], byteorder="big"))
    return header, data
