import turtle

def pythagoras_tree(t, order, size):
    if order == 0:
        return
    else:      
        t.forward(size)
        t.left(45)
        pythagoras_tree(t, order - 1, size / (2 ** 0.5))
        t.right(90)
        pythagoras_tree(t, order - 1, size / (2 ** 0.5))
        t.left(45)
        t.backward(size)


def draw_pythagoras_tree():
    order = int(input("Введіть рівень рекурсії: "))
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)

    size=100
    # Малюємо дерево Піфагора3
    pythagoras_tree(t, order, size)
    window.mainloop()


draw_pythagoras_tree()