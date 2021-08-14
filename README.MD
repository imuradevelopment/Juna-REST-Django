# juna

## 環境設定

|Package| Version|
|:----|:----|
|asgiref| 3.3.4|
|Django| 3.2.3|
|django-cleanup| 5.2.0|
|django-cors-headers| 3.7.0|
|djangorestframework| 3.12.4|
|Pillow| 8.2.0|
|pip| 21.0.1|
|pytz| 2021.1|
|setuptools| 54.1.2|
|sqlparse| 0.4.1|
|wheel| 0.36.2|

## メモ

```bash
cd ../../mnt/c/work/REST
find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*django/db/*" -delete
find .  -path "*/migrations/*.pyc" -not -path "*django/db/*" -delete
```
