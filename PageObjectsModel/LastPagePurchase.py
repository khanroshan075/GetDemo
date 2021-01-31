from selenium.webdriver.common.by import By

class LastPagePurchase:

    def __init__(self, driver):
        self.driver = driver  # <-- actual test driver, we are assigning to local class driver

    counrtyname = (By.XPATH,"//input[@id='country']")
    CheckBox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Purchasebutton = (By.XPATH,"//input[@value='Purchase']")

    def EntryCountryName(self):
        return self.driver.find_element(*LastPagePurchase.counrtyname)

    def CheckBoxSelection(self):
        return self.driver.find_element(*LastPagePurchase.CheckBox)

    def Purchase(self):
        return self.driver.find_element(*LastPagePurchase.Purchasebutton)