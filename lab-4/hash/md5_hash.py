def left_rotate(value,shift):
    return ((value<<shift)|(value>>(32-shift)))& 0xFFFFFFFF
def md5(message):
    a=0x