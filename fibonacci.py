#   Gregory Gilbert
#   8/9/2025
#   Practice with Fibonacci

def fibonacci(fibi):
    if fibi < 2:
        return fibi
    else:
        return fibonacci(fibi - 1) + fibonacci(fibi - 2)

def fibonacci_custom(first, second, length):
    hold = 0
    print(first, second)
    for i in range(1, length-2):
        first, second = second, first + second
        print(second)


if __name__ == '__main__':
    fibi = 1
    while fibi != 0:
        fibi = int(input('What number of fibonacci do you want? '))
        print("Fibonacci number " + str(fibi) + " is:", fibonacci(fibi))

    print("What numbers to start with?")
    first = int(input("First number: "))
    second = int(input("Second number: "))
    length = int(input("What length of sequence do you want: "))
    fibonacci_custom(first, second, length)

