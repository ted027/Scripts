import numpy as np

class nn():
  def __init__(self, n_i, n_o, lr):
    self.weight = np.random.randn(n_o, n_i)
    self.input = None
    self.grad = np.zeros((n_i, n_o))
    self.lr = lr

  def forward(self, x):
    self.inputs = x.reshape(-1, 1)  # 入力の値を保持
    return np.dot(self.weight, self.inputs)

  def backward(self, dx):
    self.grad = np.dot(self.inputs.reshape(-1,1), dx.reshape(1,-1)).reshape(self.weight.shape) # wに関する微分計算
    return np.dot(dx.reshape(1, -1), self.weight) # xに関する微分計算

  def update(self):
    self.weight -= self.grad*self.lr
