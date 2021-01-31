#select product and navigate to checkout after clicking checkout button

from selenium.webdriver.common.by import By
from PageObjectsModel.CheckOutPage import CheckOutPage


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements_by_css_selector(".card-title a")
    ProductsTitle = (By.XPATH,"//h4[@class='card-title']//a")            # its a tuple example
    Addbutton = (By.XPATH,"//div//button[@class='btn btn-info']")
    Checkoutbutton = (By.XPATH,"//li[@class='nav-item active']")

    def getCardTitles(self):
        return self.driver.find_elements(*ProductsPage.ProductsTitle)

    def addToCart(self):
        return self.driver.find_elements(*ProductsPage.Addbutton)

    # click on checkout
    def getcheckoutfromProductPage(self):
        self.driver.find_element(*ProductsPage.Checkoutbutton).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage