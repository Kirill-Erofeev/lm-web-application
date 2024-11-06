# Гайд по веб-приложению, использующему языковую модель
### Установка приложения
Клонирование репозитория
```cmd
git clone https://github.com/Kirill-Erofeev/lm_web-application.git
```
Переход в корневую папку проекта
```cmd
cd ./lm_web-application
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
![Речь в текст и язык](https://github.com/user-attachments/assets/431bfffb-2f97-46cd-9cf3-38008446612d)
Предсказание эмоции
![Эмоция](https://github.com/user-attachments/assets/c39c5e4a-86eb-429c-aa09-295ba390b34e)
