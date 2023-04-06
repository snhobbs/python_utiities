def ReadKeyValueDataFile(string, header_char='#', delim = ':'):
    '''
    Breakup lines into key value pairs
    Any value not in a key value pair and has none white space characters is added to a list
    '''
    lines = string.split("\n")
    key_value = list()
    data = list()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue # skip line
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
    '''
    HP Data file is a new line delimited list.
    Header:
        ```
        NPoints-1
        Step Size
        ??
        ```
    returns: x, y array
    FIXME this is actually mathcad format
    '''
    import numpy as np
    npoints, step_size, _ = data[:3]
    npoints = int(npoints)
    step_size = float(step_size)
    y = np.array(data[3:], dtype=float)
    assert len(y) == npoints+1
    return [pt*step_size for pt in range(len(y))], y



def read_hp_spreadsheet(fname):
    '''
    reads spreadsheet output from HP scopes with preamble.
    Generate these using the WFMCONVERT function.
    '''
    import pandas
    from io import StringIO
    with open(fname, 'r') as f:
        text = f.read().split(";")
        header_line, data_text = text[:-1], text[-1]
        header_array = [pt.split(' ', 1) for pt in header_line]
    header = dict(header_array)
    for key, value in header.items():
        header[key] = value.strip('"')
    data = pandas.read_csv(StringIO(data_text), names=["x", "y"])
    data[header["YUNIT"]] = data['y']*float(header["YMULT"]) + float(header["YOFF"])
    data[header["XUNIT"]] = data['x']
    return header, data
