# ## Loops
# for loops: used to iterate over sequence of numbers
# range(5)  it display numbers from 0 to 5

range(4)
for i in range(5):
    print(i)
range(1,10,1) # the third para is step size. 
for i in range(1,10,2):
    print(i)
for i in range(10,1,-1):
    print(i)
# Traversing string

str_ = "Anas Khan"

for i in str_:
    print(i)
# while loop: continues to execute as long as the condition is True.

count = 0
while count<5:
    print(count)
    count = count + 1
# Loop control statements 
# break: exits the loop prematurely.

for i in range(5):
    if i == 5:
        break
    print(i)
# continue: skips the current iteration and continues with the next.

for i in range(10):
    if i %2==0:
        continue
    print(i)
# pass: a null operation; it does nothing

for i in range(5):
    if i == 3:
        pass
    print(i)
# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")
        
# Calculate the sum of first N natural numbers using a while and for loop

# while loop

n = 10
sum = 0
count = 1

while count <= n:
    sum = sum + count
    count = count+1
print('sum of first 10 natural num is:', sum)
# Using for loop
n = 10
sum = 0

for i in range(11):
    sum = sum + i
print("Sum of first 10 natural num is:", sum)
# Prime num: which is divisiblle by 1 or the number itself. 

for num in range(1,101):
    if num > 1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
num = int(input("enter the number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime numbe.")
