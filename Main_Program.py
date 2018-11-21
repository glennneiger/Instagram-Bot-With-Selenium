from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException

from Info import applicationInfo
from Interface import interfaceControl
from bcolors import bcolors

# todo change
driver = webdriver.Chrome(applicationInfo.CHROME_DRIVER)
number_of_images_liked = 0


def main_program(username, password, hash_tags_number, hash_tags_list):
    try:
        interfaceControl.start_application(driver)
        interfaceControl.sign_into_instagram(driver, username, password)
    except (TimeoutException, NoSuchElementException):
        interfaceControl.go_to_instagram(driver)
        main_program(username, password, hash_tags_number, hash_tags_list)

    n = 0
    while n < applicationInfo.REDO_WHOLE_HASH_TAG_LIST:
        i = 0
        while i < hash_tags_number:
            print(bcolors.OKBLUE + applicationInfo.CURRENT_TAG + hash_tags_list[i] + bcolors.ENDC)
            try:
                interfaceControl.search_hash_tag(driver, hash_tags_list[i])
                interfaceControl.like_images(driver)
                i += 1
                if applicationInfo.RUN_CONTINUOUSLY is False:
                    n += 1
            except (TimeoutException, NoSuchElementException, WebDriverException):
                interfaceControl.go_to_instagram(driver)
                print("Crashed")

    interfaceControl.finished(driver)