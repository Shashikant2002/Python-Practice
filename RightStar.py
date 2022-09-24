
# for i in range(6):
#     print('*' * (i+1))

n = 5

for i in range(3):  
    print("0" * (n - i - 1), end="1")
    print("*" * (2 * i + 1), end="2")
    print("0" * (n - i - 1))
