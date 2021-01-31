import pytest
from selenium import webdriver


# https://docs.pytest.org/en/latest/example/simple.html
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\roshkhan\\Documents\\Pytone notes\\driver\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\roshkhan\\Documents\\Pytone notes\\driver\\geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver #We are assigning our local driver of this fixture to class driver
    #So which ever uses this fixture in that if there is a driver variable than our local driver will go and assign to that.
    yield
  #driver.refresh()
    driver.close()
