import hashlib
zero = "00000"
code = b"yzbqklnj"
for i in range (0,1000):
    m = hashlib.md5()
    m.update(code)
    ms = str(m.hexdigest())
    str(code)
    str(i)
    if (ms[0:4]==zero):
        break
    else:
        code = code + i
print(ms)
