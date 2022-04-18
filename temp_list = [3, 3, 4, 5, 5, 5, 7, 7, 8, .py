#set사용
temp_list = [3, 3, 4, 5, 5, 5, 7, 7, 8, 9, 10, 10, 10]
temp_set = set(temp_list)
temp_list = list(temp_set)
print(temp_list)
#for사용
temp_list = [3, 3, 4, 5, 5, 5, 7, 7, 8, 9, 10, 10, 10]
new_list = []
for i in temp_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
#Anagram문제풀이
str1 = input("첫번째 문장을 입력해주세요.:")
str2 = input("두번째 문장을 입력해주세요.:")


