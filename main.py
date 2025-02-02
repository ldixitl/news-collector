import datetime
import logging
import os

from src.news import get_news
from src.save_to_file import save_to_file

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

news_dir = "news"
os.makedirs(news_dir, exist_ok=True)

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/main.log", mode="w", encoding="UTF-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def main() -> None:
    """Главная функция для работы приложения"""
    try:
        logger.info("Запрос у пользователя ключевых слов")
        query = input("Введите ключевые слова: ")
        exclude_words = input("Введите слова для исключения (через запятую): ").split(",")

        logger.info("Получение новостей")
        articles_list = get_news(query, exclude_words)

        today = datetime.datetime.today()
        today_string = today.strftime("%Y-%m-%d")

        logger.info("Запись новостей в файл")
        file_name = f"{today_string}_{query.replace(' ', '_')}.json"
        file_path = f"news/{file_name}"
        save_to_file(articles_list, file_path)
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
    finally:
        logger.info("Завершение работы приложения")


if __name__ == "__main__":
    main()
