from random import seed
from random import randint
from BotFunction.BotReferences.ApplicationInfo import ApplicationInfo


class TimeManager:

    @staticmethod
    def get_load_time():
        return float(ApplicationInfo.PAGE_LOAD_TIMEOUT)

    @staticmethod
    def get_stall_time():
        return float(TimeManager.get_number(ApplicationInfo.MIN_SECONDS_PER_LIKE, ApplicationInfo.MAX_SECONDS_PER_LIKE))

    @staticmethod
    def get_long_time():
        return 5

    @staticmethod
    def get_number(lowest, highest):
        seed(1)
        return randint(lowest, highest)
