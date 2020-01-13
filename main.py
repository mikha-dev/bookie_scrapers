from oddsportal.oddsportal import OddsPortal

config = {
    "url": "https://www.oddsportal.com/soccer/england/premier-league/",
    "data_path": "./data",
    "competition_name": "premier-league"
}

OddsPortal(config).start_scraper()
