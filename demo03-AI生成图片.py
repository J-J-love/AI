import torch

# 检查CUDA是否可用
is_cuda_available = torch.cuda.is_available()

if is_cuda_available:
    print("使用的是GPU版本的PyTorch。")
else:
    print("使用的是CPU版本的PyTorch。")