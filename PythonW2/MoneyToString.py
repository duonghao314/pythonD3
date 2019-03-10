doc_so = ["không","một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám","chín"]
doc_vi_tri = ["đồng", "mươi", "trăm", "nghìn", "mươi", "trăm", "triệu", "mươi", "trăm", "tỷ"]
money = str(input("Nhập số tiền: "))
str_money = ""
for index, c in enumerate(money):
    str_money += doc_so[int(c)] + " "
    str_money += doc_vi_tri[len(money) - index - 1] + " "

str_money = str_money.replace("không trăm không mươi không đồng", "đồng chẵn")
str_money = str_money.replace("không trăm không mươi không nghìn ", "")
str_money = str_money.replace("không mươi", "lẻ")
str_money = str_money.replace("một mươi", "mười")
str_money = str_money.replace("mười không", "mười")
print(str_money)

