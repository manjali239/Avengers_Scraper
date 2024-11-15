# Avenger Character Image Scraper#

## Description

This Python script scrapes information about Avengers from the following URL:  
`https://www.ranker.com/list/list-of-every-avenger-of-all-time/super-hero-teams`. The script extracts:
- The name of each Avenger
- A short description of the character
- The image URL for the character

The images are downloaded in `.jpg` or `.png` formats and saved to your Downloads folder.

## Features
- Scrapes Avengers' character details (name, description, image).
- Downloads character images in `.png` or `.jpg` format.
- Resolves relative URLs for images.
- Uses Selenium to handle dynamic content loading.
- Handles SSL errors and retries for loading the page.

## Prerequisites

- Python 3.x
- ChromeDriver (Ensure it is installed and the path is correct for your system)

## Installation

# Clone this repository:
   https://github.com/manjali239/Avengers_Scraper.git


# Install the required dependencies:
pip install -r requirements.txt


# Ensure that you have ChromeDriver installed and the correct path is set in the script:
chrome_driver_path = 'path_to_your_chromedriver'

# Run the script:
python scraper.py

How it Works
The script uses Selenium to open the web page and wait for the images to load dynamically.
BeautifulSoup is used to parse the HTML of the page once it’s fully loaded.
The character name, description, and image URL are extracted.
The image URL is downloaded and saved to the Downloads folder.
The script handles errors gracefully and retries if necessary.


Example Output
# For each character, the script will output the following:
Name: Thor
Image URL: https://imgix.ranker.com/user_node_img/112/2239723/original/thor-comic-book-characters-photo-u12?auto=format&amp;q=60&amp;fit=crop&amp;fm=pjpg&amp;dpr=2&amp;crop=faces&amp;h=125&amp;w=125
Text Description: God of Thunder, Thor Odinson is an Asgardian prince and one of the mightiest warriors in all Marvel Comics...
Downloaded image: C:\Users\Manjali\Downloads\thor-comic-book-characters-photo-u12.jpg
Requirements
Selenium: Used to automate the browser.
BeautifulSoup4: Used to parse the HTML.
urllib: Used to download images.

# To install the dependencies, run the following command:
pip install selenium beautifulsoup4 Pillow

# Make sure your Chrome browser version matches the ChromeDriver version.
The script assumes that images are in .jpg or .png format and saves them accordingly. Images in other formats will be skipped.

