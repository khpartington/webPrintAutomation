import pyautogui
import argparse
import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Set up file to print
parser = argparse.ArgumentParser(description="Process filename for print.")
parser.add_argument('printer_location', type=str, help="The printer location")
parser.add_argument('filename', type=str, help="The name of the file to be printed")
args = parser.parse_args()
printer = args.printer_location
filename = args.filename


if printer == 'null':
    root= tk.Tk()
    root.withdraw()

    printer = None
    while not printer:
        printer = simpledialog.askstring("Input", "Please enter Printer Name:")
        if not printer:
            print("No input provided. Try again.")

# Initialize the Edge WebDriver
service = Service(executable_path=r"C:\Users\Kevin\AppData\Local\Programs\Python\Python312\Scripts\webprint_automation\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Open Webprint
driver.get("https://webprint.pfw.edu/app?service=page/Home")

# Wait for the page to load
time.sleep(2)

# Find Username Input Box
search_box = driver.find_element(By.NAME, "inputUsername")
search_box.send_keys("partkh01")

# Find Password Input Box & Login
search_box = driver.find_element(By.NAME, "inputPassword")
search_box.send_keys("Khp.1020", Keys.RETURN)

# Wait for page to load
time.sleep(1)

# Go to Web Print Submission Page 
search_button = driver.find_element(By.LINK_TEXT, "Web Print")
search_button.click()

# Click Button - "Submit a Job"
search_button = driver.find_element(By.LINK_TEXT, "Submit a Job »")
search_button.click()

# Enter Printer Name
search_box = driver.find_element(By.NAME, "$TextField")
search_box.send_keys(printer, Keys.RETURN)

# Click Button - "Print Options"
search_button = driver.find_element(By.NAME, "$Submit$1")
search_button.click()

# CLick Button - "Upload Documents"
search_button = driver.find_element(By.NAME, "$Submit")
search_button.click()

# CLick Button - "Upload from computer"
search_button = driver.find_element(By.ID, "upload-from")
search_button.click()

# Wait for file explorer window to appear
time.sleep(1)

# Enter file name into file slot
pyautogui.write(filename)
pyautogui.press('enter')

# Click Button - "Upload & Complete"
search_button = driver.find_element(By.ID, "upload")
search_button.click()

# Wait to see the results
time.sleep(3)

# Close the browser
driver.quit()
