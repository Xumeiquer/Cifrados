#!/usr/bin/env python
# -*- coding: utf8 -*-

from cesar import cesar, u_cesar

try:
    cesar("test", "1")
except(TypeError):
    print("Error esperado")

try:
    u_cesar("test", "1")
except(TypeError):
    print("Error esperado")

print cesar("test", 1)
print u_cesar(cesar("test", 1), 1)

