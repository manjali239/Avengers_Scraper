from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request
import time
import os
from urllib.parse import urlparse, urljoin

# Path to ChromeDriver (Use your correct path)
chrome_driver_path = 'C:\\Users\\Manjali\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# Set up Chrome options to ignore SSL errors
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Set the path for the Downloads folder
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")  # Path to Downloads folder

# Initialize Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = 'https://www.ranker.com/list/list-of-every-avenger-of-all-time/super-hero-teams'
    driver.get(url)
    
    # Retry loading and scrolling to ensure all elements appear
    for attempt in range(3):
        # Scroll down gradually to load dynamic content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Adjust delay if needed

        # Check if elements are loaded
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
            )
            break  # Exit loop if elements are found
        except Exception:
            print(f"Retrying... (Attempt {attempt + 1}/3)")

    # Parse the rendered page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all list items containing the character information
    list_items = soup.find_all('li', class_='listItem_main__gsJuN')
    
    # Check if list items were found
    if not list_items:
        print("No list items found on the page.")
    else:
        for item in list_items:
            # Extract the character name (heading)
            name_tag = item.find('h2')
            name = name_tag.get_text(strip=True) if name_tag else "No name found"

            # Extract the image URL
            img_tag = item.find('img')
            image_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

            # Resolve relative image URLs to absolute URLs
            if image_url and not image_url.startswith('http'):
                image_url = urljoin(url, image_url)

            # Extract the text description (paragraph)
            description_tag = item.find('p')
            description = description_tag.get_text(strip=True) if description_tag else "No description available"

            # Output the extracted data
            print(f"Name: {name}")
            print(f"Image URL: {image_url}")
            print(f"Text Description: {description}\n")
            
            # Download the image if it is a PNG or JPG
            if image_url:
                # Check if the image URL ends with .png or .jpg
                if not (image_url.endswith('.png') or image_url.endswith('.jpg')):
                    continue  # Skip if not PNG or JPG

                # Define the filename for saving the image
                image_name = os.path.basename(image_url).split('?')[0]  # Strip query parameters from filename

                # Sanitize filename to avoid invalid characters
                image_name = image_name.replace('<', '_').replace('>', '_').replace(':', '_').replace('"', '_').replace('/', '_').replace('\\', '_').replace('|', '_').replace('?', '_').replace('*', '_')

                # Construct the full path to save the image
                save_path = os.path.join(download_folder, image_name)

                # Download the image
                try:
                    urllib.request.urlretrieve(image_url, save_path)
                    print(f'Downloaded image: {save_path}')
                except Exception as img_e:
                    print(f"Failed to download {image_name}: {img_e}")
            
finally:
    driver.quit()
