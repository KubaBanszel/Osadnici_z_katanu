# Map dimensions
MAP_WIDTH = 5
MAP_HEIGHT = 5

# Initial player position
player_x = 0
player_y = 0

# Game loop
while True:
    # Display the map
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if x == player_x and y == player_y:
                print("P", end=" ")  # Player's position
            else:
                print(".", end=" ")  # Empty space
        print()  # New line

    # Get user input for movement
    direction = input("Enter direction (w/a/s/d): ")

    # Update player position based on input
    if direction == "w" and player_y > 0:
        player_y -= 1  # Move up
    elif direction == "a" and player_x > 0:
        player_x -= 1  # Move left
    elif direction == "s" and player_y < MAP_HEIGHT - 1:
        player_y += 1  # Move down
    elif direction == "d" and player_x < MAP_WIDTH - 1:
        player_x += 1  # Move right

    # Clear the console (optional)
    # This works on most platforms, but may not work on all
    import os
    os.system("cls" if os.name == "nt" else "clear")
