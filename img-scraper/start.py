from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
import requests
import io
from PIL import Image
import time
import json

wd = webdriver.Chrome()

def download_image(download_path, url, file_name):
    with open('../img-scraper/urls.json', 'w') as f:
        json.dump(url, f, indent=4, ensure_ascii=False)

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





def get_images(driver, delay, max_images):
    # def scroll_down(driver):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(delay)

    logos_urls = []

    with open('../json/predictions.json', 'r') as f:
        teams = json.load(f)  


    for team in teams['data']:
        team = team['home_team']

        print(team)

        url = f"https://www.google.com/search?sxsrf=AB5stBgsjkBv66FxCb74wcAgXKkU64tjIw:1689663636123&q={team}+fc+logo+png&tbm=isch&sa=X&ved=2ahUKEwidosjG15eAAxW_g_0HHaFwBocQ0pQJegQIDBAB&biw=1360&bih=657&dpr=1"
        driver.get(url)

        image_urls = set()

        while len(image_urls)  < max_images:
            # scroll_down(wd)

            thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

            for img in thumbnails[len(image_urls) :max_images]:
                try:
                    img.click()
                    time.sleep(delay)
                except:
                    continue


                images = wd.find_elements(By.CLASS_NAME, "r48jcc")
                for image in images:
                    # if image.get_attribute('src') in image_urls:
                    #     max_images += 1
                    #     break
                    
                    # if image.get_attribute('src') and 'https' in image.get_attribute('src'):
                    if image.get_attribute('src'):

                        src = image.get_attribute('src')
                        print(src)
                        logos_urls.append(src)    

                        try:
                            image_urls.add(image.get_attribute('src'))

                            print(f"Found {len(image_urls)}")
                        except:
                            continue

        for url in image_urls:
            download_image(f"../static/logos/", url, team + ".png")

    for team in teams['data']:
        team = team['away_team']

        print(team)

        url = f"https://www.google.com/search?sxsrf=AB5stBgsjkBv66FxCb74wcAgXKkU64tjIw:1689663636123&q={team}+fc+logo+png&tbm=isch&sa=X&ved=2ahUKEwidosjG15eAAxW_g_0HHaFwBocQ0pQJegQIDBAB&biw=1360&bih=657&dpr=1"
        driver.get(url)

        image_urls = set()

        while len(image_urls)  < max_images:
            # scroll_down(wd)

            thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

            for img in thumbnails[len(image_urls) :max_images]:
                try:
                    img.click()
                    time.sleep(delay)
                except:
                    continue


                images = wd.find_elements(By.CLASS_NAME, "r48jcc")
                for image in images:
                    # if image.get_attribute('src') in image_urls:
                    #     max_images += 1
                    #     break
                    
                    # if image.get_attribute('src') and 'https' in image.get_attribute('src'):
                    if image.get_attribute('src'):
                        
                        image_urls.add(image.get_attribute('src'))

                        print(f"Found {len(image_urls)}")

        for url in image_urls:
            download_image(f"../static/logos/", url, team + ".png")

    with open('logos_urls.json', 'w') as f:
        json.dump(logos_urls, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    get_images(wd, 1, 2)
    wd.quit()

