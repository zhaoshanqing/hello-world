import numpy as np; 
def softmax(a):
        exp_a=np.exp(a);
        exp_a_sum=np.sum(exp_a);
        y=exp_a/exp_a_sum;
        return y;
def softmax1(a);
        c=np.max(a);
        exp_a=np.exp(a-c);
        exp_a_sum=np.sum(exp_a);
        y=exp_a/exp_a_sum;
        return y;
a=np.array([1,2,3]);
print(softmax(a));

