import json
import os
from glob import glob

from models.news import NewsModel


class NewsService:
    """
    Сервис для работы с данными о новостях.
    """

    def get_news(self) -> dict[str, list[NewsModel]]:
        """
        Получение списка новостей
        :return:
        """

        result = {}
        for filename in glob("fixtures/news/*"):
            with open(filename, encoding="utf-8") as file:
                alpha2code = os.path.basename(filename).split(".")[0]
                if data := json.load(file):
                    result[alpha2code] = [
                        NewsModel(
                            title=news.get("title"),
                            author=news.get("author"),
                            description=news.get("description"),
                            content=news.get("content"),
                            source=news.get("source").get("name"),
                            url=news.get("url"),
                            published_at=news.get("publishedAt"),
                        )
                        for news in data.get("articles", [])
                    ]
        return result
