from selene import browser, be
import pytest

desktop = pytest.mark.parametrize('browser_config', [(1440, 1080), (1920, 1080)], indirect=True,
                                  ids=['desktop_1440_1080', 'desktop_1920_1080'])
mobile = pytest.mark.parametrize('browser_config', [(360, 740), (412, 915)], indirect=True,
                                 ids=['mobile_360_740', 'mobile_412_915'])


@desktop
def test_github_desktop(browser_config):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


@mobile
def test_github_mobile(browser_config):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)

