# -*- coding: utf-8 -*-
from selenium import webdriver
from filter import Filter

import unittest


class TestAddFilter(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.maximize_window()

    def create_group(self, wd, filter):
        #init filter creation
        wd.find_element_by_css_selector('a[title="Create"]').click()
        wd.find_element_by_css_selector('.open > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        #fill filter form
        wd.find_element_by_css_selector('.input-xlarge').clear()
        wd.find_element_by_css_selector('.input-xlarge').send_keys(filter.title)
        wd.find_element_by_css_selector('.nav-tabs > li:nth-child(2) > a:nth-child(1)').click()
        wd.find_element_by_css_selector('#id_emails').send_keys(filter.list_emails_send)
        wd.find_element_by_css_selector('.nav-tabs > li:nth-child(3) > a:nth-child(1)').click()
        #submit filter creation
        wd.find_element_by_css_selector('button.btn-success:nth-child(2)').click()

    def logout(self, wd):
        wd.find_element_by_css_selector('li.dropdown:nth-child(7) > a:nth-child(1)').click()
        wd.find_element_by_css_selector(
            'li.dropdown:nth-child(7) > ul:nth-child(2) > li:nth-child(8) > a:nth-child(1)').click()

    def login(self, wd, username, password):
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def open_home_page(self, wd):
        wd.get("http://192.168.100.3/accounts/login/?next=/")

    def tearDown(self):
        self.wd.quit()

    def test_add_filter(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "123")
        self.create_group(wd, Filter("Myfilter", "asdasdasd"))
        self.logout(wd)

    # def test_add_empty_filter(self):
    #     wd = self.wd
    #     self.open_home_page(wd)
    #     self.login(wd, username="admin", password="123")
    #     self.create_group(wd, namefilter='')
    #     self.logout(wd)


if __name__ == "__main__":
    unittest.main()
