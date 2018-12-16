import pytest
import time
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(5)
    yield selenium
    # time.sleep(100)


def test_something(selenium):
    selenium.get("https://www.google.com")
    element = selenium.find_element_by_css_selector("input[type=text]")
    element.screenshot("/tmp/element1.png")

    element.send_keys("selenium with python and pytest")
    element.screenshot("/tmp/element2.png")
    value = element.get_attribute("value")

    assert "pytest" in value
    assert "python" in value

    element.send_keys(Keys.ENTER)
    main_element = selenium.find_element_by_id("main")
    assert "pytest" in main_element.text
