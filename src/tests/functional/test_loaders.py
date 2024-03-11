import pytest

from dataloaders import CountryLoader, NewsLoader
from models.countries import CountryModel
from models.news import NewsModel


class TestCountryLoader:
    @pytest.fixture
    def loader(self):
        return CountryLoader()

    def test_load_one_country(self, loader):
        country: CountryModel = loader.load("RU").get()
        assert country.name == "Russian Federation"
        assert country.alpha2code == "RU"
        assert country.alpha3code == "RUS"
        assert country.capital == "Moscow"
        assert country.region == "Europe"
        assert country.subregion == "Eastern Europe"
        assert country.population == 146599183
        assert country.latitude == 60.0
        assert country.longitude == 100.0
        assert country.demonym == "Russian"
        assert country.area == 17124442.0
        assert country.numeric_code == "643"
        assert country.flag == "http://assets.promptapi.com/flags/RU.svg"
        assert country.currencies == ["RUB"]
        assert country.languages == ["Russian"]

    def test_load_many_countries(self, loader):
        countries: list[CountryModel] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(countries) == 3


class TestNewsLoader:
    @pytest.fixture
    def loader(self):
        return NewsLoader()

    def test_load_one_news(self, loader):
        news: list[NewsModel] = loader.load("RU").get()

        assert len(news) == 20
        news_item = news[0]
        assert news_item.author == "Хибины.ru"
        assert news_item.source == "Google News"
        assert (
            news_item.title
            == "Есть ли братья по разуму: Обнаружена планета с океаном и контрастной "
            "температурой — для кого подходят такие условия жизни - новости Хибины.ru - Хибины.ru"
        )
        assert news_item.description is None
        assert (
            news_item.url
            == "https://news.google.com/rss/articles/CBMirgFodHRwczovL3d3dy5oaWJpbnkucnUvbXVybWFuc2theWE"
            "tb2JsYXN0L25ld3MvaXRlbS1lc3RsaS1icmF0eWEtcG9yYXp1bXUtb2JuYXJ1amVuYS1wbGFuZXRhLXNva2Vhbm9t"
            "LWlrb250cmFzdG5veS10ZW1wZXJhdHVyb3ktZGx5YS1rb2dvLXBvZGhvZHlhdC10YWtpZS11c2xvdml5YS1qaXpuL"
            "TMyNTUxMy_SAQA?oc=5"
        )

    def test_load_many_news(self, loader):
        news: list[list[NewsModel]] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(news) == 3
