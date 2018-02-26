# Spareroom scraper

A web scraper that performs an 'advanced' search in Spareroom and sends an email with a list of results.

It reads a configuration file and generates a payload to be used for scraping the spareroom endpoints.

Please note that this has been created only for educational purposes and I am not familiar with
Spareroom's policies. The urls used for scraping are explicitly dissalowed by the robots.txt of
of the website, thus use it politely and at your own risk!

### Requirements

1. Python (3.5.0)
2. beautifulsoup4 (4.6.0)

### Installing

These instructions will get you a copy of the project up and running on your local machine.

1. Create a python virtual environment with virtualenv
2. Install Python 3.5.0 or above
3. Clone the repository to a local directory inside the new virtual environment
4. Use pip to install the required libraries from requirements.txt

### Getting Started

1. Alter the payload_config.ini file with your search criteria (Have a look at Sparerooms 'Advanced Search' to help you understand the values of each attribute)
2. Configure emailer_config.ini with your gmail authentication details

### Usage

Navigate to the root directory of the project (spareroom-scraper/) and run the executable as:

```
bin/scrape spareroomScraper/conf/payload_config.ini
```

You can create your own payload_config.ini files for separate searches.

### Authors

* **Christos Liontos**
