#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# ベクトルを用意
# h:特徴ベクトル, x:入力, y:出力表現
# N:yの長さ

h = [0.9, 0.2, 0.4]
x = [0.5, 1.0, 0.7, 0.1]
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
plt.plot(range(N), y)
plt.show()
