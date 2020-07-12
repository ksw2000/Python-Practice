import tensorflow as tf

print(tf.__version__)

# 創立兩個矩陣
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])

# 矩陣相乘
product = tf.matmul(matrix1, matrix2)

# product 無法直接計算要透過 session 才可以

sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# stdout:
# [[12]]

# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-3-session/
