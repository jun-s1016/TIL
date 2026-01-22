# %% [markdown]
# 1. 숫자가 양수인지 음수인지 판별하는 함수, 단 0은 0을 출력하기

# %%
def check_sign(num):
    if num > 0:
        return "양수"
    elif num < 0:
        return "음수"
    else :
        return "0"

print(check_sign(5)) # 양수 
print(check_sign(-10)) # 음수
print(check_sign(0)) # 0

# %% [markdown]
# 2. 숫자가 짝수인지 홀수인지 판별하기

# %%
def is_even_or_odd(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"
    
print(is_even_or_odd(2)) # 짝수
print(is_even_or_odd(5)) # 홀수
print(is_even_or_odd(0)) # 짝수

# %% [markdown]
# 3. 리스트에 특정 값이 있는지 확인하기

# %%
def check_fruit(fruit_list, fruit):
    
    if fruit in fruit_list:     #fruit으로 받아온 문자열이 fruits라는 문자열로 받아온 fruit_list 라는 곳에 있니?
        return "있음"
    else:
        return "없음"

fruits = ["사과", "딸기", "멜론", "포도", "오렌지"]

print(check_fruit(fruits, "사과")) # 있음
print(check_fruit(fruits, "망고")) # 없음
print(check_fruit(fruits, "멜론")) # 있음

# %% [markdown]
# 4. 딕셔너리에 키 존재 여부 확인하기

# %%
def key_exists(dic, key):
    if key in dic:          
        return "존재함"
    else:
        return "존재하지 않음"
    pass


my_dict = {"제목": "Drowning", "아티스트": "WOODZ", "발매일": "2023-04-26"}

print(key_exists(my_dict, "제목"))  # 존재함
print(key_exists(my_dict, "순위"))  # 존재하지 않음
print(key_exists(my_dict, "아티스트"))  # 존재함

# %% [markdown]
# 5. 리스트 합 구하기 (sum 사용 금지)
#    - `누적 합` 이라는 개념을 나타낼 변수가 필요합니다.
#    - 숫자를 더하기 전 `누적 합`은 0에서 시작하며, 숫자를 하나씩 더해가면 계속 바뀌게 됩니다.
#    - 1+2+3+4+5 를 계산하는 과정으로 예를 들어보면,
#    - 0 + 1 = 1
#    - 1 + 2 = 3
#    - 3 + 3 = 6
#    - 6 + 4 = 10
#    - 10 + 5 = 15
#    - 이전 누적합 + 현재 숫자 = 새로운 누적합

# %%
def sum_list(lst):
    amount = 0
    for num in lst:           #lst 그자체를 받아왔어. num 을 lst 안에 있는 숫자로 볼거야.
        amount+=num           # 첫 경우 1 2 3 4 5 를 받아오고, 두번째는 100 200 300 으로 받아올거고, 그걸 차례차례 더할거야.
    return amount

print(sum_list([1,2,3,4,5])) # 15
print(sum_list([100,200,300])) # 600
print(sum_list([])) # 0

# %% [markdown]
# 6. 리스트 길이 구하기 (len 사용 금지)
#     - 합을 구했던 이전 문제를 참고해 보세요. 이번에는 `길이` 를 나타낼 변수가 필요합니다.

# %%
def len_list(lst):
    length=0
    for num in lst: #lst길이 만큼 돈다.
        length+=1   # 돈 만큼 길이에 +1을 한다.
    return length

print(len_list([1,2,3,4,5])) # 5
print(len_list([100,200,300])) # 3
print(len_list([])) # 0

# %% [markdown]
# 7. 딕셔너리의 모든 key 와 value 출력하기 (for 문 사용)

# %%
def print_dict(dic):
    for i,j in dic.items():           #.items()는 딕셔너리의 키 밸류를 쌍으로 갖고와준다.
        print(f" key:{i}/ value:{j}") # 그래서 i 랑 j 두개의 변수를 지정해 각각 키 밸류에 넣어준다.

print_dict({"번호" : 1, (1,3,4): "튜플은 키로 사용 가능", 1 : "숫자도 사용 가능"})
# key : 번호 / value : 1
# key : (1, 3, 4) / value : 튜플은 키로 사용 가능
# key : 1 / value : 숫자도 사용 가능

# %% [markdown]
# 8. 리스트에서 홀수만 출력

# %%
def print_odd(lst):

    for num in lst:
        if num % 2 == 1:
            print(num)
        
print_odd([1,2,3,4,5,99]) 
# 1
# 3
# 5
# 99

# %% [markdown]
# 9. 문자열에서 모음 개수 세기(hint : str.islower())

# %%
def get_vowels_count(text):
    vowel = ['a','e','i','o','u']
    vowel_num=0

    for i in text:         # 순차적으로 i 에 h e l l o 를 넣는다.
        if i in vowel:     # vowel(모음) 에 h 가 있다면? e가 있다면? , , , , ,
            vowel_num +=1  # vowel_num 을 +1 하자...

    return vowel_num


print(get_vowels_count("hello")) # 2
print(get_vowels_count("world")) # 1
print(get_vowels_count("hello my name is minseok")) # 8

# %% [markdown]
# 10. 문자열에서 각 글자가 등장한 횟수 세기, 딕셔너리로 반환
#     - 딕셔너리에 원소를 새로 추가하는 것과 변경하는 것의 차이를 생각해보세요.

# %%
def char_count(text):
    save = {}           #우선 딕셔너리를 지정해주고,
    for i in text:      #i에 가 나 다 가 나 다 를 들고 오는데.
        if i in save:   #만약 '가' 가 '가나다가나다' 딕셔너리에 있다면.
            save[i] +=1 # key:'가'를 이미 본 사람이라면 +1
        else :
            save[i] = 1 # key:'가' 를 처음봤다면 초기값을 1로 설정해주고
    
    return save         # 계산된 key value 값이 지정된 딕셔너리를 return 해준다.

print(char_count("가나다가나다")) # {'가': 2, '나': 2, '다': 2}
print(char_count("123123123")) # {'1': 3, '2': 3, '3': 3}
print(char_count("jazz is good")) # {'j': 1, 'a': 1, 'z': 2, ' ': 2, 'i': 1, 's': 1, 'g': 1, 'o': 2, 'd': 1}
