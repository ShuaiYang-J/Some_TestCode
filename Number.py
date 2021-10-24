# coding: utf-8
import numpy
import scipy.special
import imageio


class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 函数调用时神经网络输入节点数、隐层节点数、输出节点数
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # 学习速率
        self.lr = learningrate
        # 连接权重矩阵
        self.wih = (numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes)))
        self.who = (numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes)))
        #匿名函数，可以搜一搜，是个有趣的东西
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # 训练神经网络
    def train(self, inputs_list, targets_list):
        # 将输入转为二维数组
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        # 神经网络计算
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        # 基于所计算输出与目标输出之间的误差，改进权重。
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 权重编码（隐藏层-最终层）
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        # 权重编码（输入层-隐藏层）
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        pass

    # 神经网络查询
    def query(self, inputs_list):
        # 将输入转为二维数组
        inputs = numpy.array(inputs_list, ndmin=2).T
        # 神经网络计算
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

# 神经网络输入节点数、隐层节点数、输出节点数
input_nodes = 784# 28 * 28 = 784
hidden_nodes = 200
output_nodes = 10

# 学习速率
learning_rate = 0.1

# 创建神经网络
net = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
# 将mnist training data csv文件加载到列表中
training_data= open(r"C:\Code\Toy_CNN\number\mnist_dataset\mnist_test.csv", 'r')
training_list = training_data.readlines()
training_data.close()

# 训练，epochs是训练重复次数，值越大时间越长，精度越高
repeat = 2
for e in range(repeat):
    for record in training_list:
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        net.train(inputs, targets)
        pass
    pass

# 测试神经网络是否能准确识别自己的手绘28*28 png图像
image=r'C:\Code\Toy_CNN\number\1.jpg'
img_array = imageio.imread(image, as_gray=True)
    # 从28x28重塑为784个值列表
m,n=img_array.shape
# 黑底白字 白底黑字--- 需求是不一样的 
# img_data = 255.0 - img_array.reshape(m*n)
img_data = img_array.reshape(m*n)
img = (img_data / 255.0 * 0.99) + 0.01
inputs = img
# 查询神经网络
outputs = net.query(inputs)
# 系统得到的值
result = numpy.argmax(outputs)
print("识别结果：", result)