#
# @Date        : 2020-05-20 19:38:43
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-05-20 20:12:07
# @FilePath    : \python-examples\test\Cupid's-arrow.py
# @Describe    :
#
import turtle as t


def init():
    t.speed(2)
    t.pensize(2)
    t.screensize(400, 360)
    t.color("red", "red")
    t.bgcolor("white")


def drawHeartRight():
    t.up()
    t.goto(50, 50)
    t.pendown()
    t.right(45)
    t.goto(100, 0)
    t.seth(45)
    t.fd(120)
    t.circle(50, 225)


def drawHeartLeft():
    t.up()
    t.goto(0, 0)
    t.down()
    t.seth(45)
    t.fd(120)
    t.circle(50, 225)
    t.seth(90)
    t.circle(50, 225)
    t.fd(120)


# problems???
def drawArrow():
    t.up()
    t.seth(0)

    # 箭羽
    t.goto(-210, 40)
    t.pendown()
    t.goto(-215, 44)
    t.goto(-190, 49)
    t.goto(-175, 46)
    t.up()

    t.goto(-210, 40)
    t.pendown()
    t.goto(-213, 34)
    t.got0(-185, 39)
    t.goto(-175, 46)
    t.up()

    # # 箭杆
    # t.pendown()
    # t.goto(0, 80)
    # t.penup()
    # t.goto(160, 110)
    # t.pendown()
    # t.goto(320, 140)

    # # 箭蔟
    # t.left(160)
    # t.begin_fill()
    # t.fd(10)
    # t.left(120)
    # t.fd(10)
    # t.left(120)
    # t.fd(10)
    # t.end_fill()


if __name__ == "__main__":
    init()
    drawHeartRight()
    drawHeartLeft()
    drawArrow()
    t.hideturtle()
    t.done()
