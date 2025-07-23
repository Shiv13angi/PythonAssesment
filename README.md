# Restaurant Finder Script

## Overview
This Python script finds the top 10 restaurants in a specified city by searching Google and extracting restaurant information including ratings, reviews, and descriptions. The results are saved in a JSON file with restaurant names as keys.

## Features
- 🔍 **Web Scraping**: Searches Google for restaurant information
- 📊 **Data Extraction**: Extracts ratings, reviews, descriptions, and cuisine types
- 💾 **JSON Storage**: Saves data in structured JSON format
- 🛡️ **Error Handling**: Robust error handling with fallback sample data
- 🎯 **Smart Filtering**: Filters results to focus on actual restaurants
- 🔄 **Duplicate Removal**: Removes duplicate restaurant entries

## Installation

1. **Clone or download the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python restaurant_finder.py
```

The script will:
1. Prompt you to enter a city name
2. Search for restaurants in that city
3. Display the top 10 restaurants found
4. Save the results to a JSON file named `restaurants_[city_name].json`

## Output Format

The JSON file contains restaurant data structured as:
```json
{
  "Restaurant Name": {
    "rank": 1,
    "rating": 4.5,
    "reviews": 234,
    "description": "Restaurant description...",
    "city": "City Name",
    "url": "https://restaurant-url.com",
    "cuisine_type": "Italian"
  }
}
```

## Technical Approach

### 1. Web Scraping Strategy
- Uses `requests` library with rotating user agents to avoid detection
- Implements proper headers and delays to be respectful to servers
- Parses HTML content using `BeautifulSoup`

### 2. Data Extraction Methods
- **Restaurant Identification**: Uses keyword matching to identify restaurant results
- **Rating Extraction**: Regex patterns to find ratings (4.5 stars, 4.2/5, etc.)
- **Review Counting**: Extracts review counts from various formats
- **Cuisine Classification**: Intelligent guessing based on keywords

### 3. Error Handling & Fallbacks
- Network error handling with retry mechanisms
- Fallback to sample data if web scraping fails
- Graceful handling of parsing errors

### 4. Data Processing
- Deduplication based on restaurant names
- Data cleaning and normalization
- Structured JSON output with restaurant names as keys

## Challenges & Solutions

### Challenge 1: Anti-Bot Protection
**Problem**: Many websites implement measures to prevent automated scraping.
**Solution**: 
- Rotating user agents
- Proper HTTP headers
- Request delays
- Session management

### Challenge 2: Dynamic Content
**Problem**: Modern websites often load content dynamically with JavaScript.
**Solution**: 
- Multiple extraction patterns
- Alternative parsing methods
- Fallback to sample data when needed

### Challenge 3: Data Quality
**Problem**: Inconsistent data formats and quality from web sources.
**Solution**: 
- Robust regex patterns for data extraction
- Data validation and cleaning
- Smart filtering to focus on restaurant results

### Challenge 4: Rate Limiting
**Problem**: Search engines may limit request frequency.
**Solution**: 
- Built-in delays between requests
- Respectful scraping practices
- Sample data fallback

## Dependencies

- **requests**: HTTP library for making web requests
- **beautifulsoup4**: HTML parsing library
- **lxml**: Fast XML and HTML parser (optional but recommended)

## Legal & Ethical Considerations

This script is designed for educational and personal use. When using web scraping:
- Respect robots.txt files
- Don't overload servers with requests
- Consider using official APIs when available
- Be aware of terms of service

## Example Output

```
🍽️  Restaurant Finder
========================================
This script will find the top 10 restaurants in your specified city
and save the results to a JSON file.

Please enter the name of a city: New York

🔍 Searching for restaurants in New York...

============================================================
TOP 10 RESTAURANTS FOUND
============================================================

1. The Golden Fork - New York
   Rating: 4.5/5.0 (234 reviews)
   Cuisine: American
   Description: Upscale dining experience in the heart of New York...
--------------------------------------------------

✅ Successfully found 10 restaurants!
📄 Data saved to: restaurants_new_york.json
```

## Future Enhancements

Potential improvements could include:
- Integration with restaurant APIs (Yelp, Google Places)
- More sophisticated rating aggregation
- Image extraction and storage
- Price range information
- Location/address details
- Menu information extraction

## Troubleshooting

**Issue**: No restaurants found
**Solution**: Try a different city name or check internet connection

**Issue**: Script fails with network errors
**Solution**: The script includes fallback sample data for demonstration

**Issue**: Dependencies not found
**Solution**: Run `pip install -r requirements.txt`
