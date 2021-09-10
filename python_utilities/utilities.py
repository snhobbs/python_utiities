def RegistersToBytes(registers):
  text = []
  for register in registers:
      text.append((register>>8)&0xff)
      text.append((register&0xff))
  return bytes(text)

def TransformBytesToDataType(dtype, data : bytes, byteorder="big"):
    if dtype == "string":
        if isinstance(data, bytes):
            return data.decode("utf-8")
        return "".join([chr(pt) for pt in data])

    signed = dtype[0] != "u"
    return int.from_bytes(data, byteorder=byteorder, signed=signed)

def bytes_to_int32(data, byteorder="big", endianness=None):
    return TransformBytesToDataType("int32", data, byteorder)

