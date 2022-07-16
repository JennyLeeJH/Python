# try:
#     value1 = int(input('첫번째 값을 입력 >>>'))
#     value2 = int(input('두번째 값을 입력 >>>'))
#     print(value1/value2)
# except:
#     print('오류')

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print('Eagle')

eagle = Eagle()
eagle.fly()