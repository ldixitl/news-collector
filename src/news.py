import datetime
import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
BASE_URL_NEWS = os.getenv("BASE_URL_NEWS")


logger = logging.getLogger("news")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/news.log", mode="w", encoding="UTF-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_news(query: str, exclude_words: list, api_key: str = API_KEY_NEWS) -> list:
    """
    Получает новости с сайта newsapi.org на основе заданного запроса и исключает статьи, содержащие определенные слова.

    Параметры:
    query (str): Ключевые слова для поиска новостей.
    exclude_words (list): Список слов, наличие которых в статье исключает её из результатов.
    api_key (str, optional): API ключ для доступа к newsapi.org. По умолчанию используется API_KEY_NEWS.

    Возвращает:
    list: Список словарей, содержащих основную информацию о статьях (заголовок, автор, описание, ссылка).
    """
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    params = {
        "q": query,
        "from": yesterday.strftime("%Y-%m-%d"),  # При необходимости заменить эту строку для изменения даты публикации
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }
    try:
        logger.info(f"Выполняем запрос с ключевыми словами: {query}")
        response = requests.get(url=BASE_URL_NEWS, params=params)

        news_data = response.json()
        if news_data.get("status") != "ok":
            logger.info("Статьи по ключевым словам не найдены")
            return []

        articles_list = news_data.get("articles", [])
        print(articles_list)
        articles_result = []

        logger.info(f"Фильтруем новости по словам исключениям: {', '.join(exclude_words)}")
        for article in articles_list:

            content = f"{article.get('title')} {article.get('content')} {article.get('description')}".lower()
            if any(word.lower() in content for word in exclude_words):
                continue

            articles_result.append(
                {
                    "title": article.get("title"),
                    "author": article.get("author"),
                    "description": article.get("description"),
                    "url": article.get("url"),
                }
            )

        return articles_result
    except requests.RequestException as e:
        logger.error(f"Произошла ошибка: {e}")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []
