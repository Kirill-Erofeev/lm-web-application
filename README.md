# Гайд по веб-приложению, использующему языковую модель
### Установка приложения
Клонирование репозитория
```cmd
git clone https://github.com/Kirill-Erofeev/lm-web-application.git
```
Переход в корневую папку проекта
```cmd
cd ./lm-web-application
```
Создание виртуального окружения
```cmd
python -m venv venv
```
Активация виртуального окружения
```cmd
venv\Scripts\activate.bat
```
Установка зависимостей
```cmd
pip install -r requirements.txt
```
Запуск приложения
```cmd
python ./__main__.py
```
> **Warning**<br>
После запуска приложения необходимо дать браузеру доступ к микрофону
> 
### Использование приложения
Перевод речи в текст и вывод языка
![Речь в текст и язык](https://github.com/user-attachments/assets/b56c4b1c-b4f7-4e87-a028-695ff70abf5e)
Предсказание эмоции
![Эмоция](https://github.com/user-attachments/assets/d38f7680-c903-4a29-9db2-13b7d19cfe69)
