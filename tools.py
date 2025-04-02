"""
A custom library with uselfull stuff to make other codes work
"""

from screeninfo import get_monitors
import os ,sys, threading, time # Python's libraries
from pygame import mixer



def get_screen_resolution() -> tuple:
    """
    Gets the resolution of the primary monitor
    """
    for monitor in get_monitors():
        return monitor.width, monitor.height 
    
def resource_path(relative_path):
    """ Get the absolute path to a resource, accounting for PyInstaller's behavior """
    if getattr(sys, '_MEIPASS', False):  # If running as a PyInstaller bundle
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def shutdown_computer():
    """
    does the funny command
    """
    os.system("shutdown /s /f /t 0")

def get_folder_file(path,format) -> list:
# Initialize an empty list to store .png file names
        png_files = []
        # Loop through the folder
        for file_name in os.listdir(path):
            # Check if the file has a .png extension
            if file_name.endswith(f'.{format}'):
                # Add the file to the list
                png_files.append(os.path.splitext(file_name)[0])
        return png_files

#---Sound Player---#

class __SoundPlayer__:
    def __init__(self):
        self.stop_flag = False
        mixer.init()

    def play_sound(self, file_path):
        """
        Play sound in a loop until stopped.
        """
        self.stop_flag = False
        sound = mixer.Sound(file_path)  # Create a Sound object
        sound.play(loops=-1)  # Play sound in a loop
        while not self.stop_flag:
            time.sleep(0.1)  # Check every 0.1 seconds if the sound should stop
        sound.stop()  # Stop the sound when stop_flag is True
    def stop_sound(self):
        self.stop_flag = True

sound_threads = {}
sound_players = {}

def start_sound(path,number = 1):
    """
    Start the sound in a separate thread.
    """
    if f"sound_thread{number}" not in sound_threads:
        sound_threads[f"sound_thread{number}"] = None
        sound_players[f"sound_player{number}"] = __SoundPlayer__()

    if not sound_threads[f"sound_thread{number}"] or not sound_threads[f"sound_thread{number}"].is_alive():

        sound_threads[f"sound_thread{number}"] = threading.Thread(target=sound_players[f"sound_player{number}"].play_sound, args=(resource_path(path),), daemon=True)
        sound_threads[f"sound_thread{number}"].start()
    else:
        stop_sound(sound_threads[f"sound_thread{number}"])


def stop_sound(number=1):
    """
    Stop the sound and join the thread.
    """
    if f"sound_player{number}" in sound_players:
        sound_players[f"sound_player{number}"].stop_sound()
    if sound_threads.get(f"sound_thread{number}"):
        sound_threads[f"sound_thread{number}"].join()