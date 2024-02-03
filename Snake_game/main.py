# Import necessary libraries
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (36, 36, 36)
red = (213, 50, 80)
green = (0, 255, 0)

# Game window dimensions
display_width = 600
display_height = 400  # Adjusted to 400 for better gameplay area

# Set up display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock for controlling game FPS
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Function to display the score
def score(score):
    font = pygame.font.SysFont("arial", 15)
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, [0, 0])

# Function to draw the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color, y_displace=0, font_size=35):
    font_style = pygame.font.SysFont("bahnschrift", font_size)
    mesg = font_style.render(msg, True, color)
    rect = mesg.get_rect(center=(display_width / 2, display_height / 2 + y_displace))
    display.blit(mesg, rect)

# Function for the start screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        display.fill(black)
        message("Welcome to Snake Game", green, -50, 40)
        message("Press Space to Play or Q to Quit", white, 50, 25)
        pygame.display.update()
        clock.tick(15)

# Function for the game over screen
def game_over_screen(score):
    display.fill(black)
    message("Game Over", red, -50, 50)
    message("Your Score: " + str(score), white, 0, 40)
    message("Press Space to Play Again or Q to Quit", white, 50, 25)
    pygame.display.update()
    time.sleep(2)

    # Wait for player input to restart or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    gameLoop()  # Restart the game

# Main game loop function
def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_over_screen(Length_of_snake - 1)  # Show the game over screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_intro()
gameLoop()


