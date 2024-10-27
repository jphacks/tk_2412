import numpy as np
import random
import torch


# normalize the input data
def data_normalization(data, min, max):
    return (data - min) / (max - min)

def data_receive(data_list):
    max_data = max(data_list)
    min_data = min(data_list)
    return max_data, min_data

def data_input(len, data_list):
    input = []
    for _ in range(len):
        data = 1
        max, min = data_receive(data_list)
        data = data_normalization(data, max ,min)
        input.append(data)
    return input

def database(url):
    file_object = open(url)
    database = []
    for line in file_object.readlines():
        database.append(int(line.replace('\n', '')))
    return database

# 删除数据集中最大和最小值
def data_cleaning(data_list, up, down):
    for _ in range(up):
        max, min = data_receive(data_list)
        data_list.remove(max)
    for _ in range(down):
        max, min = data_receive(data_list)
        data_list.remove(min)
    return data_list


# train data preprocess
def data_preprocess(data_list, len, value):
    signal_list = []
    train_x_list = []
    train_y_list = []
    interval = 0
    data_cleaning(data_list, 10, 20)
    max, min = data_receive(data_list)
    for signal in data_list:
        interval =interval + 1
        signal = data_normalization(signal, max, min)
        signal_list.append(signal)
        if interval % len == 0:
            train_x_list.append(signal_list)
            if np.average(signal_list) > value:
                train_y_list.append([1])
            else:
                train_y_list.append([0])
            signal_list = []
            interval = 0
    return train_x_list, train_y_list


def use_model(inputs, interval=0.5, file='ReadingAssistant/Model/save.pt'):
    for i in range(5):
        inputs[i] = data_normalization(inputs[i], 100, 600)
    inputs = torch.tensor(inputs, dtype = torch.float32)
    with torch.no_grad():
        import dill
        model = torch.load(file, pickle_module=dill)
        outputs = model(inputs)
        if outputs > interval:
            return True
        else:
            return False

# 定义信号采样器
def Sampler():
    x_list = []
    y_list = []
    for i in range(1000):
        if random.random() < 0.5:
            x = np.random.random(10) * 0.1
            alpha = noise_Sampler()
            x = x + alpha
            x_list.append(x.tolist())
            y_list.append([0])
        else:
            x = np.random.normal(0.5, 0.1, 10)
            alpha = noise_Sampler()
            x = x + alpha
            x_list.append(x.tolist())
            y_list.append([1])
    return x_list, y_list


# 定义噪声函数
def noise_Sampler():
    alpha = np.random.normal(0, 0.1, 10)
    return alpha