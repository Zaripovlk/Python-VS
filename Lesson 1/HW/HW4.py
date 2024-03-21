# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no
a = int(input("введеите сторону шоколадки a:"))
b = int(input("введеите сторону шоколадки b:"))
c = int(input("введеите кол-во долек с:"))
if a * b < c or c == a * b:
   print ('no')
elif c % a == 0 or c % b == 0:
   print ('yes')
else: 
   print ('no')

   # if (c%b==0 or c%a==0)  and a*b>c:
#     print("yes")
# else:
#     print("no")


# if a * b < c or c == a * b:
#    print ('no')
# elif c % a == 0 or c % b == 0:
#    print ('yes')
# else: 
#    print ('no')


# if a>c and a%c==0:
#     print("yes")
# elif c>a and c%a==0:
#     print("yes")
# elif b>c and b%c==0:
#     print("yes")
# elif c>b and c%b==0:
#     print("yes")
# else:
#     print("no")