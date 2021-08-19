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
# def dog_voice ():
# def dog_voice ():
#     return ('woof!')
#     return ('woof!')
# for x in range(2):
#     print(dog_voice())

#
# x = input('Введите текст')
#
# def get_voice(x):
#     if '!' in x:
#         return x
#     else:
#         return False
#
# print (get_voice(x))



def num_list (a,b):
    c=list(range(a,b+1))
    return [z for z in c if z%2==1]
print(num_list(1,6))


def num_list (a,b):
    c=list(range(a,b+1))
    num_list=[]
    for x in c:
        if x%2==1:
            num_list.append(x)
    return (num_list)
print(num_list(4,9))