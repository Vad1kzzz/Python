
def fun_proverka(i, j):
    n=0
    while True:
        try:
            print("Введите число от ",i,"до ",j)
            n=int(input())
            if(n>=i and n<=j):
                break
            else:
                print("Неверный ввод, папробуйте снова")
        except ValueError:
            print("Неверный ввод, папробуйте снова")
        
    return n

from random import *
n=0
game_type=0
print("Игра Кости!")
while True:
    print("Введите тип игры:\n 1- Игра сам с сабой \n 2-Игра с компьютером \n 3-Игра с другим игроком :")
    game_type=fun_proverka(1,3)
    print("Выбран тип ",game_type)
    break



    
     
