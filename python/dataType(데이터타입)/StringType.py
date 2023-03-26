# 문자열 indexing
str1 = 'hello python'
str_len = len(str1)
print(f"문자열 길이 : {str_len}")

print(str1[0], str1[6], str1[str_len-1])

# 문자열 내부 검색 (특정 문자 검색)
find_word = 'th'
res = find_word in str1
print(f'{find_word} 단어검색 : {res}')

# 문자열 자르기 (슬라이싱)

# str1[ start index : end index] (start index 포함 end index 미포함)
print(str1[0:2])  # index 0 ~ index 1 까지
print(str1[1:])  # index 1 ~ 끝까지
print(str1[:3])  # 처음부터 index 2까지
print(str1[:-2])  # 처음부터 끝에서 -2 까지

