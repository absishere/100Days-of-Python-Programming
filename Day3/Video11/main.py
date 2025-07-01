import time
# a = 'qwertyuiopasdfghjklzxcvbnm'
# print(a[100::-1])

# b = '''I am
# Abbas
# Sangameshwari
# '''
# print(b[::-1])

name = 'Abbas Sangameshwari'

j = 1
while j:
    try:
        for i in range(len(name)):
            time.sleep(0.6)
            print(name[i])
            j = 0
    except IndexError as e:
        print(e)
        j = 0

print('While loop se bahar.')