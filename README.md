### Oddsportal scraper

####  Usage:
```
config = {
    "url": "https://www.oddsportal.com/soccer/england/premier-league/", # URL to all upcoming fixtures
    "data_path": "./data", # Were output files are saved
    "competition_name": "premier-league", # Name to be  used for output file
}

ScraperClient(config).start_scraper()
```

#### run: 

Since we are "tabbing" the windows it will switch focus to the browser, running it within a virtual framebuffer 
is preferable if you do not run it on a dedicated server.  
```.env
Xvfb :99 -screen 0 640x480x8 -nolisten tcp &
```
For testing purposes one can run the script as is and watch the browser switch tabs.

### requirements

chromedriver for your version of google chrome must be in your PATH

https://chromedriver.chromium.org/
### TODO:

* Reload crashed windows
* Add correct waits instead of python time.sleep(.)
* Add support for other browsers than google Chrome/Chromium