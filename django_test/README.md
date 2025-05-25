# Django Project

## Описание

Это проект блога на Django.

## Функции

- Регистрация и авторизация
- Создание, редактирование и удаление постов
- Просмотр списка постов, деталей поста и поиск
- Редактирование профиля
- Возможность оставлять комментарии

## Установка и настройка

### Клонирование репозитория
```bash
git clone https://github.com/project-name-link.git
cd django_test
```

### Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate
venv/Scripts/activate # Для Виндовс
```

### Установка зависимостей
```bash
pip install -r requirement.txt
```

### Применение миграций
```bash
python manage.py migrate
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Запуск сервера
```bash
python manage.py runserver
```

## Основные страницы

- Главная страница: [Ссылка](http://127.0.0.1:8000/)
- Детали поста: [Ссылка](http://127.0.0.1:8000/detail/<id>/)
- Создание поста: [Ссылка](http://127.0.0.1:8000/create/)
- Редактирование поста: [Ссылка](http://127.0.0.1:8000/update/<id>/)
- Профиль пользователя: [Ссылка](http://127.0.0.1:8000/profile/)

## Тестирование
```bash
python manage.py test blog
```
