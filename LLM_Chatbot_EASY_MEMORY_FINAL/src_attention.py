import math
import torch


def attention(Q, K, V):
    scores = Q @ K.T / math.sqrt(Q.shape[-1])
    weights = torch.softmax(scores, dim=-1)
    return weights @ V


if __name__ == "__main__":
    Q = torch.rand(3, 4)
    K = torch.rand(3, 4)
    V = torch.rand(3, 4)
    print(attention(Q, K, V))
