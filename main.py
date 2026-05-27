import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.randn(3, 5)
c = b.view(5, 3)
d = c.unsqueeze(0)
e = d.to('cuda')  # если доступно