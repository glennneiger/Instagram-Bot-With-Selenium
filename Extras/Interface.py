import time
from random import randint

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from Extras.Info import applicationInfo
from Extras import bcolors

import Main


class interfaceControl:

    ####################################################################################################################
    # OTHER METHODS
    ####################################################################################################################

    def pop(message):
        print(message)

    ####################################################################################################################
    # INSTAGRAM METHODS
    ####################################################################################################################

    def go_to_instagram(driver):
        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        driver.get(applicationInfo.URL)
        time.sleep(applicationInfo.SLEEP_TIME)
        interfaceControl.check_for_x(driver)

    def check_for_x(driver):
        try:
            driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
            driver.find_element_by_xpath(applicationInfo.CLOSE_BUTTON_PATH).click()
            time.sleep(applicationInfo.SLEEP_TIME)
            driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
            driver.find_element_by_xpath(applicationInfo.CLOSE_BUTTON_PATH).click()
        except (TimeoutException, NoSuchElementException, WebDriverException):
            print("No X")

    def start_application(driver):
        print(bcolors.HEADER + applicationInfo.STAGE1_KEYWORD + bcolors.ENDC)

        driver.set_page_load_timeout(applicationInfo.PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        driver.get(applicationInfo.URL)
        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        elem = driver.find_element_by_link_text(applicationInfo.LOG_IN_TEXT)
        elem.click()
        time.sleep(applicationInfo.SLEEP_TIME)

    def sign_into_instagram(driver, username, password):
        print(bcolors.HEADER + applicationInfo.STAGE2_KEYWORD + bcolors.ENDC)

        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        driver.find_element_by_name(applicationInfo.USERNAME_TEXT).send_keys(username)
        driver.find_element_by_name(applicationInfo.PASSWORD_TEXT).send_keys(password)
        driver.find_element_by_xpath(applicationInfo.LOG_IN_BUTTON_PATH).click()
        time.sleep(applicationInfo.SLEEP_TIME)
        interfaceControl.check_for_x(driver)

    def search_hash_tag(driver, hash_tag):
        print(bcolors.HEADER + applicationInfo.STAGE3_KEYWORD + bcolors.ENDC)

        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        input_element = driver.find_element_by_xpath(applicationInfo.SEARCH_BAR_PATH)
        input_element.send_keys('#' + hash_tag)
        time.sleep(applicationInfo.SLEEP_TIME)
        input_element.send_keys(Keys.ENTER)
        time.sleep(applicationInfo.SLEEP_TIME)
        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        element = WebDriverWait(driver, applicationInfo.IMPLICIT_WAIT).until(lambda drive: driver.find_element_by_class_name(applicationInfo.FIRST_LINK_CLASS))
        element.click()
        time.sleep(applicationInfo.SLEEP_TIME)

    def like_images(driver):
        print(bcolors.HEADER + applicationInfo.STAGE4_KEYWORD + bcolors.ENDC)

        # driver.execute_script("document.body.style.zoom='50%'")
        # driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL, Keys.SUBTRACT);

        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        driver.execute_script("window.scrollTo(0, (document.body.scrollHeight/2));")
        time.sleep(applicationInfo.SLEEP_TIME)

        driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
        driver.find_element_by_xpath(applicationInfo.FIRST_SEARCH_IMAGE_PATH).click()
        time.sleep(applicationInfo.SLEEP_TIME)
        print(bcolors.OKBLUE + 'Clicked on first image' + bcolors.ENDC)
        skipped = False
        i = 0

        while i < applicationInfo.NUMBER_OF_LIKES_PER_HASH_TAG:
            driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
            try:
                print("Liking Image")
                like_button = driver.find_elements_by_xpath(applicationInfo.LIKE_BUTTON_XPATH)[0]
                like_button.click()

            except (NoSuchElementException, IndexError):
                break

            Main.number_of_images_liked += 1
            print("Liked Image: " + str(Main.number_of_images_liked))
            time.sleep(applicationInfo.SLEEP_TIME)
            driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
            elem_next = driver.find_element_by_link_text(applicationInfo.NEXT_TEXT)
            elem_next.click()
            time.sleep(applicationInfo.SLEEP_TIME)
            driver.implicitly_wait(applicationInfo.IMPLICIT_WAIT)
            if skipped is False:
                time.sleep(randint(applicationInfo.MIN_SECONDS_PER_LIKE, applicationInfo.MAX_SECONDS_PER_LIKE))
            else:
                skipped = False
            i += 1

    def finished(driver):
        print(bcolors.HEADER + 'Stage 5: Application Finished' + bcolors.ENDC)
        driver.quit()