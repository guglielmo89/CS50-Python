import re

email = input("Email: ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

### REGEX NOTATION ###
#    .       any character except a newline
#    *       0 or more repetition
#    +       1 or more repetition
#    ?       0 or 1 repetition
#    {m}     m repetitions
#    {m,n}   m-n repetitions

#    ^       matches the start of the string
#    $       matches the end of the string or before the newline

#    []      set of characters
#    [^]     complementing the set

#    \w      alpha numeric value (letters, numbers, underscore)
#    \d      decimal value
#    \s      blankspace value

#    (...)   a group of values - A | B (A or B) - captured
#    (?:...) a group of values, not captured
