# strign is immutable so, we can`t chnage it we only make copy of string
name = 'Dhruv dankhara'

# upper() & lower() = this create new string don`t make changes in old one
# print(name.upper())
# print(name.lower())

# rstrip() = remove trailing character from string 
name1 = '!!dhruv!!!!!!'
# print(name1) # ir remove from last , but 
# print(name1.rstrip("!"))  # it not remove from start

# replace() = it replace all who match
# print(name.replace("Dh","o"))

# split() = it sperete string from given word/space and return list 
# print(name.split(" ")) # ['Dhruv', 'Dankhara']

# capitalize() = convert first character of string in UpperCase ohrt convert to lowerCase.
# str = "heLlo, i aM dhRuv"
# print(str.capitalize())

# center() : it center the string
# print(len(name))
# print(name.center(28))

# count() : count character
# print(name.count("da"))

# endswith() : check string end with given character. true / false.
# print(name1.endswith("!!"))
# we can even also check for a value in-between the string by providing start and end position.
# first slice the string with giving postion and check end character.
# print(name1.endswith("to", 4, 10))

# find() : find the given value and return index if value not find then return -1
# print(name.find("kh"))

# index() : this is similer to find() but if value don`t exit then this throw error
# print(name.index("khu"))

# isalnum() : it return true if all element is A-Z a-z and 0-9 otherwise return false and space also throw false.
# print(name.isalnum())

# isalpha() : A-Z a-z
# print(name.isalpha())

# islower() : 
# print(name1.islower())

# isnumeric() : 0-9
# print(name.isnumeric())

# isprintable : \n = false
# print(name.isprintable())

# isspace() : return true is string contians All white spaces
# print(name.isspace())

# istitle() : if all first character of Word is upperCase return true
# print(name.istitle())

# isupper() : similer to islower()

# startswith() : similer to endswirh()

#swapcase() : convert uppercase to lowercase and lower to upper
# print(name.swapcase())

# title() : change to upperCase all charcter for all words first letter
# print(name.title())




