# placeholder 是 tensorflow 中的占位符，暫時儲存變量

import tensorflow as tf

# 定義 tensorflow 的型態
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict = {
        input1:[7.],
        input2:[2.]
    }))

# stdout
# [14.]

# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-5-placeholde/
