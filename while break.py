j = 0
for i in range(5):
    j = j + 2
    print('i = ', i, ', j = ', j)
    if j == 6:
        break
try:
    answer = 12/0
    print(answer)
except:
    print("an error occured")
