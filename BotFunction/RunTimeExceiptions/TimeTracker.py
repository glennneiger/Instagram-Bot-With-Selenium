import datetime
import time

from BotFunction.BotReferences.BColors import BColors


class TimeTracker:

    @staticmethod
    def sleeping():
        print(BColors.FAIL + "Going To Sleep" + BColors.ENDC)

    @staticmethod
    def waking_up():
        print(BColors.OKGREEN + "Waking Up" + BColors.ENDC)

    @staticmethod
    def sleep_till_tomorrow():
        TimeTracker.sleeping()
        time.sleep(60 * 60 * 24)
        TimeTracker.waking_up()

    @staticmethod
    def check_time():
        current_hour = datetime.datetime.now().hour
        print("Current time: " + current_hour.__str__())
        if current_hour < 5:
            TimeTracker.sleeping()
            time.sleep(60 * 60 * (5 - current_hour))
            TimeTracker.waking_up()
        elif current_hour >= 22:
            TimeTracker.sleeping()
            time.sleep(60 * 60 * (5 + (24 - current_hour)))
            TimeTracker.waking_up()
