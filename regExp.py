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

print float_pattern.match("2.56")

print float_pattern.match("2.560")

print float_pattern.match("4")