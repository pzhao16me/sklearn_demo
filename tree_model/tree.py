import turtle


def tree(branchlen, t):
	if branchlen > 5:
		t.forward(branchlen)
		t.right(20)
		tree(branchlen - 15, t)
		t.left(40)
		tree(branchlen - 15, t)
		t.right(20)
		t.backward(branchlen)


def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("blue")
	tree(75, t)
	myWin.exitonclick()


if __name__ == '__main__':
	main()
