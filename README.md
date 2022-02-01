# Xakaton
Компоненты XXXX для приложения "Народный Контроль". Данное приложение было разработано с помощью Python 3.10.1 и Django 4.0.1

## **Установка приложения**

1. Клонировать компоненты репозитория в удобное для вас место.
2. Создать вирутальное окружение с помощью virtualenv.
'''python
   python -m venv env
3. Затем необходимо перейти в созданное виртуальное окружение.
```python
    .\ИМЯ ОКРУЖАЮЩЕЙ СРЕДЫ\Scripts\activate # пример для Windows
```
4. Установить зависимости компонентов с помощью requirements.txt.
```python
   pip install -r requirements.txt
```
5. В файле settings.py указать настройки подключения к базе данных в переменной "DATABASES"
```
 'default': {
    'ENGINE': 'django.db.backends.mysql', 
    'NAME': 'DATABESE_NAME',
    'USER': 'USER_NAME',
    'PASSWORD': 'PASSWORD',
    'HOST': 'HOSTNAME',
    'PORT': 'PORT',  # default 3306
    }
```
6. Извлекаем обновленные модели из базы данных 
```python
   python manage.py inspectdb > ИМЯ ПРИЛОЖЕНИЯ\models.py
```
7. Меняем кодировку файла models.py с UTF-16 LF на UTF-8
8. В файле ИМЯ ПРИЛОЖЕНИЯ\admin.py регистрируем модели #если есть новые модели
```python
   admin.site.register(ИМЯ МОДЕЛИ)
```
9. Делаем миграцию командой
```python
   python manage.py migrate 
```
10. Создаем суперпользователя для взаимодействия с админ-панелью
```python
   python manage.py createsuperuser
```
и вводим необходимые данные


## **Запуск Приложения**

1. Запускаем консоль в папке приложения и запускаем сервер
```python
   python manage.py runserver PORT
              или
   python manage.py runserver IP:PORT
              или
   python manage.py runserver #default 127.0.0.1:8000
```
2. Переходим по ссылке и авторизуемся
```python
   http://IP:PORT/admin/login/
```

