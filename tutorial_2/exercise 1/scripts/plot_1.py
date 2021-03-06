#!/usr/bin/python
import matplotlib.pyplot as pyp
import pylab
import numpy as np
# for reduction
#Plot between x : Problem size, y: computatinal time (OpenMP and Non-OpenMP)
#sh weak_scaling.sh
# Use numpy to load the data contained in the file
# file1.txt into a 2-D array called data
# 0 1
# 1 2
# 4 5
# Note: remove the newline from last line of txt files

file1_data = np.loadtxt('./generated_data/log_non_opemp_time_vs_prblmSize.txt')
file2_data = np.loadtxt('./generated_data/log_r_time_prlm_sz.txt')
file3_data = np.loadtxt('./generated_data/log_r_eff_vs_prblm_sz.txt')
file4_data = np.loadtxt('./generated_data/log_r_speedup_vs_prblm_sz.txt')

# plot the first column as x, and second column as y
# use pylab to plot x and y as red circles
# third parameter in plot is color, change it according to your need
#p1 = pyp.plot(file1_data[:,0], file1_data[:,1], 'ro')
p1 = pyp.plot(file1_data[:,0], file1_data[:,1], 'y')
p2 = pyp.plot(file2_data[:,0], file2_data[:,1], 'b')
p3 = pyp.plot(file3_data[:,0], file3_data[:,1], 'g')
p4 = pyp.plot(file4_data[:,0], file4_data[:,1], 'r')
        
pylab.title('Weak Scaling for reduction')
pylab.xlabel('Number of divisions')
#pylab.ylabel('Computation Time(second)')

pylab.grid(True)

#let python select the best position for legend
pyp.legend([p1[0],p2[0],p3[0],p4[0]], ['No OpenMP(Time-sec)','OpenMP(Time-sec)', 'Efficiency', 'Speedup'], 'best', numpoints=1)

pyp.savefig("./generated_plots/weak_scaling_r_time_eff_speedup_VS_size.png")

# show the plot on the screen
pylab.show()




