Books Web Scraping + EDA

A Python project that scrapes book data from [books.toscrape.com](https://books.toscrape.com) and runs exploratory data analysis (EDA) on it with pandas.

## What it does

1. `scrapper.py` scrapes all 50 catalogue pages (1000 books) and saves them to `books_data.csv`.
2. `eda.py` cleans the data (converts price from text like `£51.77` to a number), checks data quality, answers a few questions, and saves `books_clean.csv`.

## Dataset

| Column | Description |
|---|---|
| title | Book title |
| price | Price in GBP (£) |
| rating | Star rating, 1 to 5 |
| availability | Stock status |

## Key findings

- **1000 books**, 4 columns, **0 missing values**, **0 duplicate rows**.
- **Prices range from £10.00 to £59.99**, with a mean of £35.07 and a median of £35.98.
- **Ratings are spread fairly evenly**: 1-star is the most common (226 books) and 4-star the least (179).
- **Price barely changes with rating**: the average price stays between £34.56 and £36.09 across all ratings, so price is not a strong signal of rating on this site.