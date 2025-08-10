#   Gregory Gilbert
#   8/9/2025
#   Practice with Fibonacci

def fibonacci(fibi):
    if fibi < 2:
        return fibi
    else:
        return fibonacci(fibi - 1) + fibonacci(fibi - 2)

if __name__ == '__main__':
    fibi = 1
    while fibi != 0:
        fibi = int(input('What number of fibonacci do you want? '))
        print("Fibonacci number " + str(fibi) + " is:", fibonacci(fibi))
