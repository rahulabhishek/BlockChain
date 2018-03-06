def median(x,y,z):
    s = (x, y, z)
    c = list(s)
    median_value = sum(c)/len(c)
    v = round(median_value)
    return v

#print(median(1,2,2))


def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(x, y, z):
    big = biggest(x,y,z)
    if big == x:
        return bigger(y,z)
    if big == y:
        return bigger(x,z)
    else:
        return bigger(x,y)




print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7