import random

a, b = 1, 10
num = random.randint(a, b+1)
print('Добро пожаловать в числовую угадайку!')

def is_valid(otvet):
    if otvet.isdigit() == True and a <= int(otvet) <= b:
        return True
    else:
        return False

def final_part():
    print('Хочешь повторить?')
    if input().lower() == 'да':
        print('Хочешь задать новое крайнее число?')
        if input().lower() == 'да':
            print('Напиши число')
            global b

            while True:
                b = input()
                if b.isdigit() == False:
                    print('Введите целое число')
                else:
                    break
            b = int(b)
            num = random.randint(a, b+1)
            print('Отлично!')
            main_part(num)
        else:
            num = random.randint(a, b+1)
            main_part(num)
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        exit()

def main_part(num):
    print('Мы загадали число от', a, 'до', b, ', отгадывайте!')
    count = 0
    while True:
        otvet = input()
        count += 1
        if is_valid(otvet) != True:
            print('А может быть все-таки введем целое число от', a, 'до', b, '?')
        elif int(otvet) != num:
            if int(otvet) < num:
                print('Слишком мало, попробуйте еще раз')
            else:
                print('Слишком много, попробуйте еще раз')
        else:
            print('Вы угадали, поздравляем!')
            print('Вы сделали', count, 'попыток')
            final_part()

main_part(num)
