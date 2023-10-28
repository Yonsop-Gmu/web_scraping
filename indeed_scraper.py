from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to chromedriver.exe
driver_path = 'D:/Tools/Drivers/Chrome/chromedriver.exe'  # Replace with the actual path

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# URL of the Flipp.com page for groceries
url = 'https://flipp.com/en-ca/brossard-qc/item/782781670-metro-weekly-savings?postal_code=J4W1A1'

# Open the webpage
driver.get(url)

try:
    # Simulate user interaction to reveal the element (e.g., clicking on an icon)
    # Modify this part to match the actual website structure
    icon_element = driver.find_element(By.XPATH, 'xpath_to_icon')  # Replace with the actual XPath to the icon
    icon_element.click()

    # Wait for the element to become visible
    wait = WebDriverWait(driver, 10)
    relative_xpath = '//div[contains(@class, "flipp-item-dialog")]/h2/span'
    element = wait.until(EC.presence_of_element_located((By.XPATH, relative_xpath)))

    # Extract and print the data
    item_name = element.text.strip()
    print(f'Item Name: {item_name}')

except Exception as e:
    print(f'Error: {str(e)}')

# Close the WebDriver
driver.quit()
