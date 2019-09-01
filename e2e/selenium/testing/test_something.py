import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(5)
    yield selenium
    # time.sleep(100)


# def test_search_on_google(selenium):
#     selenium.get("https://www.google.com")
#     element = selenium.find_element_by_css_selector("input[type=text]")
#     element.screenshot("/tmp/element1.png")

#     element.send_keys("selenium with python and pytest")
#     element.screenshot("/tmp/element2.png")
#     value = element.get_attribute("value")

#     assert "pytest" in value
#     assert "python" in value

#     element.send_keys(Keys.ENTER)
#     main_element = selenium.find_element_by_id("main")
#     assert "pytest" in main_element.text


@pytest.mark.parametrize("i", range(0, 100))
def test_crazy_button(i, selenium):
    selenium.implicitly_wait(30)
    wait = WebDriverWait(selenium, 30)

    selenium.get("http://localhost:8080")

    element = wait.until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#button1"))
    )

    def click_with_retry(driver):
        try:
            element.click()
        except:
            return False
        return True
    wait.until(click_with_retry)
    # element.click()
