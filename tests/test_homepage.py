import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from PageObjectsModel.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class Testhomepage(BaseClass):
    def test_formsubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is" + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        # chcekbox
        homepage.getCheckbox().click()
        # dropdown
        self.selectOptionByText(homepage.getGender(), getData["gender"])  # locator
        # click on submit
        homepage.getSubmit().click()
        message = homepage.getAlert().text
        assert "success" in message
        # add refresh else 2nd data will get concatenate with 1st data
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase1"))
    def getData(self, request):
        return request.param
