#summation
score= [88,89,90,100,77,56,24,66,78,23]
summation = sum(score)
print(summation)

#another way
SUM = 0
for score1 in score:
    SUM += score1

print(SUM)

#max function
print(max(score))

#find maximum using for loop

Max = 0
for sc in score:
   if  sc > Max:
    Max = sc
   

print(Max)

#range function
total = 0
for number in range(1,101):        #range 1 to 100 but 3 by 3
   total += number

print(total)   
  