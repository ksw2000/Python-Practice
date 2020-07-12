import tensorflow as tf
import numpy as np

# 建立測試資料集
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

######################################################################
######################################################################
######################################################################

# tensorflow 建構神經網路
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

# 計算誤差
loss = tf.reduce_mean(tf.square(y-y_data))

# 反向傳播
# 梯度下降法 GradientDescentOptimize
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 準備進行訓練
init = tf.global_variables_initializer()

# 利用 session 來 run() 數據
sess = tf.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

# 得到的結果 Wegihts 很接近 1
# 而 biases 很接近 0.3

# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-2-example2/
