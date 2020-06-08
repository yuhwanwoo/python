import sys
max_num=sys.maxsize
print(max_num)
super_max=max_num*max_num
print(super_max)
print(type(super_max))

# 출력해보기
print('Hello, World')
number=10
float_num=1.3
complex_num=(3+3j)
print(type(number),type(float_num),type(complex_num))

# 2. bool
print(type(True))
print(type(False))
#0, 0.0, [], {}
print(False==0)

# 3. 문자형
# '', ""
# ''
greeting='hi'
name="kim"
print(greeting,name)

# 문자열 입력 받기
# input()
age=input("나이를 입력해 주세요. : ")
print(type(age))
print(type(int(age)))

# string interpolation
name='kim'
print('안녕하세요,', name)
print('{},{}'.format(greeting,name))
print(f'{greeting},{name}')

#연산과 출력 형태 지정
pi=3.141592
print(f'원주율은 {pi:.4}, 반지름 = 2 원의 넓이는 {pi*2*2}')


