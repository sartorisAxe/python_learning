import unfold
import mnk
import numpy as np

#GET INPUT FILES
r_values, a_values = unfold.unfold('C:\\python\\input_files\\input_ldf_01.txt')

#DATA
x_samp = np.array(r_values)
y_samp = np.array(a_values)

my_module = mnk.least_square(x_samp,y_samp)

my_module.show_plot()

my_module.get_fit()