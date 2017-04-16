import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.nasa.gov/")
    driver.find_element_by_name('query').send_keys('Leonov')
    driver.find_element_by_xpath("//input[@value='Search']").click()
    WebDriverWait(driver,10).until(EC.title_is("Leonov - NASA Search Results"))
