from selenium import webdriver
import requests
import io
from PIL import Image

PATH = "img-scraper\webdriver\chromedriver.exe"

driver = webdriver.Chrome()

image_url = "https://flagdownload.com/wp-content/uploads/Flag_of_Spain_Flat_Round-1024x1024.png"

# driver.get(image_url)

def download_image(download_path, url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name

    with open(file_path, "wb") as f:
        image.save(f, "PNG")

    print("hyeeee!")

download_image("img-scraper/", image_url, "test.png")