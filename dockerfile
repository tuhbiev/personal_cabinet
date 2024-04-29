FROM python:3.9

# Установка рабочей директории
WORKDIR /code

# Копирование зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

# Прослушивание порта
EXPOSE 8000

## Копирование остального кода
#COPY . .

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
