# key : value
# dictionaries are order in leatest version not like acesnding or decending
dic = {
    "name" : "dhruv",
    "surname" : "dankhara",
    616 : "my rno",
    123 : "random number"
}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic["name"])  # if key present throw error
print(dic.get("name")) # if key not present throw error but say none

for key in dic.keys():
    print(dic[key])

for key,value in dic.items():
    print(key,':',value)



