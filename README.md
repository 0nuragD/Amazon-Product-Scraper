# Amazon Product Scraper

This project demonstrates web scraping and data extraction using Selenium and BeautifulSoup to gather product information from Amazon. The goal is to scrape product listings and save the data in a structured format for further analysis.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)

## Introduction

The Amazon Product Scraper project consists of two main scripts:
1. **main.py**: Automates a web browser to scrape product listings from Amazon and save the HTML content.
2. **collection.py**: Parses the saved HTML files to extract product information such as title, price, and link, and compiles the data into a CSV file.

## Features

- **Web Scraping with Selenium**: Automates browsing and data extraction from multiple pages of Amazon search results.
- **Data Parsing with BeautifulSoup**: Extracts and processes relevant information from HTML files.
- **Data Storage**: Saves extracted data into a CSV file for easy analysis and further processing.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/amazon-product-scraper.git
    cd amazon-product-scraper
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver**:
    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the same directory as your scripts or add it to your system PATH.

## Usage

1. **Run the Selenium script to scrape data**:
    ```bash
    python main.py
    ```
    This script navigates through Amazon search results for the specified query (default is "laptop"), scrapes the product listings, and saves the HTML content to the `data` directory.

2. **Run the data extraction script**:
    ```bash
    python collection.py
    ```
    This script parses the saved HTML files, extracts product information, and saves the data to `data.csv`.


## Notes

- Ensure compliance with Amazon's terms of service before scraping any data.
- The scripts are configured for Amazon India (`amazon.in`). Modify the URLs if you want to scrape data from other Amazon domains.
- The scraping process may take some time depending on the number of pages and products.



