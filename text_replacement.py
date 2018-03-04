marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."
x = line.find(marker)
y = line[:x]
z = line[x+len(marker):]
replaced = y + replacement + z
print(replaced)



