import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def capabilities(capabilities):
    capabilities["goog:loggingPrefs"] = {"browser": "ALL", "performance": "ALL"}
    # capabilities['goog:chromeOptions'] = {'perfLoggingPrefs': {"enableNetwork": True, "enablePage": False}}
    return capabilities


# @pytest.fixture
# def driver_kwargs(driver_kwargs):
#     driver_kwargs['desired_capabilities']['goog:chromeOptions'] = {'perfLoggingPrefs': {"enableNetwork": True, "enablePage": False}}
#     return driver_kwargs


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_experimental_option('perfLoggingPrefs', {"enableNetwork": True, "enablePage": False})
    return chrome_options


def test_chrome_perf_logs(pytestconfig, selenium):
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
