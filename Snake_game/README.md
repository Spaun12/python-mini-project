<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Snake_game

Addition functionality added by Michael Connell
1. Directional Movement Control
The updated logic prevents the snake from immediately reversing direction, which is a common cause of issues in snake games. By adding checks that ensure the snake cannot move in the opposite direction it's currently moving (unless it's moving straight), we avoid the scenario where the snake collides with itself unexpectedly, leading to a potential game freeze or abrupt game over.

2. Game Over Screen Loop
The game over logic has been revised to handle user input more effectively. Previously, if the game ended (game_close = True), the game would show the game over screen and wait for the user to either quit or restart the game. This loop now properly captures and reacts to key presses, ensuring the game doesn't freeze waiting for input and that the transition from game over back to gameplay (or exiting) is seamless.

3. Improved Event Handling
By ensuring all events are properly handled within the game loop, especially the pygame.QUIT event, the game can gracefully handle closure requests (e.g., clicking the window's close button). Proper event handling is crucial for preventing the game window from becoming unresponsive or freezing, as it ensures the game loop can exit cleanly.

4. Intro and Game Over Screens
The introduction (game_intro) and game over (game_over_screen) functions provide clear entry and exit points for gameplay. They display messages to the player and wait for a specific action (start the game or quit, and restart the game or quit, respectively). This structure enhances the game's flow and user interaction, making it clear what the player's options are and preventing confusion that might arise from an unresponsive game state.

5. FPS and Game Speed
The frame rate (FPS) control with clock.tick(snake_speed) ensures that the game runs smoothly and consistently across different hardware. By limiting the game to a specific number of frames per second, we prevent the game from running too fast on high-performance hardware, which can cause the game to appear to freeze or skip crucial update frames.

6. Clear Game Loop Structure
The game loop's structure has been clarified, with distinct sections for event handling, game state updates, and rendering. This clear separation helps prevent logic errors that could cause the game to freeze, ensuring that each part of the game loop has a specific purpose and is executed in the correct order.

Summary
These updates aim to make the game more robust, user-friendly, and free from common issues that can lead to freezing or crashes. By focusing on clear logic, proper event handling, and smooth gameplay, the updated code provides a solid foundation for further development and enhancements to the snake game.

<!--An image is an illustration for your project, the tip here is using your sense of humour as much as you can :D 

You can copy paste my markdown photo insert as following:
<p align="center">
<img src="your-source-is-here" width=40% height=40%>
-->

## 🛠️ Description
Simple Snake game created using pygame

## ⚙️  Languages or Frameworks Used
<!--Remove the below lines and add yours -->
The program was created with Python3 and pygame.

use this for install pygame

``` bash
python -m pip install --upgrade pygame
```

## 🌟 How to run
```bash
python ./main.py
```

## You can move using: W A S D

## 📺 Demo
<p align="center">
<img src="https://github.com/ndleah/python-mini-project/blob/main/IMG/Snake_game.png" width=70% height=70%>

## 🤖 Author
<!--Remove the below lines and add yours -->
[Alexander Monterrosa](https://github.com/Alex108-lab)

Additional Contribution by Michael Connell (https://github.com/Spaun12)

