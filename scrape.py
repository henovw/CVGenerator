from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class jobInfo:
    def __init__(self, jobDescription,companyDescription, title):
        self.jobDescription = jobDescription
        self.companyDescription = companyDescription
        self.title = title


def getInfo(link):
    driver = webdriver.Chrome()
    driver.get(link)


    ## FOR JOB INFO 
    # x button 
    xbutton = driver.find_elements(By.CLASS_NAME,'modal__dismiss')
    for element in xbutton:
        if element.aria_role == "button":
            element.click()
            
    # job title 
    t = driver.find_element(By.CLASS_NAME, 'top-card-layout__title').text
   
    # show more
    driver.find_element(By.CLASS_NAME, 'show-more-less-html__button').click()

    # get description
    jobdesc = driver.find_element(By.CLASS_NAME, "show-more-less-html__markup").text
    
    
    ## FOR COMPANY INFO 
    # scroll to top
    driver.execute_script("window.scrollBy(0, -10000)")
        
    # company page
    comp = driver.find_element(By.CLASS_NAME, 'topcard__org-name-link.topcard__flavor--black-link')
    cn = comp.text
    comp.click()

    # switch to new tab
    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])
    
    # x button 
    xbutton = driver.find_elements(By.CLASS_NAME,'modal__dismiss')
    for element in xbutton:
        if element.aria_role == "button":
            element.click()
    
    # get description
    compdesc = driver.find_element(By.XPATH, '//p[@data-test-id="about-us__description"]').text
    
    driver.quit()

    return jobInfo(jobdesc, compdesc, t + cn)
