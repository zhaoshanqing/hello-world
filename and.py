import numpy as np;
def and1(x1,x2):
  w1,w2,theta=0.5,0.5,0.7;
  tmp=x1*w1+x2*w2;
  if tmp<=theta:
    return 0;
   else:
    return 1;
      
  
  
