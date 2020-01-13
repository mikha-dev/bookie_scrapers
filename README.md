### Oddsportal scraper

####  Usage:
```
from oddsportal.oddsportal import OddsPortal

config = {
    "url": "https://www.oddsportal.com/soccer/england/premier-league/",
    "data_path": "./data",
    "competition_name": "premier-league"
}

OddsPortal(config).start_scraper()

```
#### Installation:
```
pip install bookie-scrapers
```

#### Run: 

Since we are "tabbing" the windows it will switch focus to the browser, running it within a virtual framebuffer 
is preferable if you do not run it on a dedicated server.  
```.env
xvfb-run python main.py
```

For testing purposes one can run the script as is and watch the browser switch tabs.

### Requirements

chromedriver for your version of google chrome must be in your PATH

Xvfb if you're going running within virtual buffer

https://chromedriver.chromium.org/
### TODO:

* Reload crashed windows
* Add correct waits instead of python time.sleep(.)
* Add support for other browsers than google Chrome/Chromium
* Add support for custom repositories
* Add more bookies and customizable scrapers
* Add Docker support
