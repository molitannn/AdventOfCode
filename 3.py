i = 0
paper = 0
fh = open("meas.txt.", "r")
objj = fh.read()
obj = objj.split('\n')
for line in obj:
    meas = obj[i].split('x')
    l = int(meas[0])
    w = int(meas[1])
    h = int(meas[2])
    sides = [l*w,w*h,h*l]
    slack = int(min(sides))
    paper += 2*(l*w+w*h+h*l) + slack
    i += 1
print (paper)
