def biggest (x,y,z):
    if x >= y + z:
        return x
    if y>z:
        return y
    else:
        return z
print(biggest(11,12,5))

'''
if y>z and x>y:
        return x
    if y<z and x>z:
        return x
    if y>z and y>x:
        return y
    if y<z and x<y:
        return z
    if y>z and x<z:
        return y
    if z>x and x>y:
        return z
    else:
        return x 
    '''
