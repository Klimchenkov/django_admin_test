Установка
===================
1. Запустить проект с помощью докера:
   ```bash
   docker-compose up -d --build
   ```
2. Создать суперюзера для доступа к админке:
   ```bash
   docker exec -it django_admin_test-app-1 ./manage.py createsuperuser
   ```

Использование
===================
1. После запуска сервиса открыть админ панель по адресу http://0.0.0.0:8000/admin . Ввести имя пользователя и пароль, сохранённые при создании суперюзера

2. В админ панели в разделе  'Events' есть подразделы 'Пользователи', 'События' и 'Типы задач'. Данные подразделы созданы с использованием StackedInline подкласса класса Admin. В них можно создавать объекты связанных моделей, редактировать их и удалять. Можно добавлять несколько объектов одним submit-ом.