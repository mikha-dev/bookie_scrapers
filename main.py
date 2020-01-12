from oddsportal.scraper_client import ScraperClient

config = {
    "url": "https://www.oddsportal.com/soccer/england/premier-league/",
    "data_path": "./data",
    "competition_name": "premier-league"
}

ScraperClient(config).start_scraper()
