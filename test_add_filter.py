# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest


class TestAddFilter(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.maximize_window()
    
    def test_add_filter(self):
        wd = self.wd
        #login
        wd.get("http://localhost/accounts/login/?next=/")
        wd.find_element_by_id("id_username").send_keys("admin")
        wd.find_element_by_id("id_password").send_keys("123")
        wd.find_element_by_css_selector('input[type="submit"]').click()

        #add filter
        wd.find_element_by_css_selector('a[title="Create"]').click()
        wd.find_element_by_css_selector('.open > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        wd.find_element_by_css_selector('.input-xlarge').send_keys('Myfilter')
        wd.find_element_by_css_selector('.nav-tabs > li:nth-child(2) > a:nth-child(1)').click()
        wd.find_element_by_css_selector('.nav-tabs > li:nth-child(3) > a:nth-child(1)').click()
        wd.find_element_by_css_selector('button.btn-success:nth-child(2)').click()

        #logout
        wd.find_element_by_css_selector('li.dropdown:nth-child(7) > a:nth-child(1)').click()
        wd.find_element_by_css_selector('li.dropdown:nth-child(7) > ul:nth-child(2) > li:nth-child(8) > a:nth-child(1)').click()

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
