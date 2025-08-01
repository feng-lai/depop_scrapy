[English](README.md) | [العربية](README-ar.md) | [Português](README-pt.md) | [Español](README-es.md)
# Depop Product Scraper

## Overview
This Python script automates the extraction of product information from Depop.com using Selenium and BeautifulSoup. It collects various product details including title, price, description, images, options, and reviews, then structures the data into a JSON format for further processing.

## Key Features

- **Automated Data Collection**: Uses Selenium WebDriver to navigate and extract data from Depop product pages
- **Comprehensive Product Details**: Captures:
  - Product title and price
  - Detailed description
  - Multiple product images (up to 8)
  - Available options/variations
  - Customer reviews with ratings
- **Image URL Processing**: Extracts and processes image URLs with regex pattern matching
- **JSON Integration**: 
  - Reads existing image upload results from `upload_results.json`
  - Replaces original image URLs with new ones from the upload results
  - Outputs complete product data to `product_info.json`

## Technical Implementation

- **Selenium WebDriver**: For browser automation and dynamic content handling
- **BeautifulSoup**: For HTML parsing of complex description content
- **WebDriverWait**: Ensures robust element loading before extraction
- **JSON Processing**: Handles both reading and writing JSON data
- **Error Handling**: Comprehensive exception handling for all data points

## Usage

1. Set the target product URL in `product_page_url`
2. Ensure ChromeDriver is properly installed via ChromeDriverManager
3. Run the script to:
   - Open the product page
   - Extract all specified data points
   - Process and transform the data
   - Generate a structured JSON output
4. The script automatically closes the browser upon completion

## Output Structure
The final JSON includes:
```json
{
  "price": "extracted_price",
  "itm_name": "product_title",
  "img1" to "img8": "processed_image_names",
  "itm_dsc": "product_description",
  "cat_id": "category_id",
  "s_id": "seller_id",
  "attr": ["option1", "option2"],
  "eva": [{"name": "reviewer", "content": "review", "level": 5}]
}
```

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup4
- webdriver-manager
- Chrome browser

Note: The script includes robust error handling that provides default values when data isn't found, ensuring it completes execution even if some elements are missing from the page.


