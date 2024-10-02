import re
str3 = "12311221"

# output = [1231, 1221]
pattern = re.findall(r'(\d{1,2})\1', str3)

newList = list(set(int(t) for t in pattern))
print(newList)
# for ele in pattern :
#     print(list(set(ele)))
#
# res = str3.split("1")
# print(res)
