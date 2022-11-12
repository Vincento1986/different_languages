from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)

def pytest_addoption(parser):
    
    # Можно задать значение параметра по умолчанию, 
    parser.addoption('--language', action='store', default="ru", help="Choose language!")


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    language = None
    language = request.config.getoption("language")  # получаем параметр командной строки language
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
