import numpy as np;
import matplotlib.pyplot as plt;
def step_func(x):
  return np.array(x>0,dtype=np.int);
x=np.array(0,5,0.1);
y=step_func(x);
plt.plot(x,y);
plt.title("step fuction");
plt.show();

