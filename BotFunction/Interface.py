import time
from random import randint

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from BotFunction.BotReferences.ApplicationInfo import ApplicationInfo
from BotFunction.BotReferences.BColors import BColors


class InterfaceControl:

    from BotFunction.TimeManager import TimeManager
    time_manager = TimeManager()

    @staticmethod
    def remove_notification_prompt(driver):
        try:
            time.sleep(InterfaceControl.time_manager.get_load_time())
            driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
            driver.find_element_by_xpath(ApplicationInfo.CLOSE_BUTTON_PATH).click()
        except (TimeoutException, NoSuchElementException, WebDriverException):
            print("No X")

    @staticmethod
    def start_application(driver):
        print(BColors.HEADER + ApplicationInfo.STAGE0_KEYWORD + BColors.ENDC)

        driver.set_page_load_timeout(ApplicationInfo.PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        driver.get(ApplicationInfo.URL)
        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        elem = driver.find_element_by_link_text(ApplicationInfo.LOG_IN_TEXT)
        elem.click()

        time.sleep(InterfaceControl.time_manager.get_load_time())

    @staticmethod
    def sign_into_instagram(driver, username, password):
        print(BColors.HEADER + ApplicationInfo.STAGE2_KEYWORD + BColors.ENDC)

        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        driver.find_element_by_name(ApplicationInfo.USERNAME_TEXT).send_keys(username)
        driver.find_element_by_name(ApplicationInfo.PASSWORD_TEXT).send_keys(password)
        driver.find_element_by_xpath(ApplicationInfo.LOG_IN_BUTTON_PATH).click()

        time.sleep(InterfaceControl.time_manager.get_load_time())
        InterfaceControl.remove_notification_prompt(driver)

    @staticmethod
    def go_to_instagram(driver):
        print(BColors.HEADER + ApplicationInfo.STAGE2_KEYWORD + BColors.ENDC)
        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        driver.get(ApplicationInfo.URL)

        time.sleep(InterfaceControl.time_manager.get_load_time())

        InterfaceControl.remove_notification_prompt(driver)

    @staticmethod
    def search_hash_tag(driver, hash_tag):
        print(BColors.HEADER + ApplicationInfo.STAGE3_KEYWORD + BColors.ENDC)

        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        input_element = driver.find_element_by_xpath(ApplicationInfo.SEARCH_BAR_PATH)
        input_element.send_keys('#' + hash_tag)

        time.sleep(InterfaceControl.time_manager.get_load_time())

        input_element.send_keys(Keys.ENTER)

        time.sleep(InterfaceControl.time_manager.get_load_time())

        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        element = WebDriverWait(driver, ApplicationInfo.IMPLICIT_WAIT).until(lambda drive: driver.find_element_by_class_name(ApplicationInfo.FIRST_LINK_CLASS))
        element.click()

        time.sleep(InterfaceControl.time_manager.get_load_time())

    @staticmethod
    def like_images(driver, total_number_of_images_liked, error_tracker):
        print(BColors.HEADER + ApplicationInfo.STAGE4_KEYWORD + BColors.ENDC)

        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        driver.execute_script("window.scrollTo(0, (document.body.scrollHeight/2));")

        time.sleep(InterfaceControl.time_manager.get_load_time())

        driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
        driver.find_element_by_xpath(ApplicationInfo.FIRST_SEARCH_IMAGE_PATH).click()

        time.sleep(InterfaceControl.time_manager.get_stall_time())

        print('Clicked on first image')
        tracker_images_liked = 0

        while tracker_images_liked < ApplicationInfo.NUMBER_OF_LIKES_PER_HASH_TAG:
            try:
                print("Liking Image")
                driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
                like_button = driver.find_elements_by_xpath(ApplicationInfo.LIKE_BUTTON_XPATH)[0]
                like_button.click()
                total_number_of_images_liked += 1
                print(BColors.BOLD + "Liked Image: " + BColors.ENDC + BColors.OKGREEN + str(total_number_of_images_liked) + BColors.ENDC)
            except (NoSuchElementException, IndexError):
                error_tracker.add_error()
                break

            time.sleep(InterfaceControl.time_manager.get_load_time())

            try:
                print("Next Image")
                driver.implicitly_wait(ApplicationInfo.IMPLICIT_WAIT)
                elem_next = driver.find_element_by_link_text(ApplicationInfo.NEXT_TEXT)
                elem_next.click()
                error_tracker.reset_tracker()
            except (NoSuchElementException, IndexError):
                error_tracker.add_error()
                break

            time.sleep(InterfaceControl.time_manager.get_stall_time())

            tracker_images_liked += 1

    @staticmethod
    def finished(driver):
        print(BColors.HEADER + 'Stage 5: Application Finished' + BColors.ENDC)
        driver.quit()
