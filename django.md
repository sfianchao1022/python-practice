# Django
Django 是一種web server框架 可以包含多個web應用模組(app) 用來統一格式利於維護

## 安裝Django (use PyCharm terminal)
```
pip install django==3.1.1
```

## 在當前project PyShop啟動django
```
(venv) (base) zhaoshoufeng@zhaoshoufengdeMacBook-Pro PyShop % django-admin startproject pyshop .
```

## 啟動django介面 由manage.py進入
```
(venv) (base) zhaoshoufeng@zhaoshoufengdeMacBook-Pro PyShop % python3 manage.py runserver
```

## 建立Django底下其中一個web應用模組(app) products
由pyshop主模組(index主畫面)統一管理 下層其他模組(products)
```
(venv) (base) zhaoshoufeng@zhaoshoufengdeMacBook-Pro PyShop % python3 manage.py startapp products
```

## pyshop/urls.py 加入跳轉路徑連到其他app module
```python
urlpatterns = [
    path('admin/', admin.site.urls),  # django主畫面

    # 路徑products/...之後的頁面 從這個路徑跳轉(之後的路徑不必在包含products/)
    path('products/', include('products.urls'), name='products')  # 跳轉到products的url 用incluse()函式 頁籤顯示products
]

```

## 由products模組的url啟動products的view顯示頁面
```python
urlpatterns = [
    path('', views.index),  # products的主畫面
    path('new', views.new),  # products/new的頁面 呼叫views的new函式(不需要加括弧)來顯示new頁面

]

```


# 連接 SQLite data base
DBMS 使用視覺化介面 DB Browser for SQLite
- [DB Browser for SQLite](https://sqlitebrowser.org)

## 在models.py底下建立table
```python
# products app底下的模組（table)
# table 1
class Products(models.Model): 
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)

# table 2
class Offer(models.Model):  
    code = models.CharField(max_length=20)  
    description = models.CharField(max_length=255)  
    discount = models.FloatField()
```

## migration table寫入資料庫
```
python3 manage.py makemigrations  # create model 建立寫入ＤＢ的python檔(0002_offer.py)
python3 manage.py migrate  # migrate 寫入ＤＢ
```
```
(venv) (base) zhaoshoufeng@zhaoshoufengdeMacBook-Pro PyShop % python3 manage.py makemigrations
Migrations for 'products':
  products/migrations/0002_offer.py
    - Create model Offer
(venv) (base) zhaoshoufeng@zhaoshoufengdeMacBook-Pro PyShop % python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0002_offer... OK

```

## create admin user 在django admin畫面操作資料庫
```
(venv) (base) zhaoshoufeng@zhaoshoufengdeMacBook-Pro PyShop % python3 manage.py createsuperuser
account : admin
password : 1234
e-mail : sfianchao@yahoo.com.tw
```

在admin.py創建要操作的products table
```python
from django.contrib import admin
from products.models import Products

# Register your models here.
admin.site.register(Products)
```
顯示table的欄位
```python
class ProductsAdmin(admin.ModelAdmin):  
    list_display = ('name', 'price', 'stock')  
  
  # Register your models here.  
admin.site.register(Products, ProductsAdmin)
```

## django設定專案路徑
設定專案路徑後，templates資料夾即可放在專案根目錄
- [Django筆記(1) - 建置與環境設定 « dokelung's Blog](http://dokelung-blog.logdown.com/posts/220274-django-note-1-building-and-settings)
```
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES : [{
  ...
  'DIRS': [  os.path.join(BASE_DIR, 'templates') ],
  ...
}]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```









