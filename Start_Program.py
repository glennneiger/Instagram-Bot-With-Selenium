from builtins import len

import Main_Program
from Accounts import accounts

# Instagram_Info
username = accounts.USERNAME
password = accounts.PASSWORD
hash_tags = accounts.HASHTAGS

hash_tags_list = hash_tags.split(',')
hash_tags_number = len(hash_tags_list)


def main():
    Main_Program.main_program(username, password, hash_tags_number, hash_tags_list)


main()
