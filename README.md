# Spareroom scraper
A web scraper that performs an advanced search in Spareroom and sends an email with a list of results.

It reads a configuration file and generates a payload to be used for scraping the spareroom endpoints.

Please note that this has been created only for educational purposes and I am not familiar with
Spareroom's policies. The urls used for scraping are explicitly dissalowed by the robots.txt of
of the website, thus use it politely and at your own risk!

### TODO

1. filter_advert: Needs to be implemented so that we can manually filter the results further more by scraping the individual adverts. Spareroom filters are not very accurate and sometimes they return additional results.
2. Unit tests
3. Improve payload_config.ini readability
4. Improve the emailer class

### Prerequisites

1. Python (3.5.0)
2. pytest (3.2.3)
3. beautifulsoup4 (4.6.0)

### Installing

These instructions will get you a copy of the project up and running on your local machine.

1. Create a python virtual environment with virtualenv
2. Install Python 3.5.0
3. Use pip to install the required libraries from requirements.txt
4. Clone the repository to a local directory

## Getting Started

1. Alter the payload_config.ini file with your search criteria (Have a look at Sparerooms 'Advanced Search' to help you understand the values of each attribute)
2. Configure
3. Run spareroom_scraper.py module by specifying the configuration file to be used

## Authors

* **Christos Liontos**
