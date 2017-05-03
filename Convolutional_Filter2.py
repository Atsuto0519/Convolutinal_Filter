#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# ベクトルを用意
# h:特徴ベクトル, x:入力, y:出力表現
# N:yの長さ
#
# h(n) = { 2 (n=0)}
#        { 1 (n=|1|)}
#        { 0 (otherwise)}
#
# x(n) = { 2 (n=0)}
#        {-1 (n=|1|}
#        { 0 (otherwise)}

h = [0, 1, 2, 1, 0]
x = [0, -1, 2, -1, 0]
N = len(h)+len(x)-1
y = range(N)

# conv_xh:畳み込み行列
conv_xh = np.zeros((N,len(x)))
for i in range(len(h)) :
    for j in range(len(x)) :
        conv_xh[i+j][j] = h[i]

# yを求める
y = np.dot(conv_xh, x)

# yをプロット
plt.plot(np.arange(-(N-1)/2, (N+1)/2, 1), y)
plt.show()
