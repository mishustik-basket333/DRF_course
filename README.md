# DRF_course

Приветствую, это мой проект по заданию DRF

В нём выполняется поставленная задача:
"""
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.
В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.
"""

В проекте созданы приложения habit, users 

В приложении users:
  - в файле urls описаны адреса для получения token и для создания нового пользователя.
  - в файле views описан класс UserCreateAPIView.
  - в файле serializers описан класс UserSerializer.
  - в файле models переопределена модель User.
  - в файле management/commands определена функция csu, для создания суперпользователя.

В приложении habit:
  - в файле urls описаны адреса для реализации CRUD.
  - в файле views описаны соответствующие классы, для выполнения CRUD. 
  - в файле serializers описан класс HabitSerializer и указаны в нём validators, для выполнения требований проекта.
  - в файле validators описаны валидаторы, которые требуются в задании.
  - в файле models переопределена модель Habit согласно указанному заданию.
  - в файле permissions описан класс OwnerPermission для определения владельца привычки.
  - в файле pagination указаны значения вывода списка на страницу.
  - в файле tasks указана логика вызова и отправка сообщений в телеграм боте.

В корневой папке config:
  - в файле settings указаны соответствующие настройки проекта 

В файле проекта лежит .env.sample и на его основе требуется создать файл .env, для запуска проекта.
Нужно указать соответствующие ваши данные, в файле даны подсказки.

DOCKER and DOCKER COMPOSE:
  - добавлены файлы Dockerfile и docker-compose.yaml
  - команда, чтобы собрать Docker-образ. Здесь -t my-python-app задает имя образа,
  а . указывает на текущую директорию с Dockerfile:
    docker build -t my-python-app .
  - команда для запуска контейнера:
    docker run my-python-app
  - для запуска docker-compose используйте команду в терминале:
    docker-compose up --build
        
FLAKE8:
  - создан файл.flake8 с соответствующими настройками
  - для проверки кода на соответствие PEP8 используйте команду:
      flake8