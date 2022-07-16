import random

total = 0
hit = 0
oper = ['+', '-', '*', '/']
while True:
    a = random.randint(1,50)
    b = random.randint(1, 50)
    op = random.choice(oper) #리스트 안에 있는 값을 무작위로 뽑아준다
    quiz = str(a) + op + str(b)
    print(quiz)
    result = int(input('>>>'))
    total += 1

    if result == int(eval(quiz)):
        print('정답')
        hit += 1
    else:
        print('오답')
    if 'Q' == input('종료(Q) >>>').upper():
        break

print(f'맞춘 문항수:{hit}/전체 문항 수:{total}')