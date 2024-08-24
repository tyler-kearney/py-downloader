import tkinter as tk
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def download_file(url):
    driver = webdriver.Chrome('/Users/tylerkearney/Documents/chromedriver-mac-arm64/chromedriver') 
    # Eventually make a way for the user to set the path to their own web driver
    driver.get(url)
    
    # Find the download button
    download_btn = driver.find_element(By.XPATH, "//button[text()='Download']")
    download_btn.click()
    
    driver.quit()
    
def start_download():
    url = url_entry.get()
    download_file(url)
    
# Create the window
window = tk.Tk()
window.title('PyDownloader')

# Create a label and entry for the URL
url_label = tk.Label(window, text="Enter URL: ")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

# Create button to start the download
download_btn = tk.Button(window, text='Download', command=start_download)
download_btn.pack()

window.mainloop()