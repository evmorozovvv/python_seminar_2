# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


n = int(input("Введите количество монеток на столе: "))
orel = int(input("Введите количество орлов: "))

reshka = n - orel

if orel <= n/2 and orel >= 0:
    print (orel)
elif orel > n/2 and orel <= n:
    print (reshka)
else:
    print ("Invalid number of coins")


 