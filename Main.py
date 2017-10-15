from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
from random import randint
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# Todo - like blow up people's pictures?
# Todo - what if there is not enough pictures to that hashtag
# Todo - make muliple accounts to log into
# WebDriverException - this exception can pop out anytime chrome is being called and it doesnt talk back

driver = webdriver.Chrome('D:\Important\Web Drivers\chromedriver.exe')

# Instagram Info - pass username, password, and hashtags as arguments or hardcode them here
username = sys.argv[1]
password = sys.argv[2]
hash_tags = sys.argv[3]

# Bot_Info
run_continuously = True  # Change to true if you want it to not stop
number_of_likes_of_hash_tag = 30
redo_whole_hash_tag_list = 10
least_number_of_seconds_per_like = 10
max_number_of_seconds_per_like = 30

hash_tags_list = hash_tags.split(',')
hash_tags_number = len(hash_tags_list)

times_failed_time_out = 0
times_failed_no_such_element = 0
times_failed_time_out_inside_loop = 0
times_failed_no_such_element_inside_loop = 0
number_of_pictures_liked = 0

# Paths, Classes, Text Strings
# These could change if instagram changes the so you will need to edit the class paths
url = "http://www.instagram.com"
logInText = 'Log in'
userNameText = 'username'
passwordText = 'password'
logInButtonPath = "//button[contains(text(),'Log in')]"
searchBarPath = "//input[@class='_avvq0 _o716c']"
firstLinkClass = '_gimca'
firstSearchImagePath = '//div[@class="_mck9w _gvoze _f2mse"]/a'
likeText = 'Like'
nextText = 'Next'
closeButtonPath = "//button[text()='Close']"


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def go_to_instagram():
    print(BColors.HEADER + 'Stage 1: Going To WebSite' + BColors.ENDC)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(20)
    elem = driver.find_element_by_link_text(logInText)
    elem.click()
    time.sleep(5)


def sign_into_instagram():
    print(BColors.HEADER + 'Stage 2: Signing Into Instagram' + BColors.ENDC)
    driver.implicitly_wait(20)
    driver.find_element_by_name(userNameText).send_keys(username)
    driver.find_element_by_name(passwordText).send_keys(password)
    driver.find_element_by_xpath(logInButtonPath).click()


def search_hash_tag(hash_tag):
    print(BColors.HEADER + 'Stage 3: Searching Images With HashTag' + BColors.ENDC)
    driver.implicitly_wait(20)
    input_element = driver.find_element_by_xpath(searchBarPath)
    input_element.send_keys('#'+hash_tag)
    time.sleep(5)
    input_element.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.implicitly_wait(20)
    element = WebDriverWait(driver, 10).until(lambda drive: driver.find_element_by_class_name(firstLinkClass))
    element.click()
    time.sleep(10)


def like_images(hash_tag):
    print(BColors.HEADER + 'Stage 4: Liking Images With Current HashTag' + BColors.ENDC)
    global times_failed_no_such_element_inside_loop
    global number_of_pictures_liked
    global times_failed_time_out_inside_loop

    driver.implicitly_wait(5)
    driver.find_element_by_xpath(firstSearchImagePath).click()
    time.sleep(5)
    print(BColors.OKBLUE + 'Clicked on first image' + BColors.ENDC)
    skipped = False
    i = 0

    while i < number_of_likes_of_hash_tag:
        try:
            driver.implicitly_wait(5)
            element_like = WebDriverWait(driver, 10).until(lambda drive: driver.find_element_by_link_text(likeText))
            element_like.click()
            time.sleep(5)
            number_of_pictures_liked += 1
            print(BColors.OKGREEN + 'Images Liked: ' + str(number_of_pictures_liked) + BColors.ENDC)
        except TimeoutException:
            times_failed_time_out_inside_loop += 1
            print(BColors.WARNING + '--Picture Already Liked It Inside Time Out: ' +
                  str(times_failed_time_out_inside_loop) + BColors.ENDC)
            skipped = True
            i -= 1
        except NoSuchElementException:
            times_failed_no_such_element_inside_loop += 1
            print(BColors.WARNING + '--Picture Already Liked It Inside No Such Element:' +
                  str(times_failed_no_such_element_inside_loop) + BColors.ENDC)
            skipped = True
            i -= 1
        try:
            driver.implicitly_wait(10)
            elem_next = driver.find_element_by_link_text(nextText)
            elem_next.click()
            time.sleep(5)
            driver.implicitly_wait(5)
            if skipped is False:
                time.sleep(randint(least_number_of_seconds_per_like, max_number_of_seconds_per_like))
            else:
                skipped = False
            i += 1
        except TimeoutException:
            times_failed_time_out_inside_loop += 1
            print(BColors.FAIL + '--Failed Timeout Exception Inside Time In: ' + str(times_failed_time_out_inside_loop)
                  + BColors.ENDC)
            driver.implicitly_wait(20)
            driver.get(url)
            time.sleep(20)
            search_hash_tag(hash_tag)
            driver.implicitly_wait(5)
            driver.find_element_by_xpath(firstSearchImagePath).click()
            time.sleep(5)
            print(BColors.OKGREEN + 'Clicked on first image' + BColors.ENDC)
        except NoSuchElementException:
            times_failed_no_such_element_inside_loop += 1
            print(BColors.FAIL + '--Failed No Such Element Inside Time In: ' + str(times_failed_no_such_element) +
                  BColors.ENDC)
            driver.implicitly_wait(20)
            driver.get(url)
            time.sleep(20)
            search_hash_tag(hash_tag)
            driver.implicitly_wait(5)
            driver.find_element_by_xpath(firstSearchImagePath).click()
            time.sleep(5)
            print(BColors.OKGREEN + 'Clicked on first image' + BColors.ENDC)
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_xpath(closeButtonPath).click()
        time.sleep(5)
    except NoSuchElementException:
        driver.implicitly_wait(20)
        driver.get(url)
        time.sleep(20)
    except TimeoutException:
        driver.implicitly_wait(20)
        driver.get(url)
        time.sleep(20)


def finished():
    print(BColors.HEADER + 'Stage 5: Application Finished' + BColors.ENDC)
    driver.quit()


def main(first_time):

    global times_failed_time_out
    global times_failed_no_such_element

    if first_time is True:
        try:
            go_to_instagram()
            sign_into_instagram()
        except TimeoutException:
            times_failed_time_out += 1
            print(BColors.FAIL + '--Failed Outside Time Out: ' + str(times_failed_time_out) + BColors.ENDC)
            driver.implicitly_wait(20)
            driver.get(url)
            time.sleep(20)
            main(True)
        except NoSuchElementException:
            times_failed_time_out += 1
            print(BColors.FAIL + '--Failed Outside Time Out: ' + str(times_failed_no_such_element) + BColors.ENDC)
            driver.implicitly_wait(20)
            driver.get(url)
            time.sleep(20)
            main(True)
    try:
        n = 0
        while n < redo_whole_hash_tag_list:
            i = 0
            while i < hash_tags_number:
                print(BColors.OKBLUE + '--Current Hash Tag: ' + hash_tags_list[i] + BColors.ENDC)
                search_hash_tag(hash_tags_list[i])
                like_images(hash_tags_list[i])
                i += 1
            if run_continuously is False:
                n += 1
    except TimeoutException:
        times_failed_time_out += 1
        print(BColors.FAIL + '--Failed Outside Time Out: ' + str(times_failed_time_out) + BColors.ENDC)
        driver.implicitly_wait(20)
        driver.get(url)
        time.sleep(20)
        main(False)
    except NoSuchElementException:
        times_failed_no_such_element += 1
        print(BColors.FAIL + '--Failed Outside No Such Element: ' + str(times_failed_no_such_element) + BColors.ENDC)
        driver.implicitly_wait(20)
        driver.get(url)
        time.sleep(20)
        main(False)
    finished()

main(True)
