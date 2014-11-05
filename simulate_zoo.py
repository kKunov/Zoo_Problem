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
    capacity = int(input())
    print("Now we need some monny for the start. How much starting monny you want?")
    budget = int(input())
    return Zoo(capacity, budget)


def interval_to_days():
    print("Enter the interval of time:")
    interval_of_time = input()
    print("Enter the period:")
    period = int(input())
    period_of_days = 0
    if interval_of_time == "days":
        period_of_days = period
    elif interval_of_time == "months":
        period_of_days = period * 30
    elif interval_of_time == "weeks":
        period_of_days = period * 7
    elif interval_of_time == "years":
        period_of_days = period * 360
    else:
        print("Invalid interval of time!")
        interval_to_days()
    return period_of_days


def growing_of_animals(zoo, days):
    months_to_grow = days / 30
    for animal in zoo.see_animals():
        if months_to_grow > 0:
            for i in range(1, months_to_grow):
                animal.grow()


def starter_pack_animals_for_new_zoo(zoo):
    pesho_tiger = Animals("Pesho", "tiger", "male", 3)
    ivo_panda = Animals("Ivo", "panda", "male", 5)
    gosho_lion = Animals("Gosho", "lion", "male", 4)
    penka_tiger = Animals("Penka", "tiger", "female", 2)
    ani_panda = Animals("Ani", "panda", "female", 4)
    desi_lion = Animals("Desi", "lion", "female", 3)
    zoo.accomodate(pesho_tiger)
    zoo.accomodate(ivo_panda)
    zoo.accomodate(gosho_lion)
    zoo.accomodate(penka_tiger)
    zoo.accomodate(ani_panda)
    zoo.accomodate(desi_lion)


def main():
    #month = 30 * day
    #year = month * 12
    printer1()
    #initializing zoo
    my_zoo = zoo_init()
    #converting user input of period to days
    days_to_simulate = interval_to_days()
    growing_of_animals(my_zoo, days_to_simulate)
    #adding initial animals to the zoo
    starter_pack_animals_for_new_zoo(my_zoo)


if __name__ == '__main__':
    main()
