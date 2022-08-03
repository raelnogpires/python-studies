# exercise 2
# read an expression, and based in the table below,
# find the correspondent phone number.
# ABC     ->  2
# DEF     ->  3
# GHI     ->  4
# JKL     ->  5
# MNO     ->  6
# PQRS    ->  7
# TUV     ->  8
# WXYZ    ->  9


def get_number_by_character(char):
    if ["A", "B", "C"].count(char.upper()) > 0:
        return '2'
    elif ["D", "E", "F"].count(char.upper()) > 0:
        return '3'
    elif ["G", "H", "I"].count(char.upper()) > 0:
        return '4'
    elif ["J", "K", "L"].count(char.upper()) > 0:
        return '5'
    elif ["M", "N", "O"].count(char.upper()) > 0:
        return '6'
    elif ["P", "Q", "R", "S"].count(char.upper()) > 0:
        return '7'
    elif ["T", "U", "V"].count(char.upper()) > 0:
        return '8'
    elif ["W", "X", "Y", "Z"].count(char.upper()) > 0:
        return '9'
    else:
        return char


def find_phone_number_by_phrase(phrase):
    phone_number = ''
    for char in phrase:
        decode = get_number_by_character(char)
        phone_number += decode

    return phone_number
