# import torch
# x = torch.tensor([[11,2,3],[4,1,6],[8,3,1]])
# max = x.max()
# print(max)
#
# import torch
# import torch.nn.functional as F
#
# predictions = torch.tensor([[1.0, 0.0, 0.0,0.0],
#                             [0.0, 1.0, 0.0,0.0],
#                             [0.0, 0.0, 1.0,0.0],
#                             [0.0, 0.0, 0.0,1.0]])
# targets = torch.tensor([0, 1, 2, 3])
#
# loss = F.cross_entropy(predictions, targets)
# # print(loss)
#
# print("交叉熵损失:", loss.item())

import torch
import torch.nn as nn


# 定义一个简单的神经网络模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
# 创建模型实例
model = SimpleModel()
# 获取模型的所有参数及其名称
for name, param in model.named_parameters():
    print(name, param.shape)

