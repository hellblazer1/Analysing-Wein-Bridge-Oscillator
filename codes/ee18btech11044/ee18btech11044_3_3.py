import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

RC = 160 *(10**-6)

#if using termux
import subprocess
import shlex
#end

num = [3.03*(RC**2),9.09*RC,3.03]	#describing transfer function
den = [(RC**2),(-0.03)*RC,1]
system = signal.lti(num,den)


T, yout = signal.step(system)	#step response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Step system response ")

#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_3.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_3.pdf"))
#plt.show()
