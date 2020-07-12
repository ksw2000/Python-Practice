import tensorflow as tf
import numpy as np

def add_layer(inputs, in_size, out_size, activation_function = None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs

# 載入數據
# np.linspace 用來創建等差數列 -1 ~ 1 300個
# 補充個
# a = np.array([1,2,3,4,5])
# b = a[np.newaxis, :]
# b 會變成 [[1,2,3,4,5]]
# c = a[:, np.newaxis]
# c 會變成 [[1],[2],[3],[4],[5]]
x_data = np.linspace(-1, 1, 300, dtype = np.float32)[:, np.newaxis]
# 模擬自然情況增加誤差值 常態分佈的random
# random.normal(loc, scale, size)
# loc: 平均值, scale: 標準差

noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

######################################################################################

# 利用占位符定義們們所需的神經網路輸入
# None 表示無論輸入多少都可以，因為輸入只有一個特徵所以值為 1
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 搭建神經網路 inputs=xs, in_size = 1, out_size = 10
# 建立隱藏層
l1 = add_layer(xs, 1, 10, activation_function = tf.nn.relu)
# 建立輸出層
prediction = add_layer(l1, 10, 1, activation_function = None)

# 計算預測值 prediction 和真實值的誤差，對兩者差的平方求和取平均
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices = [1]))

# 以0.1的效率來最小化誤差loss
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初強化變量
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)


######################################################################################


# 開始訓練
# 當運算用到 placeholder 時，需要 feed_dict 來指定輸入
for i in range(1000):
    sess.run(train_step, feed_dict = {xs:x_data, ys:y_data})

    # 每訓練 50 次輸出機器學習的誤差
    if i % 50 == 0:
        print(sess.run(loss, feed_dict = {xs: x_data, ys:y_data}))

# 輸出誤差逐漸減小，說明機器學習是有積極效果的
