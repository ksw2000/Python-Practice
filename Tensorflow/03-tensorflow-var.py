import tensorflow as tf

# 定義一個 tensorflow 變數
state = tf.Variable(0, name='counter')

# 定義一個 tensorflow 常數
one   = tf.constant(1)

# 將這兩個相加 (尚未計算)
new_val = tf.add(state, one)

# 將 state 賦予新值
update = tf.assign(state, new_val)

# 如果在 tensorflow 中設定了變量，那麼初始化變量很重要
# 因此在定義變量後一定要初始化

init = tf.global_variables_initializer()

# 使用 session 開始做計算
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

# stdout
# 1 先 (0+1) 然後 counter = 1
# 2 再 (1+1) counter = 2
# 3 再 (2+1) counter = 3

# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-4-variable/
