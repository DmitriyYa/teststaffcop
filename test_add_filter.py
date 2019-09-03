# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddFilter(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_filter(self):
        wd = self.wd
        #login
        wd.get("http://192.168.100.3/accounts/login/?next=/")
        wd.find_element_by_id("id_username").send_keys("admin")
        wd.find_element_by_id("id_password").send_keys("123")
        wd.find_element_by_css_selector('input[type="submit"]').click()

        #add filter
        wd.find_element_by_css_selector('.menuitem-menu-hideable hideable ng-binding').click()
        wd.find_element_by_xpath('/html/body/div[3]/sc-header/ul[1]/li[2]/ul/li[1]/a/span').click()
        wd.find_element_by_css_selector('.input-xlarge ng-pristine ng-untouched ng-valid ng-not-empty').send_keys('myfilter')
        wd.find_element_by_xpath('/html/body/div[5]/div[3]/button[2]').click()

        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Запомнить меня'])[1]/following::input[2]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Создать'])[1]/following::i[1]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Создать'])[1]/following::span[1]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Название'])[1]/following::input[1]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Название'])[1]/following::input[1]").clear()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Название'])[1]/following::input[1]").send_keys("qwe")
        # wd.find_element_by_link_text(u"Уведомления").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Уведомления'])[1]/following::a[1]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Удалить'])[1]/following::button[1]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Дашборды'])[1]/following::span[1]").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Меню'])[1]/following::div[1]").click()
        # wd.find_element_by_link_text(u"Завершить работу").click()
        # wd.find_element_by_id("id_username").clear()
        # wd.find_element_by_id("id_username").send_keys("admin")
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
