# In the US, the elevators start from Floor 1 while the EU's start from 0, this code will convert the EU floor to the US format.
inp = input('Europe floor? ')
usf = int(inp) + 1
print('US floor ', usf)