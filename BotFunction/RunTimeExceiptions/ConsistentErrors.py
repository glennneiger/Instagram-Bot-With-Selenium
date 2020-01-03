from BotFunction.BotReferences.BColors import BColors


class ConsistentErrors:

    number_of_consistent_errors = 0

    def reset_tracker(self):
        print("Reset")
        self.number_of_consistent_errors = 0

    def check_tracker(self):
        if self.number_of_consistent_errors >= 3:
            print(BColors.FAIL + "Exit" + BColors.ENDC)
            return True
        return False

    def add_error(self):
        self.number_of_consistent_errors += 1
        print(BColors.WARNING + "An Error: " + self.number_of_consistent_errors.__str__() + BColors.ENDC)
        return self.number_of_consistent_errors
