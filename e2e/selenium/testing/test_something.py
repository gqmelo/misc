import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def test_search_on_google(selenium):
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


@pytest.mark.parametrize('i', range(2))
def test_screenshots(i, selenium, request):
    selenium.get('https://www.google.com')
    element = selenium.find_element_by_css_selector("input[type=text]")
    element.send_keys("1")
    # selenium.screenshot_reporter.take("1")
    element.send_keys("2")
    # selenium.screenshot_reporter.take("2")
    element.send_keys("3")
    # selenium.screenshot_reporter.take("3")
    element.send_keys("4")
    # selenium.screenshot_reporter.take("4")


@pytest.mark.mask
def test_needle(needle, request):
    """Example for comparing page with a mask

    :param NeedleDriver needle: NeedleDriver instance
    :return:
    """
    # pytest_html = request.config.pluginmanager.getplugin('html')

    # Navigate to web page
    needle.driver.get('https://www.google.com')
    # pytest_html.extras.image(needle.driver.get_screenshot_as_base64())

    # Take a entire page screen diff, ignore the doodle banner
    # needle.assert_screenshot('search_page', threshold=60, exclude=[(By.ID, 'hplogo'), (By.ID, 'prm')])
