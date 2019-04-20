import numpy as np

from nn import nn
from sigmoid import sigmoid
from MSE import MSE

fc1 = nn(10, 5, 0.1)
sig1 = sigmoid()
fc2 = nn(5, 2, 0.1)
sig2 = sigmoid()
mse = MSE()
x = np.random.randn(10) # 学習データ生成
t = np.random.randn(2) # 教師データ生成
for i in range(100):
  out = sig2.forward(fc2.forward(sig1.forward(fc1.forward(x))))
  loss = mse.forward(out, t)
  print(loss)
  grad = mse.backward(out, t)
  fc1.backward(sig1.backward(fc2.backward(sig2.backward(grad))))
  fc1.update()
  fc2.update()