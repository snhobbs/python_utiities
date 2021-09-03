def RegistersToBytes(registers):
  text = []
  for register in registers:
      text.append((register>>8)&0xff)
      text.append((register&0xff))
  return bytes(text)

def DecodeText(data: list):
    return RegistersToBytes(data).decode("utf-8")

def TransformBytesToDataType(dtype, data : bytes, byteorder="big"):
    if dtype == "string":
        dtype = "uint8"
        return data.decode("utf-8")
    signed = dtype[0]=="u"
    return int.from_bytes(data, byteorder=byteorder, signed=signed)

def bytes_to_int32(data, byteorder="big"):
    return TransformBytesToDataType("int32", data, byteorder)

