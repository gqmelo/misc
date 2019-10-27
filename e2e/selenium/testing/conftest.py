import re


# def pytest_addoption(parser):
#     parser.addoption("--stringinput", action="append", default=[],
#         help="list of stringinputs to pass to test functions")

import pytest
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
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
