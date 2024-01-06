letter = "my name is {} and i am from {}"
name = "dhruv"
coun = "india"
print(letter.format(name,coun))
print(f"my name is {name} from {coun}")
print(f"my name is {{name}} from {{coun}}")  # just see output

txt = "for only {price:.2f} dollers"
print(txt.format(price = 123.2345))

price = 123.34567
txt = f"for only {price:.2f} dollers"
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

