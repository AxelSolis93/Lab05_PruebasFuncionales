import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestPage:
    def SetUp(self): #Inicia la pagina maximizada en firefox
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.calculator.net/")
        self.driver.maximize_window()
        
    def TearDown(self): #Cierra la pagina
        self.driver.quit()

    def test_percent(self): 
        
        self.driver.find_element(By.XPATH, ".//*[@id = 'homelistwrap']/div[3]/div[2]/a").click()
      
        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[2]/tbody/tr/td/div[3]/a").click() #Percent

        self.driver.find_element(By.ID, "cpar1").send_keys("10")


        self.driver.find_element(By.ID, "cpar2").send_keys("50")


        self.driver.find_element(By.XPATH, ".//*[@id='content']/form[1]/table/tbody/tr[2]/td/input[2]").click()

        result = self.driver.find_element(By.XPATH, ".//*[@id='content']/p[2]/font/b").text
     
       

        print("El resultado es: " + result)

        assert "5" in result

    def test_binary(self):
        
        self.driver.find_element(By.XPATH, ".//*[@id = 'homelistwrap']/div[3]/div[2]/a").click()
      
        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[2]/tbody/tr/td/div[7]/a").click() #bin

        
        self.driver.find_element(By.ID, "number1").clear()
        self.driver.find_element(By.ID, "number1").send_keys("10101010")

        self.driver.find_element(By.ID, "number2").clear()
        self.driver.find_element(By.ID, "number2").send_keys("11111111")
        
        
        self.driver.find_element(By.XPATH, ".//*[@id='content']/form/table/tbody/tr[2]/td/input[2]").click()

        result = self.driver.find_element(By.XPATH, ".//*[@id='content']/div[2]/font/b").text
   

        print("El resultado es: " + result)

        assert "0110101001" in result


    def test_area(self):
        
        self.driver.find_element(By.XPATH, ".//*[@id = 'homelistwrap']/div[3]/div[2]/a").click()
      
        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[4]/tbody/tr/td/div[4]/a").click() #area
        #/html/body/div[3]/div[1]/ #Content


        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[1]/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[1]/tbody/tr/td[1]/form/table/tbody/tr[1]/td[2]/input").send_keys("15")
        
        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[1]/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, ".//*[@id = 'content']/table[1]/tbody/tr/td[1]/form/table/tbody/tr[2]/td[2]/input").send_keys("30")
        
        
        
        self.driver.find_element(By.XPATH, ".//*[@id='content']/table[1]/tbody/tr/td[1]/form/table/tbody/tr[3]/td/input[2]").click()

        result = self.driver.find_element(By.XPATH, ".//*[@id='content']/table[1]/tbody/tr[3]/td[2]/font/b").text
      

        print("El resultado es: " + result)

        assert "450 meters2" in result


def test_run():
    test_instance = TestPage()
    test_instance.SetUp()
    test_instance.test_percent()
    test_instance.TearDown()

    test_instance.SetUp()
    test_instance.test_binary()
    test_instance.TearDown()

    test_instance.SetUp()
    test_instance.test_area()
    test_instance.TearDown()

test_run()

