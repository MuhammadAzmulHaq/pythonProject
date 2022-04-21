def py(a):
    for i in range(0, a):
        for j in range(0, 1 + i):
            print("*", end="")
        print("\r")


a = 2
py(a)

print("**********************************")


def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 5
print("Factorial of", num, "is", factorial(num))
print("**********************************")

num = 11
# If given number is greater than 1
if num > 0:

    # Iterate from 2 to n / 2
    for i in range(2, int(num / 2) + 1):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

