import torch
import numpy as np

a = torch.tensor(([2, 3], [3, 4], [5, 6]))
print(a)
b = a.numpy()
c = b.flatten()
print(type(c))
print(c)
