# def cat_voice ():
#    print('meow!')
# cat_voice()
#
# def dog_voice ():
#     print('woof!')
# dog_voice()
#
# #Вывод голосов N раз
#
# def cat_voice ():
#     return ('meow!')
# for x in range(2):
#     print(cat_voice())
#
# def dog_voice ():
#     return ('woof!')
# for x in range(2):
#     print(dog_voice())


x = input('Введите текст')

def get_voice(x):
    if '!' in x:
        return x
    else:
        return False

print (get_voice(x))
