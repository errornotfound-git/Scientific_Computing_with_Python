# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
ihr = int(input('Enter Hours: ')) # Input hours will be automatically transform into integer
irt = float(input('Enter Rate: ')) # Input rate will be automatically transform into float, if not > cannot calculate as input's default is str()
grp = round((ihr * irt),2) # Round the result to 2 decimal
print('Pay: ',grp) # print('Pay: ' + str(grp)) also works