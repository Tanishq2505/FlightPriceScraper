from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time, threading
from decimal import Decimal
from re import sub
import smtplib

driver = webdriver.Chrome(ChromeDriverManager().install())


lowest_price = 10000

def cheapest_flight():
    driver.get("https://www.makemytrip.com/flight/search?tripType=O&itinerary=JAI-MAA-20/11/2020&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1603553591650&forwardFlowRequired=true&mpo=")
    nm = driver.find_elements_by_xpath('//span[@class="airways-name "]')[0].text
    driver.implicitly_wait(1)
    ac1 = driver.find_elements_by_xpath('//span[@class="actual-price"]')[0].text
    driver.implicitly_wait(1)
    ac = Decimal(sub(r'[^\d.]', '', ac1))
    return nm,ac
    
# def get_user_input():
#     u_name = input("Enter preferred flight name: ")
#     u_price = Decimal(input("Enter price: "))
#     return u_name,u_price



def infinite_loop():
    global lowest_price
    name,price = cheapest_flight()
    lowest_flight_name = ""
    print(lowest_price)
    if(price < lowest_price):
        lowest_price = price
        lowest_flight_name = name
        print(lowest_flight_name)
        print(lowest_price)
        sendemail(lowest_flight_name, lowest_price)
    print(name)
    print(price)
    threading.Timer(144000, infinite_loop).start()
    # got_name, got_price = get_user_input()

def sendemail(flight_name,flight_price):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("night.r3d29.6.2000@gmail.com","UW9mey7#")
    message = f"Flight prices dropeed! Flight name {flight_name} and flight price {flight_price}"
    s.sendmail("night.r3d25.5@gmail.com","tanishqa89@gmail.com",message)
    s.quit()


cheapest_flight()
infinite_loop()