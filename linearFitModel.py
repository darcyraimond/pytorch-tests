# Define a model
import torch

class Network(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, t):
        return self.linear(t)