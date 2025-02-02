# Проект `News Collector`

## Описание
News Collector — это приложение для сбора новостей с сайта [NewsAPI.org](https://newsapi.org/) с помощью API. Оно позволяет получать статьи за вчерашний день и сохранять их в JSON-файл с учетом заданных ключевых слов и слов-исключений.

## Функциональность
- Получение списка новостей по ключевым словам.
- Фильтрация статей по списку слов-исключений.
- Сохранение данных в JSON-файл с автоматическим названием.
- Логирование процесса работы приложения.

## Установка
### 1. Клонирование репозитория
```sh
git clone https://github.com/ldixitl/news-collector.git
```
### 2. Установка зависимостей
Используется Poetry для управления зависимостями. Убедитесь, что Poetry установлен.
После установки выполните:
```sh
poetry install
```
### 3. Настройка переменных окружения
Создайте файл переменных окружения `.env` - [**шаблон такого файла**](.env.sample).

## Использование
Запустите `main.py` и следуйте инструкциям:
```sh
python main.py
```
Введите ключевые слова для поиска и список слов, которые нужно исключить из результатов.

## Логирование
Логи работы приложения сохраняются в папке `logs/` в файлах:
- `logs/main.log`
- `logs/news.log`
- `logs/save_to_file.log`

## Пример сохраненного JSON-файла
```json
[
    {
        "title": "The Americans have nerve, asking us to sacrifice teenagers",
        "author": "Lt Yulia Mykytenko and Lara Marlowe",
        "description": "In the second column in a monthly series, the 29-year-old commander of a Ukrainian drone unit discusses fighting on while being unable to grieve for those lost in combat and how and when the war might end",
        "url": "https://www.irishtimes.com/life-style/people/2025/02/01/the-americans-have-nerve-asking-us-to-sacrifice-teenagers/"
    }
]
```

## Лицензия
Этот проект лицензирован по [лицензии MIT](LICENSE).

