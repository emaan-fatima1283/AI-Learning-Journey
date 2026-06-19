WIDTH = 20
HEIGHT = 10

def create_grid():
    grid = []
    for _ in range(HEIGHT):
        row = []
        for _ in range(WIDTH):
            row.append(" ")
        grid.append(row)
    return grid

def draw_grid(grid, score):
    print("\n" * 40)
    print(f"Score: {score}")
    print("=" * (WIDTH + 2))
    for row in grid:
        print("|" + "".join(row) + "|")
    print("=" * (WIDTH + 2))

def place_food(snake):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] not in snake:
                return [x, y]

def update_grid(grid, snake, food):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            grid[y][x] = " "

    grid[food[1]][food[0]] = "*"

    for i, part in enumerate(snake):
        x, y = part
        grid[y][x] = "O" if i == 0 else "o"

def move_snake(snake, direction):
    head = snake[0]
    x, y = head[0], head[1]

    if direction == "w":
        y -= 1
    elif direction == "s":
        y += 1
    elif direction == "a":
        x -= 1
    elif direction == "d":
        x += 1

    return [x, y]

def game_over_message(score):
    print("\n===== GAME OVER =====")
    print(f"Final Score: {score}")
    print("Better luck next time!")

def snake_game():
    snake = [[5, 5], [4, 5], [3, 5]]
    direction = "d"
    food = place_food(snake)
    score = 0

    while True:
        grid = create_grid()
        update_grid(grid, snake, food)
        draw_grid(grid, score)

        print("Controls: w = up, s = down, a = left, d = right")
        move = input("Move: ").lower()

        opposite = {"w":"s", "s":"w", "a":"d", "d":"a"}
        if move in ["w", "a", "s", "d"] and move != opposite[direction]:
            direction = move

        new_head = move_snake(snake, direction)

        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            game_over_message(score)
            break

        if new_head in snake:
            game_over_message(score)
            break

        snake.insert(0, new_head)

        if new_head == food:
            score += 10
            food = place_food(snake)
        else:
            snake.pop()

snake_game()
