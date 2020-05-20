import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end

RC = 160 *(10**-6)


num = [3*(RC**2),9*RC,3]		#describing transfer function
den = [(RC**2),0,1]
system = signal.lti(num,den)

T, yout = signal.impulse(system)	#oscillating response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Impulse system response ")
#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_5.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_5.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_5.pdf"))
#plt.show()
