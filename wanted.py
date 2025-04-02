"""
The wanted minigame were you need to find luigi made with tkinter
"""
import tkinter as tk
from PIL import Image, ImageTk
import random
from ctypes import windll
from tools import get_screen_resolution,resource_path,start_sound,stop_sound,shutdown_computer,get_folder_file
from time import sleep

class __Wanted__:
    def __init__(self, root):
        self.root = root
        self.root.title("Luigi Bouncing")

        # Canvas dimensions
        self.resolution = get_screen_resolution()
        self.canvas_width = self.resolution[0]
        self.canvas_height = self.resolution[1]

            # Make the window transparent
        root.overrideredirect(True)     # Remove the title bar and borders
        root.attributes("-transparentcolor", "gray3") # Makes everything that's gray3 transparent
        root.attributes("-topmost", True)   # Keep it above other windows
        windll.shcore.SetProcessDpiAwareness(1)     # Fix for blurry window on high DPI screens (Windows specific)

                # Create canvas
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height,highlightthickness=0,bg="gray3")
        self.canvas.pack()

        self.png_file = get_folder_file(resource_path("Media"),"png")
        self.tk_image = {}
        # Load the images using Pillow
        for image in self.png_file:
            self.img_temp = Image.open(resource_path(f"Media/{image}.png")) # Loads the images using Pillow
            self.tk_image[image] = ImageTk.PhotoImage(self.img_temp)    # Converts them into tk files

        # List to store details for all characters images
        self.characters = []

        # Create multiple characters images
        for _ in range(perf):
            # Random starting position
            x,y = random.randint(35, self.canvas_width - 35) , random.randint(50, self.canvas_height - 50)

            # Random initial velocity
            dx = random.choice([-5, 5])
            dy = random.choice([-5, 5])

            # Add characters to canvas and store its details
            image_id = self.canvas.create_image(x, y, image=random.choice([self.tk_image['wario'],self.tk_image['mario'],self.tk_image['yoshi']]),tags='not_luigi')
            self.characters.append({"id": image_id, "dx": dx, "dy": dy})
            if random.randint(1,80) == 1:
                image_id = self.canvas.create_image(x, y, image=self.tk_image['warioGreen'],tags='not_luigi')
                self.characters.append({"id": image_id, "dx": dx, "dy": dy})
        self.canvas.tag_bind("not_luigi", "<Button-1>", self.wrong_choice)

    #----------- Creates Luigi---------------

        # Random initial velocity
        dx = random.choice([-5, 5])
        dy = random.choice([-5, 5])

        # Add Luigi to canvas and store its details
        image_id = self.canvas.create_image(random.randint(35, self.canvas_width - 35), random.randint(50, self.canvas_height - 50), image=self.tk_image['luigi'], tags="luigi")
        self.characters.append({"id": image_id, "dx": random.choice([-5, 5]), "dy": random.choice([-5, 5])})
        # Bind a click event to Luigi
        self.canvas.tag_bind("luigi", "<Button-1>", self.close_program)

        self.timer = 0
        self.canvaDiv2 = self.canvas_width // 2
        self.canvaDiv22 = self.canvas_height // 2
        self.i = 10
        self.number_id = self.canvas.create_image(self.canvaDiv2, 110, image=self.tk_image['10'])
        self.findlogoCanva = self.canvas.create_image(self.canvaDiv2, self.canvaDiv22, image=self.tk_image['findLuigi'])
        self.findologo = True
        self.wrong = False

        # Start Music
        start_sound("Media/Wanted_music.mp3")
        # Start the animation loop
        self.moving_loop()
        
        

    def moving_loop(self):
        """
        loop to make the characters move on screen
        """
        for characters in self.characters:
            # Get current position of character
            coords = self.canvas.coords(characters["id"])
            
            # Move character
            self.canvas.move(characters["id"], characters["dx"], characters["dy"])

            # Bounce on edges
            if coords[0] <= 25 or coords[0] >= self.canvas_width-25:  # Left or right edge
                self.canvas.move(characters["id"], -(characters["dx"]*3), characters["dy"])
                characters["dx"] = -characters["dx"]
            if coords[1] <= 35 or coords[1] >= self.canvas_height-35:  # Top or bottom edge
                self.canvas.move(characters["id"], characters["dx"], -(characters["dy"]*3))
                characters["dy"] = -characters["dy"]
        self.timer += 1
        #checks if the wrong character is pressed
        if self.wrong == True:
            self.wrong = False
            self.i -= 2
            #check lose condition
            if self.i <= 0:
                print("Time's up!")
                stop_sound()
                self.canvas.create_image(self.canvaDiv2, self.canvaDiv22, image=self.tk_image['timesUp'])
                start_sound("Media/byebye.mp3")
        #Make the timer
        if self.timer == 30:
            if self.findologo == True:
                self.canvas.delete(self.findlogoCanva)
                self.findologo = False
            self.canvas.delete(self.number_id)
            self.i -= 1
            self.number_id = eval(f"self.canvas.create_image(self.canvaDiv2, 110, image=self.tk_image['{self.i}'])")
            self.timer = 0
            if self.i <= 0:
                print("Time's up!")
                stop_sound()
                self.canvas.create_image(self.canvaDiv2, self.canvaDiv22, image=self.tk_image['timesUp'])
                start_sound("Media/byebye.mp3",2)
                if shut == True:
                    shutdown_computer()
                self.root.destroy()
                sleep(0.80)
                stop_sound(2)
                
        # Schedule the next frame
        self.root.after(25, self.moving_loop)

    def close_program(self, event):
        """Closes the program when any Luigi is clicked."""
        print(f"Luigi clicked at position: ({event.x}, {event.y}) - Exiting program.")
        stop_sound()
        start_sound('Media/win.mp3',2)
        self.root.destroy()
        sleep(0.72)
        stop_sound(2)

    def wrong_choice(self, event):
        """Removes 2 seconds on the timer"""
        start_sound('Media/fail.mp3',2)
        sleep(0.5)
        stop_sound(2)
        self.wrong = True



def play_wanted(performance = 2,shutdown = False):
    """_summary_

    Args:
        performance (int, optional): the number of things on screen 1-low 2-Medium 3-High. Defaults to 2.
        shutdown (bool, optional): if lossing shutdown the computer False-no True-yes. Defaults to False.
    """
    # makes the performance and shutdown global
    global perf
    if performance == 3:
        perf = 100
    elif performance == 2:
        perf = 60
    else:
        perf = 35
        
    global shut
    if shutdown == True:
        shut = True
    else:
        shut = False
    # Create the main window
    root = tk.Tk()

    app = __Wanted__(root)

    # Run the Tkinter event loop
    root.mainloop()
    
