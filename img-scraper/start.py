from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

PATH = "img-scraper\webdriver\chromedriver.exe"

wd = webdriver.Chrome()


def get_images(driver, delay, max_images):
    # def scroll_down(driver):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(delay)

    url = "https://www.google.com/search?sxsrf=AB5stBgsjkBv66FxCb74wcAgXKkU64tjIw:1689663636123&q=Envigado+FC+logo+png&tbm=isch&sa=X&ved=2ahUKEwidosjG15eAAxW_g_0HHaFwBocQ0pQJegQIDBAB&biw=1360&bih=657&dpr=1"
    driver.get(url)

    image_urls = set()

    while len(image_urls)  < max_images:
        # scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

        for img in thumbnails[len(image_urls) :max_images]:
            
            img.click()
            time.sleep(delay)


            images = wd.find_elements(By.CLASS_NAME, "r48jcc")
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")

    return image_urls

       


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "PNG")

        print("hyeeee!")
    except Exception as e:

        print('FAILED -', e)



urls = get_images(wd, 1, 3)

for i, url in enumerate(urls):
	download_image("imgs/", url, str(i) + ".png")

wd.quit()