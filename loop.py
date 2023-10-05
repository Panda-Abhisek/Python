""" # for x in "banana":
#     print(x)
n = int(input("Enter n: "))
for x in range(n):
    if x == 10:
        continue        #skipping 10
    if x == 15:
        break           #breaking the code after 15   
    print(x)

"""
"""
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

ExampleGet your own Python Server
Print i as long as i is less than 6:
"""

i = 0
while i < 6:
  i += 1
  if i == 4:
    continue
  print(i)