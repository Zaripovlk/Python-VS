# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов или символами конца строки.Определите, 
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.

string =  ''' She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''
string_new = string.lower().split()
print (string_new)
string_new= set(string_new)
print (len(string_new)) 

# print(len(set(text.lower().split())))

# sym = ".,!?:;"
# str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# str = str.lower()
# for s in sym:
#     str = str.replace(s, " ")
# res = set(str.split())
# print(len(res))