#Clisck on Shop button to naviagte to products Homepage

from selenium.webdriver.common.by import By
from PageObjectsModel.ProductsPage import ProductsPage
from Utilities.BaseClass import BaseClass

class HomePage:
    def __init__(self, driver):
        self.driver = driver  # <-- actual test driver, we are assigning to local class driver

    Shop = (By.XPATH, "//a[@class='nav-link' and contains(.,'Shop')]")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    genders = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):
        self.driver.find_element(*HomePage.Shop).click()  #calling class vairable by class name. we use * to deserialize tuple below
        productspage = ProductsPage(self.driver) #creating object for next page
        return productspage
        # driver.find_element_by_link_text("Shop")
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    def getGender(self):
        return self.driver.find_element(*HomePage.genders)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)