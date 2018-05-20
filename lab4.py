# -*- coding: utf-8 -*-

from math import *

from Tkinter import *
from tkColorChooser import *

# CIRCLE
def circle_canon(cx, cy, r):
	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	for x in range(r+1):
		y = round(sqrt(r ** 2 - x ** 2))

	#	print("\nPoint: %d %d", round(x), round(y))

		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

	for y in range(r):
		x = round(sqrt(r ** 2 - y ** 2))

		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

def circle_param(cx, cy, r):
	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	l = round(pi * r / 2 )  # длина четврети окружности
	for i in range(l + 1):
		x = round(r * cos(i / r))
		y = round(r * sin(i / r))
		
	#	print("\nPoint: %d %d", round(cx + x), round(cy + y))

		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

def circle_brez(cx, cy, r):

	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	x = 0
	y = r
	d = 2 - 2 * r # D(x+1, y-1) = [(x + 1)^2 + (y - 1)^2] - R^2 при x = 0, y = R // [...] - квадрат расстояния от центра, до диаг. точки

	while y >= 0:
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

		if d < 0:  # пиксель лежит внутри окружности
			b = 2 * d + 2 * y - 1
			x += 1

			if b <= 0:  # горизонтальный шаг
				d = d + 2 * x + 1
			else:  # диагональный шаг
				y -= 1
				d = d + 2 * x - 2 * y + 2

			continue

		if d > 0:  # пиксель лежит вне окружности
			b = 2 * d - 2 * x - 1
			y -= 1

			if b > 0:  # вертикальный шаг
				d = d - 2 * y + 1
			else:  # диагональный шаг
				x += 1
				d = d + 2 * x - 2 * y + 2

			continue

		if d == 0:  # пиксель лежит на окружности
			x += 1   # диагональный шаг
			y -= 1
			d = d + 2 * x - 2 * y + 2

def circle_middle(cx, cy, r): # рассчитывается разность квадратов расстояний между центром и точкой (x + 1, y - 1/2)/ точке на окружности

	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	x = 0
	y = r
	p = 1 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2 // p = (x + 1)^2 + (y - 1/2)^2 - r^2

	img.put(color, (cx + x, cy + y))
	img.put(color, (cx + x, cy - y))
	img.put(color, (cx - x, cy + y))
	img.put(color, (cx - x, cy - y))

	img.put(color, (cx + y, cy + x))
	img.put(color, (cx + y, cy - x))
	img.put(color, (cx - y, cy + x))
	img.put(color, (cx - y, cy - x))

	IMG_OBJECTS.add((cx + x, cy + y))
	IMG_OBJECTS.add((cx + x, cy - y))
	IMG_OBJECTS.add((cx - x, cy + y))
	IMG_OBJECTS.add((cx - x, cy - y))
	
	IMG_OBJECTS.add((cx + y, cy + x))
	IMG_OBJECTS.add((cx + y, cy - x))
	IMG_OBJECTS.add((cx - y, cy + x))
	IMG_OBJECTS.add((cx - y, cy - x))

	while x < y:

		x += 1
		if p < 0:  # средняя точка внутри окружности, ближе верхний пиксел, горизонтальный шаг
			p += 2 * x + 1
		else:   # средняя точка вне окружности, ближе диагональный пиксел, диагональный шаг
			y -= 1
			p += 2 * x - 2 * y + 1

		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		img.put(color, (cx + y, cy + x))
		img.put(color, (cx + y, cy - x))
		img.put(color, (cx - y, cy + x))
		img.put(color, (cx - y, cy - x))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

		IMG_OBJECTS.add((cx + y, cy + x))
		IMG_OBJECTS.add((cx + y, cy - x))
		IMG_OBJECTS.add((cx - y, cy + x))
		IMG_OBJECTS.add((cx - y, cy - x))

# ELLIPS
def ellips_canon(cx, cy, a, b):
	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	for x in range(0, a + 1):
		y = round(b * sqrt(1.0 - x ** 2 / a / a))
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

	for y in range(0, b + 1):
		x = round(a * sqrt(1.0 - y ** 2 / b / b))
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

def ellips_param(cx, cy, a, b):
	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	m = max(a, b)
	l = round(pi * m / 2)
	for i in range(0, l + 1, 1):
		x = round(a * cos(i / m))
		y = round(b * sin(i / m))
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

def ellips_brez(cx, cy, a, b):
	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	x = 0  # начальные значения
	y = b
	a = a ** 2
	d = round(b * b / 2 - a * b * 2 + a / 2)
	b = b ** 2

	while y >= 0:
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

		if d < 0:  # пиксель лежит внутри эллипса
			buf = 2 * d + 2 * a * y - b # -a ?
			x += 1
			if buf <= 0:  # горизотальный шаг
				d = d + 2 * b * x + b
			else:  # диагональный шаг
				y -= 1
				d = d + 2 * b * x - 2 * a * y + a + b

			continue

		if d > 0:  # пиксель лежит вне эллипса
			buf = 2 * d - 2 * b * x - b
			y -= 1

			if buf > 0:  # вертикальный шаг
				d = d - 2 * y * a + a
			else:  # диагональный шаг
				x += 1
				d = d + 2 * x * b - 2 * y * a + a + b

			continue

		if d == 0:  # пиксель лежит на окружности
			x += 1  # диагональный шаг
			y -= 1
			d = d + 2 * x * b - 2 * y * a + a + b

def ellips_middle(cx, cy, a, b):
	global info_cur_draw_color_hex
	color = info_cur_draw_color_hex['text']
	global img, IMG_OBJECTS

	x = 0   # начальные положения
	y = b

	a2 = a*a
	b2 = b*b
	ad = a2 * 2
	bd = b2 * 2

	x_max = a2 / sqrt(a2 + b2)
	teta = -ad * y
	dx = 0

	fpr = b2 - a2 * y + a2 * 0.25

	while (x < x_max):
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add((cx + x, cy + y))
		IMG_OBJECTS.add((cx + x, cy - y))
		IMG_OBJECTS.add((cx - x, cy + y))
		IMG_OBJECTS.add((cx - x, cy - y))

		if fpr > 0:
			y -= 1
			teta += ad
			fpr += teta

		dx += bd
		x += 1
		fpr += dx + b2

	fpr += 0.75 * (a2 - b2) - (b2 * x + a2 * y)

	teta = bd * x
	dy = -ad * y

	while y >= 0:
		img.put(color, (cx + x, cy + y))
		img.put(color, (cx + x, cy - y))
		img.put(color, (cx - x, cy + y))
		img.put(color, (cx - x, cy - y))

		IMG_OBJECTS.add(img.put(color, (cx + x, cy + y)))
		IMG_OBJECTS.add(img.put(color, (cx + x, cy - y)))
		IMG_OBJECTS.add(img.put(color, (cx - x, cy + y)))
		IMG_OBJECTS.add(img.put(color, (cx - x, cy - y)))

		if fpr < 0:
			x += 1
			teta += bd
			fpr += teta

		dy += ad
		fpr += dy + a2
		y -= 1

def draw_circle(step = 0):
	clean_log()
	global rb_var, info_LOG
	if rb_var.get() != 1:
		info_LOG['text'] = "Switch radiobutton to 'Circle' to use this function"
		info_LOG['bg'] = "#ffdddd"
		return

	global info_cur_draw_color_hex, info_cur_bg_color
	color = info_cur_draw_color_hex['text']
	bg_color = info_cur_bg_color['bg']
	global IMG_OBJECTS

	global draw_center_str, drawcircle_radius_str
	log_msg = None
	try: xc, yc = [int(i) for i in draw_center_str.get().split()]
	except Exception: log_msg = "Wrong xc, yc coordinates.\nExpected 'x y', x, y - real or integer numbers."
	try: r = int(drawcircle_radius_str.get())
	except Exception: log_msg = "Wrong r value.\nExpected 'r', where r - real or integer number."
	if log_msg:
		info_LOG['text'] = log_msg
		info_LOG['bg'] = "#ffdddd"
		return

	r += step
	alg = alg_var.get()
	global img
	if alg == algorithms[-1]:
		global CNV_OBJECTS, canv
		id = canv.create_oval(xc - r, yc + r, xc + r, yc - r)
		CNV_OBJECTS.append(id)
		return
	for i in range(len(algorithms)):
		if alg == algorithms[i]:
			func = functions_circle[i]
			func(xc, yc, r)

def draw_ellips(step = 0):
	clean_log()
	global rb_var, info_LOG
	if rb_var.get() != 2:
		info_LOG['text'] = "Switch radiobutton to 'Ellips' to use this function"
		info_LOG['bg'] = "#ffdddd"
		return

	global info_cur_draw_color_hex, info_cur_bg_color
	color = info_cur_draw_color_hex['text']
	bg_color = info_cur_bg_color['bg']
	global IMG_OBJECTS

	global draw_center_str, drawellips_a_str, drawellips_b_str
	log_msg = None
	try: xc, yc = [int(i) for i in draw_center_str.get().split()]
	except Exception: log_msg = "Wrong xc, yc coordinates.\nExpected 'x y', x, y - real or integer numbers."
	try: a = int(drawellips_a_str.get())
	except Exception: log_msg = "Wrong a value.\nExpected 'a', where a - real or integer number."
	try: b = int(drawellips_b_str.get())
	except Exception: log_msg = "Wrong b value.\nExpected 'b', where b - real or integer number."
	if log_msg:
		info_LOG['text'] = log_msg
		info_LOG['bg'] = "#ffdddd"
		return

	a += step
	b += step
	alg = alg_var.get()
	global img
	if alg == algorithms[-1]:
		global CNV_OBJECTS, canv
		id = canv.create_oval(xc - a, yc + b, xc + a, yc - b)
		CNV_OBJECTS.append(id)
		return
	for i in range(len(algorithms)):
		if alg == algorithms[i]:
			func = functions_ellips[i]
			func(xc, yc, a, b)

def draw_concentric():
	clean_log()
	global info_LOG
	global drawconcentric_step_str, drawconcentric_number_str
	log_msg = None
	while True:
		try: step = int(drawconcentric_step_str.get())
		except Exception:
			log_msg = "Wrong step value.\nExpected 'step', where step - real or integer number."
			break
		try: number = int(drawconcentric_number_str.get())
		except Exception:
			log_msg = "Wrong number value.\nExpected 'number', where number - integer number."
			break
		break

	if log_msg:
		info_LOG['text'] = log_msg
		info_LOG['bg'] = "#ffdddd"
		return

	global rb_var
	if rb_var.get() == 1: draw_function = draw_circle
	elif rb_var.get() == 2: draw_function = draw_ellips
	current_step = 0
	for i in range(number):
		draw_function(current_step)
		current_step += step

def set_draw_color():
	clean_log()
	global info_cur_draw_color, info_cur_draw_color_hex
	draw_color = askcolor()[-1]
	info_cur_draw_color['bg'] = draw_color
	info_cur_draw_color_hex['text'] = draw_color

def set_bg_color():
	clean_log()
	global info_cur_bg_color, info_cur_bg_color_hex
	bg_color = askcolor()[-1]
	info_cur_bg_color['bg'] = bg_color
	info_cur_bg_color_hex['text'] = bg_color
	canv['bg'] = bg_color

def delall():
	global info_LOG
	info_LOG['text'] = ""
	info_LOG['bg'] = "#ffffff"

	global CNV_OBJECTS, IMG_OBJECTS, canv, img, img_id
	global info_cur_bg_color
	bg_color = info_cur_bg_color['bg']
	for obj in CNV_OBJECTS: canv.delete(obj)
	CNV_OBJECTS.clear()
	canv.delete(img_id)
	IMG_OBJECTS.clear()
	img = PhotoImage(width = WIDTH, height = HEIGHT)
	img_id = canv.create_image((WIDTH//2, HEIGHT//2), image = img, state = "normal")

def compare_time():
	global CMP_STATE
	if CMP_STATE == 1: return
	CMP_STATE = 1
	clean_log()
	from time import clock

	N = 50
	R = 100

	times = [0, 0, 0, 0]
	for i in range(4):
		draw_circle = functions_circle[i]
		for k in range(N):
			t1 = clock()
			draw_circle(250, 250, R)
			t2 = clock()
			times[i] += t2 - t1

	delall()


	cmp_msg = "Time comparation:\n" + "{ N = " + str(N) + ", R = " + str(R) + '}\n\n'
	for i in range(4):
		cmp_msg += algorithms[i] + ":   \t" + str(round(times[i], 3)) + " sec\n"

	info_LOG['text'] = cmp_msg

def clean_log():
	global CMP_STATE
	CMP_STATE = 0
	global info_LOG
	info_LOG['text'] = ""
	info_LOG['bg'] = "#ffffff"

algorithms = ["Canon eq.", "Parametr eq.", "Bresenham alg.", "Middle-point alg.", "tkinter.draw_oval"]
functions_circle = [circle_canon, circle_param, circle_brez, circle_middle]
functions_ellips = [ellips_canon, ellips_param, ellips_brez, ellips_middle]

### UI init
root = Tk()
root.config(bg='dark slate gray')
root.geometry('1200x700+100+100')
root.title("CompGraph/Lab4")

WIDTH, HEIGHT = 500, 500; center = (WIDTH/2, HEIGHT/2)
CELL = 1; SCALE = 1; offset = (0, 0)
CNV_OBJECTS = []; IMG_OBJECTS = set() # IMG_OBJECTS is a set, since points can be painted on several occasions
canv = Canvas(root, width = WIDTH, height = HEIGHT, relief = RAISED)
canv.place(relx = 0.7, rely = 0.5, anchor = CENTER)

img = PhotoImage(width = WIDTH, height = HEIGHT)
img_id = canv.create_image((WIDTH//2, HEIGHT//2), image = img, state = "normal")

### BUTTONS, ENTRIES WIDGETS
# canvas size
info_CANVAS = Label(root, text = "Size: "+str(WIDTH)+" x "+str(HEIGHT)+" pixels", relief = RIDGE).place(relx = .65, rely = .1, anchor = "w")
# algorithms
info_alg = Label(root, text = "Current algorithm:", justify = CENTER, relief = RIDGE, width = 15).place(relx = .05, rely = 0.1, anchor = "w")

alg_var = StringVar()
alg_drop_list = OptionMenu(root, alg_var, *algorithms, command = None)
alg_drop_list.place(relx = 0.2, rely = 0.1, anchor = "w")
alg_drop_list['width'] = 20
alg_var.set(algorithms[0])

info_cur_draw_color = Label(root, text = None, justify = CENTER, relief = RIDGE, width = 2, bg = "#000000")
info_cur_draw_color.place(relx = 0.2, rely = 0.15, anchor = "w")
info_cur_draw_color_hex = Label(root, text = "#000000", justify = CENTER, relief = RIDGE, width = 16)
info_cur_draw_color_hex.place(relx = 0.232, rely = 0.15, anchor = "w")

info_cur_bg_color = Label(root, text = None, justify = CENTER, relief = RIDGE, width = 2, bg = "#ffffff")
info_cur_bg_color.place(relx = 0.2, rely = 0.2, anchor = "w")
info_cur_bg_color_hex = Label(root, text = "#ffffff", justify = CENTER, relief = RIDGE, width = 16)
info_cur_bg_color_hex.place(relx = 0.232, rely = 0.2, anchor = "w")

select_draw_color_bttn = Button(text='Change draw color', command = set_draw_color, width = 13).place(relx = 0.05, rely = 0.15, anchor = "w")
select_bg_color_bttn = Button(text='Change bg color', command = set_bg_color, width = 13).place(relx = 0.05, rely = 0.2, anchor = "w")

# CENTER OF FIGURES
center_rely = .33

rb_var = IntVar()
circle_rbttn = Radiobutton(root, text="Circle", variable=rb_var, value=1, command = None)
circle_rbttn.place(relx = .18, rely = center_rely - .05, anchor = "w")
ellipse_rbttn = Radiobutton(root, text="Ellips", variable=rb_var, value=2, command = None)
ellipse_rbttn.place(relx = .23, rely = center_rely - .05, anchor = "w")
circle_rbttn.select()

info_draw_center = Label(root, text = "Xc Yc", justify = CENTER, relief = RIDGE, width = 10, bg = "#cccccc").place(relx = .05, rely = center_rely, anchor = "w")
info_draw_center_comment = Label(root, text = "^ c - center of drawing", width = 18, bg = "#cccccc").place(relx = .25, rely = center_rely, anchor = "w")

draw_center_str = StringVar(); draw_center_str.set("250 250")
draw_center_entry = Entry(root, textvariable = draw_center_str, width = 11)
draw_center_entry.place(relx = .14, rely = center_rely, anchor = "w")

# CIRCLE PARAMS
circle_rely = center_rely + .05
info_circle = Label(root, text = "Radius", justify = CENTER, relief = RIDGE, width = 10, bg = "#cccccc").place(relx = .05, rely = circle_rely, anchor = "w")

drawcircle_radius_str = StringVar(); drawcircle_radius_str.set("100")
drawcircle_radius_entry = Entry(root, textvariable = drawcircle_radius_str, width = 4)
drawcircle_radius_entry.place(relx = .14, rely = circle_rely, anchor = "w")

drawcircle_bttn = Button(root, text = "Draw circle", command = draw_circle, width = 15).place(relx = .25, rely = circle_rely, anchor = "w")

# ELLIPS PARAMS
ellips_rely = center_rely + .1
info_ellips = Label(root, text = "A B", justify = CENTER, relief = RIDGE, width = 10, bg = "#cccccc").place(relx = .05, rely = ellips_rely, anchor = "w")

drawellips_a_str = StringVar(); drawellips_a_str.set("200")
drawellips_a_entry = Entry(root, textvariable = drawellips_a_str, width = 4)
drawellips_a_entry.place(relx = .14, rely = ellips_rely, anchor = "w")

drawellips_b_str = StringVar(); drawellips_b_str.set("100")
drawellips_b_entry = Entry(root, textvariable = drawellips_b_str, width = 4)
drawellips_b_entry.place(relx = .2, rely = ellips_rely, anchor = "w")

drawellips_bttn = Button(root, text = "Draw ellips", command = draw_ellips, width = 15).place(relx = .25, rely = ellips_rely, anchor = "w")

# DRAW CONCENTRIC
concentric_rely = center_rely + .18
info_concentric = Label(root, text = "Step Number", justify = CENTER, relief = RIDGE, width = 10, bg = "#cccccc").place(relx = .05, rely = concentric_rely, anchor = "w")

drawconcentric_step_str = StringVar(); drawconcentric_step_str.set("5")
drawconcentric_step_entry = Entry(root, textvariable = drawconcentric_step_str, width = 4)
drawconcentric_step_entry.place(relx = .14, rely = concentric_rely, anchor = "w")

drawconcentric_number_str = StringVar(); drawconcentric_number_str.set("20")
drawconcentric_number_entry = Entry(root, textvariable = drawconcentric_number_str, width = 4)
drawconcentric_number_entry.place(relx = .2, rely = concentric_rely, anchor = "w")

drawconcentric_bttn = Button(root, text = "Concentric", command = draw_concentric, width = 15).place(relx = .25, rely = concentric_rely, anchor = "w")

# OTHERS
del_bttn = Button(root, text = "Delete all", command = delall, width = 42).place(relx = .05, rely = .6, anchor = "w")

cmp_time_bttn = Button(text='Compare time', command = compare_time, width = 16)
cmp_time_bttn.place(relx = .245, rely = .67, anchor = "w")
CMP_STATE = 0

info_LOG_comment = Label(root, text = "Notification window", relief = RAISED).place(relx = .05, rely = .73, anchor = "w")
info_LOG = Label(root, text = None, justify = LEFT, relief = RAISED, width = 45, height = 8)
info_LOG.place(relx = .05, rely = .85, anchor = "w")

root.mainloop()
