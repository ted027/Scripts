import numpy as np

class sigmoid():
  def __init__(self):
    self.output = None

  def forward(self, x):
    self.output = 1/(1+np.exp(-x))
    return self.output

  def backward(self, dx):
    return self.output * (1 - self.output)