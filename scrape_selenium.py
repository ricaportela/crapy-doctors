#!/usr/bin/env python
# coding: utf-8

import time
import requests
import sys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def connectFirefox():
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    print("Firefox Headless Browser Invoked")
    return driver

driver = connectFirefox()

driver.get("https://www.doctoralia.com.br/")

element = driver.find_element_by_name("q")

element.clear()

element.send_keys("Ginecologista")

element = driver.find_element_by_name("loc")

element.clear()

element.send_keys("São Paulo, SP")

button = driver.find_element(By.XPATH, '//button')

button.click()

doutor_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/ul/li[1]/div[1]/div/div/div[1]/div[1]/div[2]/h3/a/span')

doutor_link.click()

mostrar_telefone = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/main/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/button')

mostrar_telefone = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,  '/html/body/div[1]/div[4]/main/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/button')))

mostrar_telefone.click()

telefone = driver.find_element_by_xpath('/html/body/div[1]/div[4]/main/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/a/b')

telefone.text




