'''
this function meant to determine fitting
for a general exponential pattern
'''
import matplotlib.pyplot as plt 
import scipy.optimize as opt 
import numpy as np 

class least_square():
	def __init__(self, x_samp, y_samp):
		self.x_samp = x_samp
		self.y_samp = y_samp

	def __str__(self):
		return [self.x_samp, self.y_samp]

	#GENERAL EQUATION ----------------------------
	def func(self, x, A, c):
		'''
		-smaller A gives a smaller amplitude
	    -negative A flips the curve across a horizontal plane
	    -smaller c controls the shape by flattening the "knee" of the curve
	    -negative c flips the curve across a vertical plane
	    -d sets the y-intercept
		'''
		return A*np.exp(-c*x)

	def show_plot(self):
		# Plotting Sampling Data
		plt.plot(self.x_samp, self.y_samp, "ko", label="Data")

		x_lin = np.linspace(0, self.x_samp.max(), 50)                   # 50 evenly spaced digits between 0 and max

		# Trials
		A, c = -1, -1e-2
		y_trial1 = self.func(x_lin,  A,     c)
		y_trial2 = self.func(x_lin, -1, 3e-3)
		y_trial3 = self.func(x_lin, -1, -3e-3)

		plt.plot(x_lin, y_trial1, "--", label="Trial 1")
		plt.plot(x_lin, y_trial2, "--", label="Trial 2")
		plt.plot(x_lin, y_trial3, "--", label="Trial 3")
		plt.legend()
		plt.show()

	def get_fit(self):
		# REGRESSION ------------------------------------------------------------------
		p0 = [-1, 3e-3]   # guessed params
		w, _ = opt.curve_fit(self.func, self.x_samp, self.y_samp, p0=p0)     
		print("Estimated Parameters", w)  
		x_lin = np.linspace(0, self.x_samp.max(), 50) # 50 evenly spaced digits between 0 and max

		# Model
		y_model = self.func(x_lin, *w)

		# PLOT ------------------------------------------------------------------------
		# Visualize data and fitted curves
		plt.plot(self.x_samp, self.y_samp, "ko", label="Data")
		plt.plot(x_lin, y_model, "k--", label="Fit")
		plt.title("Least squares regression")
		plt.legend(loc="upper left")
		plt.show()

