# 🌍 Country Population Scraper (Scrapy Project)

This project is a Scrapy spider that crawls the [Worldometers Population by Country](https://www.worldometers.info/world-population/population-by-country/) page and extracts historical population data for each country.

---

## 📦 Features

- Scrapes list of all countries from the main population page
- Follows links to each country's page
- Extracts yearly population data
- Outputs country name, year, and population

---

## 🛠 Requirements

- Python 3.7+
- Scrapy library

### Install Scrapy
```bash
pip install scrapy
```

---

## 🚀 How to Run the Spider

1. Clone the project or place the spider code in a Scrapy project folder.
2. Open terminal in the project directory.
3. Run the spider using:

```bash
scrapy crawl Countries -o output.json
```

This will save the scraped data to a file named `output.json`.

---

## 📂 Project Structure

```
population_scraper/
├── population_scraper/
│   ├── __init__.py
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── countries_spider.py
├── scrapy.cfg
└── README.md
```

---

## 🧠 How It Works

1. **Start URL**: The spider starts at the population-by-country page.
2. **Parse Function**: It extracts country names and URLs.
3. **Requests**: It sends a new request for each country, passing the name via `meta`.
4. **Second Parse**: On the country-specific page, it extracts year-wise population data.
5. **Yield**: The spider yields a dictionary with country name, year, and population.

---

## 📝 Sample Output

```json
{
  "CountryName": "India",
  "Year": "2023",
  "Population": "1,428,627,663"
}
```

---

## 🧾 Notes

- Ensure your internet connection is stable while scraping.
- This script scrapes publicly available data for educational or research purposes only.
- Be respectful of the website’s terms of service.

---

## 💡 Author

Made with ❤️ using Scrapy by [Your Name]

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
