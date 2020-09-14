# dictionary
customer = {
    "name": "Ian",  # key-value
    "age": 24,
    "is_verified": True
}
customer["name"] = "Chao"
customer["sex"] = "male"  # add key-value to dictionary
print(customer["sex"])
print(customer["name"])  # 中括弧內的key要有雙引號
# print(customer["birthdate"])  # error
print(customer.get("birthdate"))  # 用get()嘗試 若找不到相應的key會回傳none(object)
print(customer.get("birthdate", "1995 oct 22"))  # default value to key (若找不到key就印出）

# phone mapping
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
phone = input("your phone is = ?")
output = ""
for char in phone:
    output += digit_mapping.get(char, "*") + " "  # get() default的若型態和output不同 會無法組合
print(output)

# emoji converter
message = input(">")
words = message.split(" ")  # 用空格把string分開 並存成list型態
print(words)
output = ""
emojis = {
    ":)": "😀",  # mac emoji : ctrl + command + space
    ":(": "😢"
}
for word in words:
    output += emojis.get(word, word) + " "  # 若沒有對應的key default還是輸出原本的word 有在dictionary內的key才替換
print(output)

