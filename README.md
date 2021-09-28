# DRF task
Задание по изучению DRF

## Инструкция по запуску
1. Склонировать этот репозиторий

2. Установить зависимости из файла requirements.txt
* pip install -r requirements.txt
   
3.Создать базу данных
* python manage.py makemigrations
* python manage.py migrate
   
4.Запустить проект
* python manage.py runserver

## Использование
/authors - список авторов;
/books - список книг;
/library - список книг с возможность поиска по наименованию книги или имени автора;

Для удаления или редактирования записи необходимо в url добавить ее id. 
Пример - authors/1

Поиск данных по по наименованию книги или имени автора производится с помощью /library/?search=...  

