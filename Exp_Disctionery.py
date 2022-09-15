myDict = {
    "First": "In a Quick Manner",
    "Shashikant": "A Coader",
    "Marks": [1,2,3,5],
    "another": {'Shashikant': "Coader"}
}

myDict_1 = {
    'new': "Shashikant",
    'hello': "I AM Shashikant"
}
myDict.update(myDict_1)


print(myDict.get("ne")) #throw a None if key is not present in object
# print(myDict["ne"]) #throw a error if key is not present in object
# print(myDict)
# print(myDict)
# print(myDict["First"])
# print(myDict["Shashikant"])
# print(myDict["Marks"])
# print(myDict['another']['Shashikant'])
# print(myDict.values())
