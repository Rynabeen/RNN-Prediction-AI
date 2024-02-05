import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к веб-драйверу (укажите свой путь)
driver_path = '/Users/alexander/Downloads/chromedriver-mac-arm64'

# Создаем экземпляр веб-драйвера с использованием ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = driver_path  # Указываем путь к исполняемому файлу

# Подключаем ChromeDriver с указанием пути к исполняемому файлу
driver = webdriver.Chrome(options=chrome_options)

try:
    while True:
        # Открываем веб-страницу
        driver.get('https://crypto.com/price/bitcoin')  # Замените ссылку на актуальную

        article_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//h2[@class="chakra-heading css-fophx6"]/span[@class="chakra-text css-13hqrwd"]'))
        )

        # Получаем текст из найденного элемента
        bitcoin_price = article_title.text

        # Выводим цену на экран
        print(f'Bitcoin Price: {bitcoin_price}')
        time.sleep(5)
        elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//p[@class="chakra-text css-1c8c51m"]'))
        )
        labels = ["Market Cap (USD)", "24H Volume" , "Circulating Supply ", "Max Supply ", "Total Supply"]
        for i, element in enumerate(elements):
            print(f'{labels[i]}: {element.text}')
            time.sleep(5)

        # И ВОТ НАША ПОЕБОТНЯ
except KeyboardInterrupt:
    print('Зачем меня выключил, а ?')





except Exception as e:
    print(f"Произошла ошибка: {e}")


finally:
    # Закрываем браузер в блоке finally, чтобы гарантировать, что он будет закрыт,
    # даже если произойдет исключение в блоке try
    driver.quit()
