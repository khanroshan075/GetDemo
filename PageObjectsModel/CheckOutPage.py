from selenium.webdriver.common.by import By
from PageObjectsModel.LastPagePurchase import LastPagePurchase

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver  # <-- actual test driver, we are assigning to local class driver

    CheckoutProduct = (By.XPATH, "//div[@class='media-body']/h4/a")
    ButtonInCheckoutpage = (By.XPATH,"//button[@class='btn btn-success']")

    def getVerifyProduct(self):
        return self.driver.find_element(*CheckOutPage.CheckoutProduct)

    def CheckoutButtonInCheckoutpage(self):
        self.driver.find_element(*CheckOutPage.ButtonInCheckoutpage).click()
        lastpage = LastPagePurchase(self.driver)
        return lastpage