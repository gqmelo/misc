import re
import pytest
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


# def pytest_addoption(parser):
#     parser.addoption("--stringinput", action="append", default=[],
#         help="list of stringinputs to pass to test functions")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.screenshot_labels = []
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        # if (report.skipped and xfail) or (report.failed and not xfail):
        # only add additional html on failure
        extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        if "selenium" in item.fixturenames:
            selenium = item.funcargs["selenium"]
            screenshot_reporter = selenium.screenshot_reporter
            extra_images = []
            for content, label in  screenshot_reporter.screenshots:
                extra_images.append(pytest_html.extras.png(content, label))
            extra_images.extend([elem for elem in extra if elem["format"] == 'image'])
            extra = [elem for elem in extra if elem["format"] != 'image']
            extra.extend(extra_images)
            report.screenshot_labels = [screenshot[1] for screenshot in screenshot_reporter.screenshots]
            report.screenshot_labels.append("Final state")
        report.extra = extra


from py.xml import html

def pytest_html_results_table_html(report, data):
    images = [elem for elem in data if getattr(elem.attr, "class_", "") == "image"]
    data[:] = [elem for elem in data if getattr(elem.attr, "class_", "") != "image"]
    images_elem = html.div("Images list", class_="images")
    for i, (img, label) in enumerate(zip(images, report.screenshot_labels)):
        d = html.div(f"{i+1} - {label}", class_="image-with-label", style="float: left;")
        img.attr.style = "float: none;"
        d.append(img)
        data.append(d)
    # images_elem.extend(images)
    # data.append(images_elem)
    # if report.passed:
    #     data.append(html.div('No log output captured.', class_='empty log'))


class MyListener(AbstractEventListener):
    def before_change_value_of(self, element, driver):
        driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)
        driver.screenshot_reporter.take("before_change_value_of")

    def before_click(self, element, driver):
        driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)
        driver.screenshot_reporter.take("before_click")

    def before_close(self, driver):
        driver.screenshot_reporter.take("before_close")

    def before_execute_script(self, script, driver):
        driver.screenshot_reporter.take("before_execute_script %s" % script)

    def before_find(self, by, value, driver):
        driver.screenshot_reporter.take("before_find %s, %s" % (by, value))

    def before_navigate_back(self, driver):
        driver.screenshot_reporter.take("before_navigate_back")

    def before_navigate_forward(self, driver):
        driver.screenshot_reporter.take("before_navigate_forward")

    def before_navigate_to(self, url, driver):
        driver.screenshot_reporter.take("before_navigate_to %s" % url)

    def before_quit(self, driver):
        driver.screenshot_reporter.take("before_quit")

    def after_change_value_of(self, element, driver):
        driver.screenshot_reporter.take("after_change_value_of")
        driver.execute_script("arguments[0].removeAttribute('style');", element)

    def after_click(self, element, driver):
        driver.screenshot_reporter.take("after_click")
        driver.execute_script("arguments[0].removeAttribute('style');", element)

    def after_close(self, driver):
        driver.screenshot_reporter.take("after_close")

    def after_execute_script(self, script, driver):
        driver.screenshot_reporter.take("after_execute_script %s" % script)

    def after_find(self, by, value, driver):
        driver.screenshot_reporter.take("after_find %s, %s" % (by, value))

    def after_navigate_back(self, driver):
        driver.screenshot_reporter.take("after_navigate_back")

    def after_navigate_forward(self, driver):
        driver.screenshot_reporter.take("after_navigate_forward")

    def after_navigate_to(self, url, driver):
        driver.screenshot_reporter.take("after_navigate_to %s" % url)

    def after_quit(self, driver):
        driver.screenshot_reporter.take("after_quit")

    def on_exception(self, exception, driver):
        driver.screenshot_reporter.take("on_exception %s", exception)

class MyListener2(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("MyListener2: Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("MyListener2: After navigate to %s" % url)


@pytest.fixture
def selenium(selenium):
    from unittest import mock
    original_log_types = type(selenium).log_types
    @property
    def log_types(self):
        # r = original_log_types.__get__(self)
        # return [l for l in r if l != 'browser']
        return ['browser', 'performance']
    type(selenium).log_types = log_types
    class ScreenshotReporter():
        def __init__(self, driver):
            self.screenshots = []
            self.driver = driver

        def take(self, label=""):
            self.screenshots.append((self.driver.get_screenshot_as_base64(), label))

    # selenium.implicitly_wait(5)
    selenium.screenshot_reporter = ScreenshotReporter(selenium)
    # selenium = EventFiringWebDriver(selenium, MyListener())
    # Not possible to wrap it again
    # driver = EventFiringWebDriver(driver, MyListener2())
    yield selenium 
    # time.sleep(100)