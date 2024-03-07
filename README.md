# Кальянная полка
## Описание
Сервис для вашей домашней полки с табаками. Пользователь может зарегистрироваться и создавать свои миксы, добавлять табаки в избранное, просматривать все табаки которы есть у компании, филтровать табаки по крепкости или по различным тэгам.
## Технологии
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![image](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)

- Python 3.7
- Django 2.2.19

## Backend часть
На данный момент реализованы Django модели и настроена админка Django для базового использования.

### В планах реализации:
- API сервис для взаимодействия с frontend (*В процессе реализации*)
- Создание json файлов с данными по табакам, компаниям и т.д. для дальнейшего автоматического импорта в БД (*В процессе реализации*)
- Разделение в Docker контейнеры (БД, Backend, Frontend)
- Настройка СI/CD и дальнейший запуск на сервере

### Инструкция по установке
##### Клонируем репозиторий на компьютер:

```bash
git@github.com:Fluttik/hookah-shelf.git
```
```
cd hookah-shelf
```

##### Cоздаем и активируем виртуальное окружение:
###### **Windows**
---
```bash
python -m venv venv 
```
```bash
source venv/Scripts/activate 
```
---
 ###### **Linux**
---
```bash
python3 -m venv venv 
```

```bash
source venv/bin/activate
```
---
##### Устанавливаем зависимости:
```bash
cd backend
```
```
pip install -r requirements.txt
```

#####  Выполняем миграции:
```bash
python manage.py makemigrations
```
```
python manage.py migrate
```
##### Создаем суперпользователя
```
python manage.py createsuperuser
```
##### Запускаем сервер
```
python manage.py runserver
```
#### Заходим через удобный браузер в Django admin
```
127.0.0.1:8000/admin
```
## Frontend часть
На данный момент Frontend часть не реализована

Автор: Николай Королёв