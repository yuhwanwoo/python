# 특정 범위 혹은, 시쿼스같은
# 반복가능한 객체의 요소들을 순차적으로
for num in [1,2,3,4,5] :
    print(num)
print("끝")

for num in range(10):
    print(num)

# 조건과 같이
for num in range(1,31) :
    if num%2:
        print(num)

print("끝")

# for_dictionary
dict_a={
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30
}

list_a=['삼성','역삼','선릉']
for data in dict_a.keys() :
    print(data)

for key,val in dict_a.items():
    print(key,val)