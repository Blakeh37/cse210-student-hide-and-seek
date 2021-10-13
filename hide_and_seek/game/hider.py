import random

class Hider:

    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance =[0, 0]

    def get_hint(self):
        if self.distance[-1] == 0:
            message = "\nYou found me!"
        elif self.distance[-1] < self.distance[-2]:
            message = "\nGetting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            message = "\nGetting colder!"
        return message

    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
        