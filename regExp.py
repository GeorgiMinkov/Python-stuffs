# encoding: utf - 8
# парсване и валидация

# r '^0 | [1-9][0-9]*$'

import re

int_pattern = re.compile(r'^(0|[1-9][0-9]*){, 3}$')

print int_pattern.match("123")

print int_pattern.match("q27")

print int_pattern.match("27p")

print int_pattern.match("q27p")

print int_pattern.match("3.1415")



float_pattern = re.compile(r'^(0|[1-9][0-9]*(\.[0-9]*[1-9])?)$')

float_pattern = re.compile(r'^(0|[1-9][0-9]*(\.[0-9]+)?)$')
print float_pattern.match("2.56")

print float_pattern.match("2.560")

print float_pattern.match("4")

# MAC ADDRESS XX:XX:XX:XX:XX:XX
# X e [0-9 A-F] (направи го и за [a-f]) 
# {number} - точно толкова символа
# {, n} - до n символа
# {n, } - над n симовла
mac_pattern = re.compile(r'^([0-9A-F][0-9A-F]:){5}([0-9A-F][0-9A-F])$')

print mac_pattern.match("00:00:00:00:00:00")

m = int_pattern.match("eza")
help(m)