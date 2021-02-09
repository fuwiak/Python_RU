# if-else-elif 


#1 
a,b,c = 1,2,1

delta=b**2 -4*a*c

if delta>0:
  print("2 solustions")
elif delta == 0:
  print("1 solution")
else:
  print("no solution")
  
#2

number=9

if number>=0:
  print("postive of zero")
else:
  print("negative")
  
# listy

lista = [1,2,3,-1,2]

print(lista[0]) # first element 
print(lista[-1]) # last element 
print(lista[-2]) # second last
lista[::-1] # inversed order
lista[::2 ] # every second element 
lista[1::2] # start from index=1, then every second element.

lista[2:6] # slice from index=2 to index=6



A = [[1,2,3], [4,5,6], [7,8,9]]
A[0] # first row
A[0][0] # first element of the first row
