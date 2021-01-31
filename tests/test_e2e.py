#End to End - Buying product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjectsModel.CheckOutPage import CheckOutPage
from PageObjectsModel.HomePage import HomePage
from PageObjectsModel.LastPagePurchase import LastPagePurchase
from PageObjectsModel.ProductsPage import ProductsPage
from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        productspage = homePage.shopItems()
        log.info("getting all the card titles")
# Select Product from Products page and click on checkout button
        products = productspage.getCardTitles()
        i = -1
        for product in products:
            i = i+1
            Productname = product.text
            print(Productname)  # no need to give // or / in "div/h4/a "when you are appending 2 xpaths
            if Productname == "Blackberry":
                productspage.addToCart()[i].click()
    #click on checkout
        checkoutpage = productspage.getcheckoutfromProductPage()

#verify product in cart
        CartProduct = checkoutpage.getVerifyProduct().text
        assert Productname == CartProduct
    #click on checkout
        lastpage =checkoutpage.CheckoutButtonInCheckoutpage()
        log.info("entering country as ind")
#type country in checkout page
        lastpage.EntryCountryName().send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
    #select checkbox
        lastpage.CheckBoxSelection().click()
        assert self.driver.find_element_by_xpath("//input[@id='checkbox2']").is_selected()
    #click on purchase
        lastpage.Purchase().click()
        SuccessText = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text
        log.info("text received from application is " +SuccessText)
        assert "Success" in SuccessText

#taking screenshot
        self.driver.get_screenshot_as_file("success.png")
        print("End to End Testing completed !!!")