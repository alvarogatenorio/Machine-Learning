# JUST CRAP CODE FOR NOW

# For our stuff (will be de-commented in the future).
#import ml

# For the import files dialog.
from tkinter import filedialog
from tkinter import *

# For the numpy stuff.
import numpy as np

# For the matplotlib stuff.
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# For distinguishing between drags/zooms and actual clicks.
#import time (commented for now)

# Just saving the figure to catch click events over axes.
fig = plt.figure()

# Defining the axes for the main plot
ax_main = plt.axes([0.1,0.25,0.7,0.6])

# Defining the axes for the buttons.
# The numbers on the array are: left, bottom, width, height.
# The screen is a coordinate plane with the (0,0) in the bottom-left.

# Lower buttons.
ax_least_sqr = plt.axes([0.05, 0.1, 0.15, 0.075])
ax_least_sqr_ab = plt.axes([0.25, 0.1, 0.15, 0.075])
ax_fisher = plt.axes([0.45, 0.1, 0.15, 0.075])
ax_percep = plt.axes([0.65, 0.1, 0.15, 0.075])

# Side buttons.
ax_class1 = plt.axes([0.85, 0.75, 0.1, 0.075])
ax_class2 = plt.axes([0.85, 0.65, 0.1, 0.075])
ax_class3 = plt.axes([0.85, 0.55, 0.1, 0.075])
ax_class4 = plt.axes([0.85, 0.45, 0.1, 0.075])
ax_bound = plt.axes([0.85, 0.25, 0.1, 0.075])

# Upper buttons.
ax_train = plt.axes([0.05, 0.90, 0.15, 0.075])
ax_test = plt.axes([0.25, 0.90, 0.15, 0.075])
ax_clear = plt.axes([0.65, 0.90, 0.15, 0.075])


# Defining the buttons.

# Lower buttons.
b_least_sqr = plt.Button(ax_least_sqr, 'M. Cuad.')
b_least_sqr_ab = plt.Button(ax_least_sqr_ab, 'M. Cuad. ab.')
b_fisher = plt.Button(ax_fisher, 'Fisher')
b_percep = plt.Button(ax_percep, 'Percep.')

# Side buttons.
b_class1 = plt.Button(ax_class1, 'Clase 1')
b_class2 = plt.Button(ax_class2, 'Clase 2')
b_class3 = plt.Button(ax_class3, 'Clase 3')
b_class4 = plt.Button(ax_class4, 'Clase 4')
b_bound = plt.Button(ax_bound, 'Fronter.')

# Upper buttons.
b_train = plt.Button(ax_train, 'Im. entren.')
b_test = plt.Button(ax_test, 'Im. pruebas')
b_clear = plt.Button(ax_clear, 'Reiniciar')

# Auxiliary variables.
shape = 'undefined'
#n_class1 = 0 TRANSFORM INTO A LIST, A NUMPY ARRAY OR WHATEVER
#n_class2 = 0
#n_class3 = 0
#n_class4 = 0
current_class = 0
computed_classifier = False

#issue, not counting correctly, its late, maybe tomorrow i will fix it...
current_classes = 0

# Event handlers.

# auxiliary function (maybe move to one of the IO classes)
def import_file():
	root = Tk()
	root.withdraw()
	root.filename =  filedialog.askopenfilename()
	root.destroy()
	return root.filename

def clk_train(event):
	print(import_file())
	# actually read the file with an IO class

def clk_test(event):
	print(import_file())
	# actually read the file with an IO class

def clk_clear(event):
	print("RESET")
	ax_main.clear()
	global current_class
	global computed_classifier
	global shape
	global current_classes
	current_class = 0
	computed_classifier = False
	shape = 'undefined'
	current_classes = 0
	plt.draw()

# to be simplified
def clk_least_sqr(event):
	global computed_classifier
	computed_classifier = True
	print("viva el rey minimo cuadratico")
	# actually computes the classifier

# to be simplified
def clk_least_sqr_ab(event):
	if current_classes == 2: 
		global computed_classifier
		computed_classifier = True
		print("viva el rey alfabético")
		# actually computes the classifier
	else:
		print("too much for my body")

# to be simplified
def clk_fisher(event):
	if current_classes == 2:
		global computed_classifier
		computed_classifier = True
		print("viva el rey Fisher")
		# actually computes the classifier
	else:
		print("too much for my body")

# to be simplified
def clk_percep(event):
	if current_classes == 2:
		global computed_classifier
		computed_classifier = True
		print("viva el rey perceptrónico")
		# actually computes the classifier
	else:
		print("too much for my body")

# to be simplified
def clk_class1(event):
	if not computed_classifier:	
		# blue circle
		global shape
		shape = 'ob'
		global current_class
		current_class = 1
		print("class 1 selected")
		global current_classes
		current_classes+=1

# to be simplified
def clk_class2(event):
	if not computed_classifier:
		# blue cross
		global shape
		shape = 'xb'
		global current_class	
		current_class = 2
		print("class 2 selected")
		global current_classes
		current_classes+=1

# to be simplified
def clk_class3(event):
	if not computed_classifier:
		# blue star
		global shape
		shape = '*b'
		global current_class
		current_class = 3
		print("class 3 selected")
		global current_classes
		current_classes+=1

# to be simplified
def clk_class4(event):
	if not computed_classifier:
		# blue triangle
		global shape
		shape = '^b'
		global current_class
		current_class = 4
		print("class 4 selected")
		global current_classes
		current_classes+=1

def clk_bound(event):
	print("viva el rey fronterizo")
	# NOT IMPLEMENTED YET

#issue: when zooming/dragging you will plot a point
#solution: when zooming or dragging the mouse us released after moving
#https://stackoverflow.com/questions/48446351/distinguish-button-press-event-from-drag-and-zoom-clicks-in-matplotlib
def onclick(event):
	if event.inaxes is ax_main:
		if current_class == 0 and not computed_classifier:			
			print("ERROR: No class selected")
		else:
			x = event.xdata
			y = event.ydata
			if not computed_classifier: #so i swear the class is not 0
				ax_main.plot(x,y,shape)
				plt.draw()
			else: # so i don't give a fuck about the class
				# APPLY THE CLASSIFIER!!
				ax_main.plot(x,y,'or')
				plt.draw()

# Handlers connections.
b_train.on_clicked(clk_train)
b_test.on_clicked(clk_test)
b_clear.on_clicked(clk_clear)

b_least_sqr.on_clicked(clk_least_sqr)
b_least_sqr_ab.on_clicked(clk_least_sqr_ab)
b_fisher.on_clicked(clk_fisher)
b_percep.on_clicked(clk_percep)

b_class1.on_clicked(clk_class1)
b_class2.on_clicked(clk_class2)
b_class3.on_clicked(clk_class3)
b_class4.on_clicked(clk_class4)

b_bound.on_clicked(clk_bound)

fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

print("a gato viejo rata tierna")
