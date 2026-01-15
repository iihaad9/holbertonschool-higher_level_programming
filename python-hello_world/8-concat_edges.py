#!/usr/bin/python3
import sys
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str[39:67] + str[106:112] + str[:6]
sys.stdout.write(str)
