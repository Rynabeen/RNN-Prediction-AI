from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import datetime
driver_path = '/Users/alexander/Downloads/chromedriver-mac-arm64'

# Создаем экземпляр веб-драйвера с использованием ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = driver_path  # Указываем путь к исполняемому файлу

# Подключаем ChromeDriver с указанием пути к исполняемому файлу
driver = webdriver.Chrome(options=chrome_options)
# Путь к веб-драйверу (укажите свой путь)


try:
    # Открываем веб-страницу
    driver.get('https://crypto.com/price/bitcoin')

    # Ожидаем загрузки графика
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'highcharts-series'))
    )
    time.sleep(5)  # Даем дополнительное время для загрузки данных (может потребоваться на вашем сайте)

    # Получаем HTML-код страницы
    page_source = driver.page_source

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Находим все элементы с классом 'highcharts-series'
    series_elements = soup.find_all(class_='highcharts-series')

    for series_element in series_elements:
        # Извлекаем данные (пример)
        time_data = series_element.find('path')['d']
        price_data = series_element.find('path')['fill']

        # Далее, вам нужно проанализировать структуру данных (time_data и price_data) и извлечь нужную информацию

        # Выводим время и цену
        print(f'Time: {time_data}, Price: {price_data}')



except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Закрываем браузер
    driver.quit()
