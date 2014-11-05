from animals import Animals
from zoo import Zoo
from json_adder import Animal_Add
import json


def printer1():  # Printva, nekvi na4alni gluposti :D
    print("\n\n\nThis is a simulator of Zoo!")
    print("And its not perfect so one month is aways 30 days")
    print("and one year is aways %s days\n" % (30*12))
    print("Lets start making the Zoo:")


def zoo_init():  # Inicializira zoo
    print("First we will need the capacity of the zoo.")
    print("How many animals(max) you want your Zoo to get?")
    capacity = raw_input()
    print("Now we need some monny for the start. How much starting monny you want?")
    budget = raw_input()
    return Zoo(capacity, budget)


def main():
    #month = 30 * day
    #year = month * 12
    printer1()
    my_zoo = zoo_init()

if __name__ == '__main__':
    main()
