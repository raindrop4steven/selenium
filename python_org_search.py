#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Url lists
urls = []
component_results = []
finish_count = 0

# Get url list from local file
with open('url_list.txt', 'r') as url_list:
    for url in url_list.readlines():
        urls.append(url.strip())

print("Total links %d" % len(urls))

driver = webdriver.Firefox()

for url in urls:
    result = [url]

    driver.get(url)

    # Get bread crumb
    try:
        driver.find_element_by_css_selector('span.hidden-all')
    except NoSuchElementException:
        result.append('bread_crumb')
    else:
        pass
    # Get left navigation
    try:
        left_nav = driver.find_element_by_css_selector('div.hidden-all')
    except NoSuchElementException:
        result.append('left_nav')
    else:
        pass
    # Get page selector
    try:
        driver.find_element_by_css_selector('div.technical-azure-selector')
    except NoSuchElementException:
        pass
    else:
        result.append('page_selector')
    # Get right navigation bar
    try:
        right_nav = driver.find_element_by_css_selector('div.documentation-bookmark')
    except NoSuchElementException:
        pass
    else:
        result.append('right_nav')

    line = ','.join(result)
    component_results.append(line)

    finish_count += 1
    print("Finish %d" % finish_count)

driver.close()

# Write results to local file
with open('results.txt', 'a') as out_file:
    for line in component_results:
        out_file.write(line + '\n')

# Finish
print "Done"
