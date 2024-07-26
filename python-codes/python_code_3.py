# Qn 24
import math

def compute_hypothenuse(length, breath):
    hyp_squared = (length ** 2) + (breath ** 2)
    hyp = math.sqrt(hyp_squared)
    return hyp


x = compute_hypothenuse(3, 4)
print(x)

# Qn 30
def addition(N):
    for numbers in range(1, N + 1):
        sum = numbers + numbers
        print(f"{numbers} + {numbers} = {sum}")

addition(10)

# Qn 31 
def multiple(N):
    for nos in range(1, N + 1):           # for loop
        product = nos * nos
        print(f"{nos} x {nos} = {product}")

multiple(10)

# Qn 32 
def numbers(N):                 
    result = " - ".join((str(nos)) for nos in range(1, 1 + N))  # for loop
    print(result)

numbers(10)
"""
def nums(N):
    i = 1
    while i < (N + 1):
        print(i 
        if i == 10:
            break
"""

# Qn 32 
def nums(N):
    result = " : ".join((str(nums)) for nums in range(1, 1 + N))
    print(result)

nums(10)

# Qn 33
def nums():
    numbers = [12, 14, 16, 18, 20]
    result = ", ".join((str(nums)) for nums in numbers)
    print(result, end=".")

nums()

def nums(N):
    numbers = []
    
    for num in range(12, N + 1, 2):
        numbers.append(str(num))
        if num == N:
            break

    result = ", ".join(numbers)
    print(result, end=".")

nums(20)

# Qn 33
def nums(N):
    numbers = []

    for num in range(1, int((N - 1) / 0.2) + 1):
        i = round(1.0 + (num * 0.2), 2)
        numbers.append(str(i))
        if i >= N:
            break

    result = " * ".join(numbers)
    print(result, end=".")

nums(4.0)

# Qn 33
def nums(N):
    nos = []

    for i in range(1, N + 1, 2):
        nos.append(str(i))
        if i == N:
            break

    result = "; ".join(nos)
    print(result, end=".")

nums(9)

# Qn 34
def num_list(N):
    for num in range(N + 1):    # For loop repeats number from 0 to N (loop variable is num)
            result = "".join(str(num) for num in range(0, num + 1, 2)) 
            # Inner For Loop and Join: Within the outer loop, it defines a string by joining the
            # string representation of even numbers from 0 to the current value of 'num' 
            # using "" (empty string) as the separator 
            print(result)

num_list(20)

# 35 