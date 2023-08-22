"""
Prints every number from 1 to 100
For every number divisible by 3, prints 🥕 instead
For every number divisible by 5, prints 🥔 instead
For every number divisible by 7, prints 🍎 instead
If divisible by multiple, prints multiple (🥕🥔🍎)
If divisible by none, prints the number itself
"""
for i in range(1,101):
    out = ""

    if (i % 3 == 0):
        out += "🥕"
    if (i % 5 == 0):
        out += "🥔"
    if (i % 7 == 0):
        out += "🍎"

    print(out or i)
    # Takes O(n) time