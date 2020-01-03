from builtins import len

from selenium import webdriver
from BotFunction import Main_Program

# Instagram_Info - Edit this for personal info
username = "USERNAME"
password = "PASSWORD"
hash_tags = "HASH_TAGS,SEPARATED,BY,COMMAS"

web_driver = webdriver.Chrome('/web/driver/path')

hash_tags_list = hash_tags.split(',')
hash_tags_number = len(hash_tags_list)


def main():
    Main_Program.main_program(username, password, hash_tags_number, hash_tags_list, web_driver)


main()
