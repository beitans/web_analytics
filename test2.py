from time import sleep
import random
import time

def multiply_by_2(x):
    print("Old Value: " + str(x))
    x=x*2
    print("New Value: " + str (x))
    return x

def random_delay(factor = 1):
    while factor >= 1:
        time.sleep(random.randint(1,3)/10)
        factor = factor - 1


def iterations(count, x_value):
    x=0
    while x < count:
        print("inside")
        x_value = multiply_by_2(x_value)
        random_delay()
        x=x+1


def main():
    print("Hello World!")
    print("outside 2")
    iterations(100,5)


if __name__ == "__main__":
    main()