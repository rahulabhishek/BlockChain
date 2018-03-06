def is_friend(name):
    if name[0]=='D' or name[0]=='N':
        return True
    else:
        return False

print (is_friend('Diane'))
#>>> True

print (is_friend('Ned'))
#>>> True

print (is_friend('Moe'))
#>>> False