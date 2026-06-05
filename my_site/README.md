# Create Project
```
python --version
```

## Сeate venv - віртуальне середоще для вашого проекту і пакетів
```
py -m venv .venv
python -m venv .venv
python3 -m venv .venv
```
## Перегляд списку бібліотек їх збереження та клонування проекту
```
pip freeze
pip freeze > requirements.txt

git clone https://github.com/MaksymPlichuk/ClassWork_Python
cd ClassWork_Python
cd my_site
py -m venv .venv
.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip
pip install -r requirements.txt
cd silpo
py manage.py migrate
py manage.py runserver 9581
```
# Create SuperUser
```
cd silpo
py manage.py createsuperuser
```

## Working users Custom Django
```
py manage.py startapp users
pip install Pillow 
py manage.py makemigrations users
py manage.py migrate
```