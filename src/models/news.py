from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NewsModel(BaseModel):
    """
    Модель для описания новостей.
    """

    title: str = Field(title="Название")
    author: Optional[str] = Field(title="Автор")
    description: Optional[str] = Field(title="Описание")
    content: Optional[str] = Field(title="Контент")
    source: str = Field(title="Источник")
    url: str = Field(title="Ссылка")
    published_at: datetime = Field(title="Дата публикации")
