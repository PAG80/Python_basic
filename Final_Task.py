import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


class SearchTest(unittest.TestCase):
    """ Тестовый сценарий """

    def setUp(self):
        """Перед выполнением теста. Предварительная настройка браузера и переменных."""

        # Использование предварительных настроек браузера в начале инициализации теста:
        # https://www.selenium.dev/documentation/webdriver/browsers/chrome/

        options = webdriver.ChromeOptions()                                         # Создание экземпляра настроек
        options.add_argument('--disable-notifications')                             # Отключение опции уведомлений браузера
        options.add_experimental_option("useAutomationExtension", False)            # Отключение расширений, для быстроты действий
        options.add_experimental_option("excludeSwitches", ["enable-automation"])   # Отключение табло, что браузер используется автоматизированным средством
        options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})   # Установка фиксированного языка
        service = Service('chromedriver.exe')                                       # Инициализация вэб драйвера
        self.driver = webdriver.Chrome(service=service, options=options)            # Создание метода драйвера, с которым можно работать в дальнейших шагах

    def test_search_selenide(self):
        """Тест #1 - Открытие страницы и проверка заголовка"""
        # Шаг 1. Открытие страницы
        self.driver.get('https://search.yahoo.com/')
        # Проверка заголовка
        assert 'Yahoo Search - Web Search' in self.driver.title, 'Заголовок страницы не совпадает'

        # Шаг 2. Ожидание пока элемент "поисковой строки" станет видимым
        elm = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located((By.NAME, 'p')))
        # Ввод значения "selenide"
        elm.send_keys('selenide')
        # Нажатие кнопки ввода
        elm.send_keys(Keys.ENTER)

        # Шаг 3. Проверяем, что первый результат – ссылка на сайт selenide.org.
        first_result = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.title')))
        first_result_url = first_result.find_element(By.XPATH, './..').get_attribute('href')
        assert 'selenide.org' in first_result_url, 'Первый результат не ведет на сайт selenide.org'

        # Шаг 4. Перейти в раздел поиска изображений
        images_tab = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'Images')))
        images_tab.click()

        # Шаг 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        first_image = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'img')))
        first_image_alt = first_image.get_attribute('alt')
        assert 'selenide' in first_image_alt.lower(), 'Первое изображение не связано с сайтом selenide.org'

        # Шаг 6. Вернуться в раздел поиска Все
        all_tab = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'All')))
        all_tab.click()

        # Шаг 7. Проверить, что первый результат такой же, как и на шаге 3.
        new_first_result = WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.title')))
        new_first_result_url = new_first_result.find_element(By.XPATH, './..').get_attribute('href')
        assert first_result_url == new_first_result_url, 'Первый результат изменился после возврата из раздела изображений'

    def tearDown(self):
        """После выполнения теста. Удаление переменных (если нужно) и закрытие соединений"""
        self.driver.close()    # Закрыть браузер (Имитация клика Крестика в верхнем углу)
        self.driver.quit()     # Завершение сессии браузера


if __name__ == '__main__':
    unittest.main()