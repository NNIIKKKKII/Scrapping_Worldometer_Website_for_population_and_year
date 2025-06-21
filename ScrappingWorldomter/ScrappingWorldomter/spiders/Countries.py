import scrapy


class CountriesSpider(scrapy.Spider):
    name = "Countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        for country in countries:
            name = country.xpath(".//td[2]/a/text()").get()
            link = country.xpath(".//td[2]/a/@href").get()
            absolute_url = response.urljoin(link)
            

            scrapy.Request(
                url = absolute_url,
                callback = self.Country_name_and_Population,
                meta = {"CountryName" : name}
            )



    def Country_name_and_Population(self, response):
        country_name = response.meta["CountryName"]

        rows = response.xpath(".//tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/text()").get()

            yield {
                "CountryName" : country_name,
                "Year" : year,
                "Population" : population
            }
