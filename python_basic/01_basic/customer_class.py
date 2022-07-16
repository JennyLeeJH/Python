# 콘솔형 고객 정보 관리 시스템 구축

# 1. 기능  
# 고객 정보 입력(I), 현재/이전/다음 고객 정보 조회(C/P/N), 고객 정보 수정(U), 고객 정보 삭제(D), 고객 정보 종료(Q)

# - 괄호 안 영문자를 입력하면(대소문자 구분 안함) 각 기능이 구현되게 만든다
# - 종료(Q)를 입력하기 전까지 기능 선택 메시지가 계속 뜨도록 만든다
# - 각 기능은 함수로 관리한다
# - 입력된 각 정보는 인덱스 값에 따라 페이지를 가진다
#   -> 첫 정보 입력 시 인덱스는 0이므로, 입력 전 기본 page 값은 -1로 설정한다

# 2. 입력(I)
# - dictionary로(데이터 한 건당) 각 키의 값을 받고 빈 리스트에 채워나간다
# - 이름
# - 성별(gender) : M, m, F, f로만 입력 가능
#   -> 소문자로 입력하는 경우 대문자로 자동 변환
#   -> gender 값이 M 또는 F가 아닐 경우 다시 입력
# - 이메일(email) : 입력값 내 '@'가 반드시 있어야 함
#   -> 정규표현식 사용
#   -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악
#   -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함
# - 출생년도(birthyear) : 4자리로 입력, 숫자로 입력되어야 함
#   -> len 값으로 입력 값의 길이를 구함
#   -> 4자리가 아닐 경우 재입력 하도록 함
# - 출생년도까지 입력이 완료되었을 경우
#   -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append)한다
#   -> 고객 정보가 새로 입력 되었으므로 page 값에 1을 더한다

# 3. 조회(C, P, N)
# - 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력시 page+1 값을 반환한다
# - 이전 페이지 조회(P)의 경우, 첫 번 째 페이지인 상태에서 이전 페이지로 이동이 불가하므로 현재 페이지인 첫 번 째 페이지를 반환
# - 다음 페이지 조회(N)의 경우, 마지막 페이지인 상태에서 다음 페이지로 이동이 불가하므로 현재 페이지인 마지막 페이지를 반환


# 4. 삭제(D)
# - unique한 키를 기준으로 삭제정보를 선택한다 -> 여기서는 이메일로 가정
# - 삭제 성공 여부 변수(delok)
#   -> 입력한 이메일이 등록된 정보 내에 있을 경우 삭제
#   -> 삭제가 성공하면 delok=1 (default 값 0)
#   -> 등록된 정보 내에 없는 이메일일 경우(delok=0) 등록되지 않았다고 출력

# 5. 수정(U)
# - unique한 키를 기준으로 수정 정보를 선택한다 -> 여기서는 이메일로 가정
# - 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력
#   -> idx의 default 값은 -1
#   -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
# - 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
# - 수정할 정보 선택 후 수정할 내용 입력
# - 수정하고 픈 변수가 없는 경우 exit 입력 시 수정 창 종료

# 6. 종료(Q)
# - 맨 처음 while 반복문을 나간다 -> break


import sys,json,re

class Customer:
    
    def data_load(self, path):
        f = open(path, 'r')
        data = json.load(f)
        f.close()
        return data

    def data_save(self, path, data):
        f = open(path,'w')
        json.dump(data,f,indent=True)
        f.close()

    def customer_input(self):
        customer = {}
        customer['name'] = input('이름 >>>')
        while True:
            customer['gender'] = input('성별(M,F) >>>').upper()
            if customer['gender'] in ('M', 'F'):
                break
        while True:
            p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.](kr|com|org|net)$')
            while True:
                customer['email'] = input('emmail >>>')
                result = p.match(customer['email'])
                if result:
                    break
                else:
                    print('@를 포함하여 정확한 이메일을 기입하세요')
            
            #똑같은 이메일이 있는지 여부 확인하기
            check = 0
            for i in self.custlist:
                if customer['email'] == i['email']:
                    check = 1
            if check == 0:
                break
            else:
                print('중복된 이메일입니다.')
        while True:
            customer['birth'] = input('출생년도 4자리 >>>')
            if len(customer['birth']) == 4 and customer['birth'].isdigit():
                break
        self.custlist.append(customer)
        page = len(customer) - 1
        print(customer)
        print(self.custlist)
        return page # 데이터 값이 복사되어 넘어올 경우 변경 값을 꼭 리턴시켜줘야 한다.

    def cur_page(self):
        if self.page < 0:
            print('입력된 정보가 없습니다.')
        else:
            print(f'현재 페이지는 {self.page+1}페이지 입니다.')
            print(self.custlist[self.page])

    def pre_page(self):
        if page <= 0:
            print('첫번째 페이지 입니다. 이전 페이지 이동이 불가합니다.')
        else:
            page -= 1
            print(f'현재 페이지는 {page+1}페이지입니다.')
            print(self.custlist[page])
        print(page)
        return page #페이지 값을 -1씩 변경 되기에 리턴해줘야 한다.

    def next_page(self):
        if page >= len(self.custlist) - 1 :
            print('마지막 페이지입니다. 다음 페이지로 이동이 불가합니다.')
        else:
            page += 1
            print(f'현재 페이지는 {page+1}페이지입니다.')
            print(self.custlist[page])
        print(page)
        return page

    def customer_delete(self):
        email = input('삭제하려는 email >>>')
        delok = 0
        for i in range(len(self.custlist)):
            if email == self.custlist[i]['email']:
                print('{} 고객님의 정보가 삭제됩니다.'.format(self.custlist[i]['name']))
                del self.custlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 고객입니다.')
        print(self.custlist)

    def customer_update(self):
        while True:
            email = input('수정할 고객 이메일 >>>')
            idx = -1
            for i in range(len(self.custlist)):
                if email == self.custlist[i]['email']:
                    idx = i
                    break
            if idx == -1:
                print('등록되지 않은 이메일입니다.')
                break
            choice1 = input('''
    다음 중 수정할 항목을 선택하세요. (name, genger, birth) 
    >>>''') #들여쓰기가 됨으로 앞에서 부터 적어주기
            self.custlist[idx][choice1] = input('수정할 {}을 입력하세요 >>>'.format(choice1))
            print(self.custlist)
            break

    def exe(self):
        choice = input('''
==============================================================
                    고객정보관리 프로그램
==============================================================
I-입력 C-현재 정보 P-이전 정보 N-다음 정보 U-수정 D-삭제 Q-종료
        ''').upper()

        if choice == "I":  
            self.customer_input() # page로 변경된 리턴값 받아줘야 한다.
        elif choice =="C": 
            self.cur_page()
        elif choice == 'P':
            self.pre_page()
        elif choice == 'N':
            self.next_page()
        elif choice == 'D':
            self.customer_delete()
        elif choice == "U": 
            self.customer_update()
        elif choice == "Q":
            self.data_save('python_basic/01_basic/custlist.json', self.custlist)
            sys.next()

    def __init__(self):
        self.custlist = self.data_load('python_basic/01_basic/custlist.json')
        #custlist = []
        self.page = len(self.custlist) - 1

        while True:
            self.exe()

Customer()