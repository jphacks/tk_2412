from ReadingAssistant.Utils import utils_function

import numpy as np

data = []
data = utils_function.database("./sensor_values.txt")
print(np.average(data))
train_x, train_y = utils_function.data_preprocess(data, 5, 0.8)
print(train_x)
print(train_y)


print(utils_function.use_model([0.6,0.7,0.1,0.6,1], 0.5, "../Model/save.pt"))