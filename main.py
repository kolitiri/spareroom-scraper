# Standard library imports
import sys

# Local imports
from spareroomScraper.search import Search

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('usage: bin/scrape <config>')
        sys.exit(0)

    # Perform a new search
    new_search = Search(sys.argv[1], 1, 20)
    new_search.search()
