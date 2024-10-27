import numpy as np
from ReadingAssistant.Utils import utils_function
import torch
import torch.nn as nn
import torch.optim as optim

# 定义Emotion模型
class Emotion_MLP(nn.Module):
    def __init__(self):
        super(Emotion_MLP, self).__init__()
        self.fc1 = nn.Linear(5, 64)  # 输入层到隐藏层
        self.fc2 = nn.Linear(64, 32)  # 隐藏层
        self.fc3 = nn.Linear(32, 1)   # 隐藏层到输出层

    def forward(self, x):
        import torch
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


#model training
def train_model(model, x_train, y_train, epochs, batch_size):
    criterion = nn.BCELoss()  # 二元交叉熵损失函数
    optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adam优化器

    for epoch in range(epochs):
        for i in range(0, len(x_train), batch_size):
            x_batch = x_train[i:i+batch_size]
            y_batch = y_train[i:i+batch_size]

            # 前向传播
            outputs = model(x_batch)
            loss = criterion(outputs, y_batch)

            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')
    #torch.save(model, '../Model/save.pt')
    import dill
    torch.save(model, '../Model/save.pt', pickle_module=dill)


# model evaluating
def evaluate_model(model, x_test, y_test):
    with torch.no_grad():
        outputs = model(x_test)
        predicted = (outputs > 0.5).float()
        correct = (predicted == y_test).float()
        accuracy = correct.sum() / len(y_test)
        print(f'测试集准确率: {accuracy.item():.4f}')

if __name__ == '__main__':
    # 给出数据
    data = [[0.1, 0.1, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1, 0.1]]

    result = [[1], [0], [0], [0], [0]]

    train_url = './sensor_values.txt'
    evaluate_url = './sensor_values.txt'

    state_0 = torch.tensor(utils_function.noise_Sampler(),  dtype=torch.float32)
    data_train = utils_function.database(train_url)
    data_eval = utils_function.database(evaluate_url)
    x_train, y_train = utils_function.data_preprocess(data_train , 5, 0.5)
    x_train = torch.tensor(x_train, dtype = torch.float32)
    y_train = torch.tensor(y_train, dtype = torch.float32)

    x_test, y_test = utils_function.data_preprocess(data_eval , 5, 0.5)
    x_test = torch.tensor(x_test, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32)


    model = Emotion_MLP()

    # 训练模型
    train_model(model, x_train, y_train, epochs=50, batch_size=16)

    #model = torch.load('.\save.pt')

    # 评估模型
    evaluate_model(model, x_test, y_test)

    # 使用模型范例
    #print(f'网络输出结果: {use_model(state_0).item():.4f}')
