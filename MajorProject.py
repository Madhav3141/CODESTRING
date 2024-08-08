import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up game variables
block_size = 20
snake_speed = 15
clock = pygame.time.Clock()

# Initialize snake and food
snake = [(width // 2, height // 2)]
direction = 'RIGHT'
change_to = direction

food_pos = (random.randrange(1, (width // block_size)) * block_size, 
            random.randrange(1, (height // block_size)) * block_size)
food_spawn = True

# Game Over flag
game_over = False

# Glow effect parameters
glow_color = (0, 255, 0)
glow_intensity = 100
glow_pulse = 0
glow_direction = 1

def draw_background():
    for i in range(height):
        color = (i * 255 // height, 0, 255 - i * 255 // height)
        pygame.draw.line(win, color, (0, i), (width, i))

def show_start_screen():
    win.fill(black)
    font = pygame.font.Font(None, 74)
    text = font.render("Press any key to start", True, white)
    win.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Show start screen
show_start_screen()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    # Validate direction change
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        new_head = (snake[0][0], snake[0][1] - block_size)
    elif direction == 'DOWN':
        new_head = (snake[0][0], snake[0][1] + block_size)
    elif direction == 'LEFT':
        new_head = (snake[0][0] - block_size, snake[0][1])
    elif direction == 'RIGHT':
        new_head = (snake[0][0] + block_size, snake[0][1])

    # Add new head
    snake.insert(0, new_head)

    # Check if snake has eaten the food
    if snake[0] == food_pos:
        food_spawn = False
    else:
        snake.pop()

    # Spawn food
    if not food_spawn:
        food_pos = (random.randrange(1, (width // block_size)) * block_size, 
                    random.randrange(1, (height // block_size)) * block_size)
    food_spawn = True

    # Game Over conditions
    if (snake[0][0] not in range(0, width) or 
        snake[0][1] not in range(0, height)):
        game_over = True
    for block in snake[1:]:
        if snake[0] == block:
            game_over = True

    # Update screen
    draw_background()

    # Glowing effect calculation
    glow_pulse += glow_direction
    if glow_pulse >= 100 or glow_pulse <= 0:
        glow_direction *= -1

    glow_value = glow_pulse / 100.0 * glow_intensity

    for pos in snake:
        pygame.draw.rect(win, (0, int(255 - glow_value), 0), pygame.Rect(pos[0], pos[1], block_size, block_size))
        pygame.draw.rect(win, (0, int(255 - glow_value), 0), pygame.Rect(pos[0] + 2, pos[1] + 2, block_size - 4, block_size - 4))

    pygame.draw.rect(win, (255, 255, int(255 - glow_value)), pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))
    pygame.draw.rect(win, (255, 255, int(255 - glow_value)), pygame.Rect(food_pos[0] + 2, food_pos[1] + 2, block_size - 4, block_size - 4))

    pygame.display.flip()

    clock.tick(snake_speed)

# End the game
pygame.quit()
