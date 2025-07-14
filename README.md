Инструкция по работе с venv Зачем нужно виртуальное окружение? Изоляция зависимостей – пакеты не конфликтуют между проектами.

Контроль версий Python – можно использовать нужную версию, не затрагивая систему.

Совместная работа – все разработчики работают в одинаковом окружении.

Как использовать venv?

Создание окружения bash python -m venv venv # или python3 на Linux/macOS
Активация Windows (CMD/PowerShell):
bash venv\Scripts\activate Linux/macOS:

bash source venv/bin/activate (После активации в начале строки появится (venv))

Установка зависимостей bash pip install -r requirements.txt # если файл есть (Или устанавливайте пакеты вручную через pip install ...)

Деактивация bash deactivate

Важно! Не добавляйте папку venv в Git – используйте requirements.txt.

Всегда активируйте окружение перед работой с проектом.

(@Deepseek)


####Для запуска fastapi: uvicorn main:app --reload

####Чтобы поднять бд и phpmyadmin: docker-compose up -d

