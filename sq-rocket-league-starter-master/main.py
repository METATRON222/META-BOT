# This file is for strategy

from util.objects import *
from util.routines import *


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        # self.set_intent(drive(2300))
        self.set_intent(short_shot(self.foe_goal.location))
        print("shooting")