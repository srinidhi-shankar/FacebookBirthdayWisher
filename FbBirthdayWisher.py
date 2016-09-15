from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time
import sys

#Options for the Google Chrome Browser 
chrome_options = Options()

#Path to Chrome's User Data Directory. Among Other things, User Data Directory contains Profile data.
chrome_options.add_argument("--user-data-dir=C:\\Users\\username\\AppData\\Local\\Google\\Chrome\\User Data")

#When you have multiple Profiles, Specify the User Profile with which Chrome has to be opened.
#Default Profile is selected when nothing is specified
chrome_options.add_argument("--profile-directory=Profile 2")
driver = webdriver.Chrome(chrome_options=chrome_options)

#Use the driver to open this URL.
#Inorder to directly go to the following URL without being directed to the login page, your FB credentials has to be saved in your Profile
driver.get('https://www.facebook.com/events/birthdays')

#Array of birthday wishes
wishes = ["Happy Birthday! :)", "Happy Birthday! Wish you many more happy returns of the day! :)", 
"Happy Birthday. Wishing you more glorious and wonderful years ahead! :)","Have a wonderful happy, healthy birthday and many more to come. Happy Birthday! :)"]

#OR

#Simple birthday wish
wishes_simple = ["Happy Birthday! :)"]

try:
	#Get all the textarea elements in the page. FB displays textboxes for people whose birthdays were yesterday or is today. 
	birthdayboxes = driver.find_elements_by_tag_name('textarea')
	for birthdaybox in birthdayboxes:
		#Send Random birthday wishes. Depending on the kind of 'birthday wish' you want for people, use wishes or wishes_simple array  
		birthdaybox.send_keys(wishes[random.randint(0, len(wishes_simple)-1)])
		birthdaybox.send_keys(Keys.ENTER)
		#Sleep will wait for 2 secs afetr wishing a single person.
		time.sleep(2)
except:
    print 'error!'
    time.sleep(5)
    driver.close()
    sys.exit()

#Print Success message and close the driver
print "Done! Wished Everyone."
time.sleep(5)
driver.close()
sys.exit()
