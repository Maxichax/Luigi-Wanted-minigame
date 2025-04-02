# Luigi Wanted minigame

## Description

Luigi wanted is a small game built with Python using the Tkinter library. The objective of the game is to find Luigi among the characters (Wario, Mario, and Yoshi). The game features music, dynamic animation, and even a shutdown function when time runs out (optional).

### Features

- Find Luigi among the bouncing characters.
- Adjustable performance settings (Low, Medium, High) to reduce lag.
- Random restarts after completion.
- Sound effects and background music.
- Optional shutdown when time runs out.

## Installation

Make sure you have Python installed on your system. To install the required packages, run:

```
pip install -r requirements.txt
```

## How to Run

To start the game, simply run the following command:

```
python main.py
```

### Compiling to Executable

To compile the code using PyInstaller, use the following command:

```
pyinstaller main.spec
```

This will generate an executable file in the `dist/` folder.

## Configuration

The game can be customized using the following variables in the `main.py` file:

- `performance`: Adjusts the number of characters on the screen (1 = Low, 2 = Medium, 3 = High).
- `shutdown`: Determines whether the computer will shut down when the timer reaches zero (True = Yes, False = No).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## MIT License

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Small note

I'm also not affiliated in any way with nintendo and I do not own the assets.
