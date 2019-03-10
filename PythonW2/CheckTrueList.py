isList = True
input = "[12,25,'acv',18,16]"

for index, c in enumerate(input):
    if c == "[" and index != 0:
        isList = False
    if c == "]" and index != (len(input)-1):
        isList = False

new_str = input[1:len(input)-1]
print(new_str)
list = new_str.split(",")
ele_true = 0
for ele in list:
    isString = True
    isNumber = False

    if (ele[0] == "'" or ele[0] == '"') and (ele[len(ele)-1] == "'" or ele[len(ele)-1] == '"' ):
        #print(ele + " là string")
        pass
    else:
        #print(ele + " không phải string")
        isString = False
    if ele.isdigit():
        #print(ele + " là số")
        isNumber = True
    if isString or isNumber:
        ele_true += 1
if ele_true != len(list):
    isList = False
print(isList)

