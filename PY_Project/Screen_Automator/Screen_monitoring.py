from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

# Path to your WebDriver
PATH = r"D:\Design_model\edgedriver_win64\msedgedriver.exe"

# Setup Edge options
options = Options()

# Initialize WebDriver with options and service
service = Service(executable_path=PATH)
driver = webdriver.Edge(service=service, options=options)

# Define contact_name and online_count at the beginning
contact_name = "Abhay BAC20"  # Replace with the contact's name
online_count = 0  # Initialize online_count before using it

# Define the start time and duration for monitoring
start_time = datetime.now()
monitor_duration = timedelta(hours=1)  # Set the duration you want to monitor

try:
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com")
    
    # Wait for the user to scan the QR code
    print("Please scan the QR code to log in to WhatsApp Web.")
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "._3m_Xw"))
    )

    search_box = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
    )
    search_box.send_keys(contact_name)
    time.sleep(2)  # Wait for the search results to appear

    try:
        search_result = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[@title='{contact_name}']"))
        )
        search_result.click()
    except TimeoutException:
        print(f"Unable to find contact: {contact_name}")

    while datetime.now() - start_time < monitor_duration:
        try:
            # Use the updated XPath for online status
            online_status = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span'))
            )
            status = online_status.text
            if status == "online":
                online_count += 1
                print(f"{contact_name} is online at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"{contact_name} is offline at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        except TimeoutException:
            print(f"Unable to determine {contact_name}'s status at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(10)  # Check every 10 seconds
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

# Print the final message after quitting the driver
print(f"{contact_name} came online {online_count} times.")
