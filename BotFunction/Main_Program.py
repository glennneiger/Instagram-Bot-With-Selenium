from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium import webdriver

from BotFunction.BotReferences.ApplicationInfo import ApplicationInfo
from BotFunction.Interface import InterfaceControl
from BotFunction.BotReferences.BColors import BColors

total_number_of_images_liked = 0


def main_program(username, password, hash_tags_number, hash_tags_list, web_driver):

    print("\n" +
          BColors.BOLD + BColors.OKBLUE + username + BColors.ENDC
          + "\n")

    from BotFunction.RunTimeExceiptions.ConsistentErrors import ConsistentErrors
    error_tracker = ConsistentErrors()

    from BotFunction.RunTimeExceiptions.TimeTracker import TimeTracker
    time_tracker = TimeTracker()

    try:
        InterfaceControl.start_application(web_driver)
        InterfaceControl.sign_into_instagram(web_driver, username, password)
    except (TimeoutException, NoSuchElementException):
        main_program(username, password, hash_tags_number, hash_tags_list)

    number_of_times_to_read_through_list = 0  # 0 = infinite
    while number_of_times_to_read_through_list < ApplicationInfo.REDO_WHOLE_HASH_TAG_LIST:

        index_of_hash_tag_array = 0
        while index_of_hash_tag_array < hash_tags_number:

            print(BColors.BOLD + username + ": " + BColors.ENDC + BColors.OKBLUE + hash_tags_list[index_of_hash_tag_array] + BColors.ENDC)

            try:
                InterfaceControl.search_hash_tag(web_driver, hash_tags_list[index_of_hash_tag_array])
                InterfaceControl.like_images(web_driver, total_number_of_images_liked, error_tracker)

                if error_tracker.check_tracker():
                    break

                InterfaceControl.go_to_instagram(web_driver)

                index_of_hash_tag_array += 1
                if index_of_hash_tag_array >= len(hash_tags_list):
                    index_of_hash_tag_array = 0

                if ApplicationInfo.RUN_CONTINUOUSLY is False:
                    number_of_times_to_read_through_list += 1

            except (TimeoutException, NoSuchElementException, WebDriverException):
                error_tracker.add_error()
                if error_tracker.check_tracker():
                    break
                InterfaceControl.go_to_instagram(web_driver)

            time_tracker.check_time()

        # Deciding between this or break and ending the program
        if error_tracker.check_tracker():
            from BotFunction.RunTimeExceiptions.TimeTracker import TimeTracker
            TimeTracker.sleep_till_tomorrow()

    # InterfaceControl.finished(driver)
    print("Application Finished")
