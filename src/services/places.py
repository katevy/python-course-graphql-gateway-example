import json
from typing import Optional

from models.places import PlaceModel


class PlacesService:
    """
    Сервис для работы с данными о любимых местах.
    """

    def get_places(self) -> list[PlaceModel]:
        """
        Получение списка любимых мест.

        :return:
        """

        result = []
        with open("fixtures/places.json", encoding="utf-8") as file:
            if data := json.load(file):
                result = [
                    PlaceModel(
                        id=place.get("id"),
                        latitude=place.get("latitude"),
                        longitude=place.get("longitude"),
                        description=place.get("description"),
                        country=place.get("country"),
                        city=place.get("city"),
                        locality=place.get("locality"),
                        created_at=place.get("created_at"),
                        updated_at=place.get("updated_at"),
                    )
                    for place in data.get("data", [])
                ]

        return result

    def get_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Получение информации о любимом месте.
        :param place_id: Идентификатор любимого места.
        :return:
        """
        result = {place.id: place for place in self.get_places()}
        return result.get(place_id, None)
