#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(number) -> float:

    return math.sqrt(number)


def square(number) -> float:
    return math.pow(number, 2)


def average(number1, number2, number3) -> float:
    return sum([number1,number2,number3])/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs+(angle_mins+(angle_secs/60))/60)


def to_degrees(angle_rads) -> float:
    angle_deg = math.degrees(angle_rads)
    minutes = (angle_deg - math.floor(angle_deg))*60
    secondes = (minutes - math.floor(minutes))*60
    return math.floor(angle_deg), math.floor(minutes), math.floor(secondes)


def to_celsius(temperature: float) -> float:
    return (temperature - 32)/1.8


def to_farenheit(temperature: float) -> float:
    return (temperature + 32)/1.8


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
