from selenium import webdriver #connect python with webbrowser-chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#the local user will have to update these fields with their credentials
email1 = "waldmannevan@knights.ucf.edu" #email
pass1 = "not this time" # password

# Login to Linked in :
def login(email, password1):
    username = driver.find_element_by_id("login-email")
    username.send_keys(email)
    password = driver.find_element_by_id("login-password")
    password.send_keys(password1)
    driver.find_element_by_id("login-submit").click()
    print("successfully logged in")

#launch url and log in
url = "http://linkedin.com/"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
driver.get(url)
login(email1, pass1)

# open address file
file = open("address.txt", "r")

#start looping through database of people to connect
for line in file:
    linkedinlink = line # linkedin profile address.
    driver.get(linkedinlink)
    try:
        # driver.save_screenshot("test1.jpg")
        button1 = driver.find_element(By.CLASS_NAME, 'pv-s-profile-actions--connect')
        button1.click()
        # driver.save_screenshot("test2.jpg")
        button2 = driver.find_element(By.CLASS_NAME, 'button-primary-large')
        # button2.click()  this will send the invitation..
        print("connected the two people! ")
    except Exception as ex:
        print("ERROR: the two people were connected already")
        print("NOT CONNECTED TO {}".format(line))
