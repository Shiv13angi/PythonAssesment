#!/usr/bin/env python3
"""
Restaurant Finder Script

This script prompts the user for a city name, searches for the top 10 restaurants
in that city using web scraping techniques, and stores the restaurant data in a JSON file.

"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
import random
from urllib.parse import quote_plus

class RestaurantFinder:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Mozilla/5.0 (X11; Linux x86_64)'
        ]
        self.session = requests.Session()

    def _random_headers(self):
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html',
            'Accept-Language': 'en-US,en;q=0.5'
        }

    def search(self, city):
        query = f"best restaurants in {city} ratings reviews"
        url = f"https://www.google.com/search?q={quote_plus(query)}&num=20"
        try:
            print(f"Searching in: {city}")
            res = self.session.get(url, headers=self._random_headers(), timeout=10)
            soup = BeautifulSoup(res.content, 'html.parser')
            return self._parse_results(soup, city)
        except:
            print("Something went wrong, showing sample results.")
            return self._sample_data(city)

    def _parse_results(self, soup, city):
        results = []
        blocks = soup.find_all('div', class_='g')

        for block in blocks:
            title = block.find('h3')
            if not title:
                continue

            name = title.get_text(strip=True)
            if not self._is_likely_restaurant(name):
                continue

            link = block.find('a')['href'] if block.find('a') else ''
            snippet = block.find('div', class_='VwiC3b')
            text = snippet.get_text(strip=True) if snippet else ''
            rating = self._extract_rating(text)
            reviews = self._extract_reviews(text)

            results.append({
                'name': self._clean_name(name),
                'rating': rating,
                'reviews': reviews,
                'description': text,
                'url': link,
                'city': city
            })

            if len(results) >= 10:
                break

        return results

    def _is_likely_restaurant(self, name):
        keywords = ['restaurant', 'cafe', 'grill', 'bar', 'diner', 'bistro']
        return any(k in name.lower() for k in keywords)

    def _extract_rating(self, text):
        match = re.search(r'(\d\.\d)\s?(?:stars?|/5)', text)
        return float(match.group(1)) if match else None

    def _extract_reviews(self, text):
        match = re.search(r'(\d{2,5})\s+reviews', text)
        return int(match.group(1)) if match else None

    def _clean_name(self, name):
        return re.split(r'[-–—,|]', name)[0].strip()

    def _sample_data(self, city):
        return [
            {
                'name': f"Spice Hub - {city}",
                'rating': 4.3,
                'reviews': 320,
                'description': "Popular for curries and biryani",
                'url': '',
                'city': city
            },
            {
                'name': f"Pizza Junction - {city}",
                'rating': 4.1,
                'reviews': 210,
                'description': "Local favorite for wood-fired pizza",
                'url': '',
                'city': city
            }
        ]

    def save_to_file(self, data, city):
        data_map = {item['name']: item for item in data}
        file_name = f"restaurants_{city.lower().replace(' ', '_')}.json"
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data_map, f, indent=2)
        print(f"\nData saved to {file_name}")

    def show_results(self, data):
        print("\nTop Restaurants:\n")
        for idx, r in enumerate(data, 1):
            print(f"{idx}. {r['name']} ({r.get('rating', 'N/A')}/5)")
            print(f"   {r['description'][:100]}...")
            print()

def main():
    print("Restaurant Finder\n")
    city = input("Enter city: ").strip()
    if not city:
        print("City required.")
        return

    app = RestaurantFinder()
    data = app.search(city)
    app.show_results(data)
    app.save_to_file(data, city)

if __name__ == "__main__":
    main()
