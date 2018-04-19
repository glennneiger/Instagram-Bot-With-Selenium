from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
from Extras.Accounts import accounts
from Extras.Info import applicationInfo
from Extras.Interface import interfaceControl
from Extras.bcolors import bcolors

driver = webdriver.Chrome(applicationInfo.CHROME_DRIVER)

# Instagram_Info
username = accounts.USERNAME
password = accounts.PASSWORD
hash_tags = accounts.HASH_TAG

hash_tags_list = hash_tags.split(',')
hash_tags_number = len(hash_tags_list)


def main(first_time):

    images_liked = 0

    if first_time is True:
        try:
            interfaceControl.start_application(driver)
            interfaceControl.sign_into_instagram(driver, username, password)
        except (TimeoutException, NoSuchElementException):
            interfaceControl.go_to_instagram(driver)
            main(True)

        n = 0
        while n < applicationInfo.REDO_WHOLE_HASH_TAG_LIST:
            i = 0
            while i < hash_tags_number:
                print(bcolors.OKBLUE + applicationInfo.CURRENT_TAG + hash_tags_list[i] + bcolors.ENDC)
                try:
                    interfaceControl.search_hash_tag(driver, hash_tags_list[i])
                    images_liked = interfaceControl.like_images(driver, images_liked)
                    i += 1
                    if applicationInfo.RUN_CONTINUOUSLY is False:
                        n += 1
                except (TimeoutException, NoSuchElementException, WebDriverException):
                    interfaceControl.go_to_instagram(driver)
                    print("Crashed")

    interfaceControl.finished(driver)

main(True)
