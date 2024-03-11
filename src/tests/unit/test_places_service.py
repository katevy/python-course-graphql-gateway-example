from datetime import date

from services.places import PlacesService


def test_read_place():
    """
    Тестирование сервиса мест
    """
    place = PlacesService().get_place(1)
    assert place.id == 1
    assert place.city == "Perm"
    assert place.country == "RU"
    assert place.latitude == 58.0081
    assert place.longitude == 56.249
    assert place.locality == "Sverdlovsky City District"
    assert place.description == "Супер место!"
    assert place.created_at.date() == date(2022, 10, 29)
    assert place.created_at.date() == date(2022, 10, 29)
