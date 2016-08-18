myList = [1,2,3,4,5, "hello"]

print(myList)
print(myList[2])
print(myList[-1])

myList2 = myList[1:5]
print(myList2)

myList[1] = 20
print(myList)

myList.append("How are you?")
print(myList)

del myList[5]
print(myList)

myDict = {"One": 1.35, 2.5:"Two Point Five", 3:"+", 7.9: 2}
print(myDict)