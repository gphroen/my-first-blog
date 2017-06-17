#if 2 > 5:
#    print("Bla")
#elif 2 < 5:
#    print("True")
#else:
#    print("Not True")
def hi():
    print("My fist function")
    print("The second command of my first function")

hi()
def hi(name):
    if name == 'Ola':
        print('Hi Ola')
    elif name == 'Anna':
        print('Hi Anna')
    else:
        print('Hi anonym')

hi('Ella')


def hi(name):
    print('Hi '+name+'!')
hi('Ale')

girls=['Anna','Ella','Ola']

for name in girls:
    hi(name)
    print('aaaaaand')

for i in range(0,5):
    print(i)
    
