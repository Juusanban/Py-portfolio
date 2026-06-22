import turtle


def create_turtle():
    screen = turtle.Screen()
    screen.title("Turtle Fractal Generator")
    screen.setup(width=1000, height=800)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)

    return screen, pen


def draw_square(pen, size):
    for _ in range(4):
        pen.forward(size)
        pen.left(90)


def draw_rotating_squares(pen):
    pen.color("orange")

    for _ in range(36):
        draw_square(pen, 200)
        pen.left(10)


def draw_geometric_pattern(pen):
    pen.color("darkred")

    for _ in range(72):
        pen.forward(180)
        pen.left(175)


def draw_koch_curve(pen, length, level):
    if level == 0:
        pen.forward(length)
        return

    draw_koch_curve(pen, length / 3, level - 1)
    pen.left(60)

    draw_koch_curve(pen, length / 3, level - 1)
    pen.right(120)

    draw_koch_curve(pen, length / 3, level - 1)
    pen.left(60)

    draw_koch_curve(pen, length / 3, level - 1)


def draw_koch_line(pen, level):
    pen.color("blue")
    pen.penup()
    pen.goto(-350, 0)
    pen.pendown()

    draw_koch_curve(pen, 700, level)


def draw_koch_snowflake(pen, level):
    pen.color("green")
    pen.penup()
    pen.goto(-300, 180)
    pen.pendown()

    for _ in range(3):
        draw_koch_curve(pen, 600, level)
        pen.right(120)


def select_recursion_level():
    while True:
        value = input("再帰レベルを入力してください（0〜5）: ").strip()

        try:
            level = int(value)

            if 0 <= level <= 5:
                return level

            print("0〜5の数字を入力してください。")

        except ValueError:
            print("数字を入力してください。")


def show_menu():
    print("=== Turtle Fractal Generator ===")
    print("1. 回転する正方形")
    print("2. 幾何学模様")
    print("3. コッホ曲線")
    print("4. コッホ雪片")


def main():
    show_menu()

    choice = input("描画する図形を選択してください: ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("1〜4の番号を入力してください。")
        return

    level = 0

    if choice in ["3", "4"]:
        level = select_recursion_level()

    screen, pen = create_turtle()

    if choice == "1":
        draw_rotating_squares(pen)

    elif choice == "2":
        draw_geometric_pattern(pen)

    elif choice == "3":
        draw_koch_line(pen, level)

    elif choice == "4":
        draw_koch_snowflake(pen, level)

    pen.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    main()