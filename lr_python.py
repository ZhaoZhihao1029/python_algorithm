# -*- coding:utf-8 -*-
"""
@author:zzh
@file:lr_python.py
@time:2019/3/2717:32
"""
import numpy as np
import pandas as pd


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def computeLoss(X, y, theta):
    X = np.copy(X)
    y = np.copy(y)
    theta = np.copy(theta)
    m = X.shape[0]
    h = sigmoid(np.matmul(X, theta.T))
    first = np.matmul(-y.T, np.log(h))
    second = np.matmul((1 - y).T, np.log(1 - h))
    return np.sum(first - second) / m


def gradientDescent(X, y, theta, alpha, iters):
    m = X.shape[0]
    cost = np.zeros(iters)
    for i in range(iters):
        error = sigmoid(np.matmul(X, theta.T)) - y
        theta = theta - ((alpha / m) * np.matmul(X.T, error)).T
        cost[i] = computeLoss(X, y, theta)

    return theta, cost


def predict(theta, X):
    probability = sigmoid(np.matmul(X, theta.T))
    return [1 if x >= 0.5 else 0 for x in probability]
