from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://demoqa.com/text-box')
    time.sleep(2)

    #заполнение поля full_name
    full_name = driver.find_element(By.ID,'userName')
    full_name.send_keys('Hello World')
    time.sleep(2)

    # заполнение колонки email
    email = driver.find_element(By.ID,'userEmail')
    email.send_keys('owner_of_valhalla@text.com')
    time.sleep(2)

  #заполнение колонки current adress
    current_adress = driver.find_element(By.ID,'currentAddress')
    current_adress.send_keys('Midgard')
    time.sleep(2)
  #заполнение колонки permanent adress
    permanent_adress = driver.find_element(By.ID,'permanentAddress')
    permanent_adress.send_keys('Valhalla')
    time.sleep(2)
  #клик на кнопку submit
    submit_button = driver.find_element(By.ID,'submit')
    submit_button.click()
    time.sleep(10)


    # Проверка через assert
    def test_full_name(element):
        expected_name = "Name:Hello World"
        actual_name = element.find_element(By.ID, "name").text
        assert actual_name == expected_name, f"Expected name to be '{expected_name}', but got '{actual_name}'"


    def test_email(element):
        expected_email = "Email:owner_of_valhalla@text.com"
        actual_email = element.find_element(By.ID, "email").text
        assert actual_email == expected_email, f"Expected email to be '{expected_email}', but got '{actual_email}'"


    def test_current_address(element):
        expected_current_address = "Current Address :Midgard"
        actual_current_address = element.find_element(By.ID, "currentAddress").text
        assert actual_current_address == expected_current_address, f"Expected current address to be '{expected_current_address}', but got '{actual_current_address}'"


    def test_permanent_address(element):
        expected_permanent_address = "Permananet Address :Valhalla"
        actual_permanent_address = element.find_element(By.ID, "permanentAddress").text
        assert actual_permanent_address == expected_permanent_address, f"Expected permanent address to be '{expected_permanent_address}', but got '{actual_permanent_address}'"


    element = driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")

    test_full_name(element)
    test_email(element)
    test_current_address(element)
    test_permanent_address(element)
    print("Tests passed!")

finally:
    time.sleep(2)
    driver.quit()

