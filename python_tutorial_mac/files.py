from pathlib import Path  # Path is a class

path = Path()  # 若不寫路徑 則默認當前目錄
path1 = Path("ecommerce")  # 相對路徑或絕對路徑皆可
path2 = Path("mail")
print(path.exists())  # 查看路徑是否存在
# print(path2.mkdir())  # 若路徑不存在 直接建一個資料夾 make directory
# path2.rmdir()  # remove directory

# path.glob() 攫取路徑
for file in path.glob("*.py"):  # *代表全部 也可寫成 *.* *.html *.php 攫取對應檔案
    print(file)

for file in path.glob("*"):  # 攫取所有檔案
    print(file)