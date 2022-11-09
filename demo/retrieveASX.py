# Author: Yue Ma
# Data: Dec, 9, 2022
# Midnight QA Task

import typer
import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(
        companyName: str = typer.Option(..., prompt=True)
):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www2.asx.com.au/")

    # Accept Cookie dialog
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()

    # the search bar icon
    magnifierIcon = driver.find_element(By.XPATH, "//*[@id='btn-search']/a")
    # the search bar area
    searchBar = driver.find_element(By.NAME, "search-input")

    actions = ActionChains(driver).move_to_element(magnifierIcon).click(magnifierIcon).click(searchBar) \
        .send_keys(companyName).send_keys(Keys.RETURN).perform()

    print("############################################")
    print("Stage 1: Retrieve the 3th company stock info")
    print("The current page url is " + driver.current_url)
    print("Title is :" + driver.title)

    time.sleep(3)

    # click the entry to enter the selected stock home page
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "asx-code"))).click()

    # print current page URL
    print("The page url: " + driver.current_url)
    print("Title: " + driver.title)

    # wait till price loaded
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "dd[data-v-1b06b642='']"), "$"))

    # get info from 'Last Price / Today's Change'
    lastPrice1 = driver.find_element(By.CSS_SELECTOR, "dd[data-v-1b06b642='']").text.split(" ")[0]
    # todayChange = priceList[1]
    # changeRatio = priceList[2]

    time.sleep(3)

    # get ticker name
    ticker1 = driver.find_element(By.CLASS_NAME, "h2.panel-title").text.split(" peer analysis")[0]

    print("Stock1 ticker: " + ticker1)
    print("Stock1 Last Price: " + lastPrice1)

    # get the PE ratio
    peRatio1 = float(
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > "
                                             "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
                                             "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > "
                                             "div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > "
                                             "div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > "
                                             "tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)").text)

    print("Stock1 PE ratio: " + str(peRatio1))

    time.sleep(3)

    # wait for peer analysis loaded
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "h2.panel-title"), "peer analysis"))

    time.sleep(3)

    # get all four related companies info
    relatedCompany1 = driver.find_element(By.CLASS_NAME, "legend-item.legend-item-lg.legend-item-0").text
    relatedCompany2 = driver.find_element(By.CLASS_NAME, "legend-item.legend-item-lg.legend-item-1").text
    relatedCompany3 = driver.find_element(By.CLASS_NAME, "legend-item.legend-item-lg.legend-item-2").text
    relatedCompany4 = driver.find_element(By.CLASS_NAME, "legend-item.legend-item-lg.legend-item-3").text

    # process to get the ticker
    relatedCompany1Ticker = relatedCompany1.split("\n")[1].split(" ")[0]
    relatedCompany2Ticker = relatedCompany2.split("\n")[1].split(" ")[0]
    relatedCompany3Ticker = relatedCompany3.split("\n")[1].split(" ")[0]
    relatedCompany4Ticker = relatedCompany4.split("\n")[1].split(" ")[0]

    # create an array
    relatedCompanyList1 = [relatedCompany1Ticker, relatedCompany2Ticker, relatedCompany3Ticker, relatedCompany4Ticker]
    print("The related company array is :" + relatedCompanyList1.__str__())

    time.sleep(3)

    # 2) navigates to second company URL
    print()
    print("############################################")
    print("Stage 2: Retrieve the 2nd company stock info")
    driver.get("https://www2.asx.com.au/markets/company/" + relatedCompany2Ticker)
    print("The page url: " + driver.current_url)
    print("Title: " + driver.title)
    time.sleep(8)

    # wait till price loaded
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "dd[data-v-1b06b642='']"), "$"))

    time.sleep(5)
    # get ticker2 name
    ticker2 = driver.find_element(By.CLASS_NAME, "h2.panel-title").text.split(" peer analysis")[0]

    # get ticker2 from 'Last Price / Today's Change'
    lastPrice2 = driver.find_element(By.CSS_SELECTOR, "dd[data-v-1b06b642='']").text.split(" ")[0]
    peRatio2 = float(
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > "
                                             "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
                                             "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > "
                                             "div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > "
                                             "div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > "
                                             "tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)").text)

    print("Stock2 ticker: " + ticker2)
    print("Stock2 Last Price: " + lastPrice2)
    print("Stock2 PE ratio: " + str(peRatio2))

    time.sleep(3)

    # 3) navigates to 3rd company URL
    print()
    print("############################################")
    print("Stage 3: Retrieve the 3th company stock info")
    driver.get("https://www2.asx.com.au/markets/company/" + relatedCompany3Ticker)
    print("The page url: " + driver.current_url)
    print("Title: " + driver.title)
    time.sleep(8)

    # wait till price loaded
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "dd[data-v-1b06b642='']"), "$"))

    time.sleep(5)
    # get ticker3 name
    ticker3 = driver.find_element(By.CLASS_NAME, "h2.panel-title").text.split(" peer analysis")[0]

    # get ticker3 from 'Last Price / Today's Change'
    lastPrice3 = driver.find_element(By.CSS_SELECTOR, "dd[data-v-1b06b642='']").text.split(" ")[0]

    peRatio3 = float(
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > "
                                             "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
                                             "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > "
                                             "div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > "
                                             "div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > "
                                             "tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)").text)

    print("Stock3 ticker: " + ticker3)
    print("Stock3 Last Price: " + lastPrice3)
    print("Stock3 PE ratio: " + str(peRatio3))

    # Stage 4 navigates to 3rd company URL
    time.sleep(3)
    print()
    print("############################################")
    print("Stage 4: Retrieve the 4th company stock info")
    driver.get("https://www2.asx.com.au/markets/company/" + relatedCompany4Ticker)
    print("The page url: " + driver.current_url)
    print("Title: " + driver.title)
    time.sleep(8)

    # wait till price loaded
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "dd[data-v-1b06b642='']"), "$"))

    time.sleep(5)
    # get ticker4 name
    ticker4 = driver.find_element(By.CLASS_NAME, "h2.panel-title").text.split(" peer analysis")[0]

    # get ticker4 from 'Last Price / Today's Change'
    lastPrice4 = driver.find_element(By.CSS_SELECTOR, "dd[data-v-1b06b642='']").text.split(" ")[0]
    time.sleep(3)

    peRatio4 = float(
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > "
                                             "div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
                                             "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > "
                                             "div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > "
                                             "div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > "
                                             "tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)").text)

    print("Stock4 ticker: " + ticker4)
    print("Stock4 Last Price: " + lastPrice4)
    print("Stock4 PE ratio: " + str(peRatio4))

    relatedCompanyDic = {
        ticker1: peRatio1,
        ticker2: peRatio2,
        ticker3: peRatio3,
        ticker4: peRatio4,
    }

    lowestRatio = min(relatedCompanyDic, key=relatedCompanyDic.get)
    print(relatedCompanyDic)
    print("Recommended purchased is " + lowestRatio)

    stockData1 = [ticker1, lastPrice1, peRatio1, "NO"]
    stockData2 = [ticker2, lastPrice2, peRatio2, "NO"]
    stockData3 = [ticker3, lastPrice3, peRatio3, "NO"]
    stockData4 = [ticker4, lastPrice4, peRatio4, "NO"]
    stockArray = [stockData1, stockData2, stockData3, stockData4]

    for stock in stockArray:
        if stock[0] == lowestRatio:
            stock[3] = "YES"

    # Define the structure of the data
    listing_header = ['ticker', 'price', 'ratio', 'recommended']
    # Open a new CSV file
    with open('stock.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(listing_header)
        writer.writerow(stockData1)
        writer.writerow(stockData2)
        writer.writerow(stockData3)
        writer.writerow(stockData4)

    print("##########################")
    print("Thank you guys for having me practice such interesting task and making me continuously improving! :-)")

    driver.close()


if __name__ == "__main__":
    typer.run(main)
