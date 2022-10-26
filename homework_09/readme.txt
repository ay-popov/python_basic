Запуск проекта:
pip install -r requirements.txt
cd ordersbook
python manage.py runserver

Запуск тестов
python manage.py test

Описание:
Добавлены фикстуры employees/fixtures
Добавлены тесты в employees/tests/test_employees.py
Добавлены тесты в myauth/tests/test_login.py

--------------------------------------------------------------
админка		http://127.0.0.1:8000/admin/        (admin 123456)
сотрудники  http://127.0.0.1:8000/employees/
наряды		http://127.0.0.1:8000/orders/




