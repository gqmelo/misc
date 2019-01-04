import re


# def pytest_addoption(parser):
#     parser.addoption("--stringinput", action="append", default=[],
#         help="list of stringinputs to pass to test functions")


def pytest_collection_modifyitems(items):
    def sort_by_language_and_account_key(item):
        m = re.search(r"\[.*?LANGUAGE\((.+?)\)-ACCOUNT\((.+?)\)\]", item.name)
        if m:
            return m.group(2), m.group(1)
        else:
            return ()

    items[:] = sorted(items, key=sort_by_language_and_account_key)


def pytest_generate_tests(metafunc):
    if "language" in metafunc.fixturenames:
        metafunc.parametrize("language", ["en", "ja"],
                             ids=["LANGUAGE(en)", "LANGUAGE(ja)"],
                             scope="session")
    if "account" in metafunc.fixturenames:
        metafunc.parametrize("account", ["ms1", "ms2"],
                             ids=["ACCOUNT(ms1)", "ACCOUNT(ms2)"],
                             scope="session")
