import time
from wanted import play_wanted
from random import randint

# Because it's tkinter it uses a lot of cpu an does not multi thread so it can be laggy so you can change the performance setting in the config.txt.
# it will only affect the number of characters on screen and so the difficulty
performance = 2   # 1-Low   2-Medium   3-High

# will the program shutdown the computer or not if the timer reaches 0
shutdown = False  # -True will shutdown   -False will not


play_wanted(performance,shutdown) # starts the game directly
while True:
    time.sleep(randint(60,3600)) # wait a random amount until it restarts (default 1min to 1hour)
    play_wanted(performance,shutdown)