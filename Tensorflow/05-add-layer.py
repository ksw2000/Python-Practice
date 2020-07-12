import tensorflow as tf

# add_layer 需要四個參數：
# 輸入值、輸入的大小、輸出的大小、激勵函數

def add_layer(inputs, in_size, out_size, activation_function = None):
    # 生成參數時，隨機變量會比全部為 0 來的好
    # 因此我們這裡 weights 為一個 in_size 行 out_size 列的隨機變量矩陣
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    # 在機器學習中，biases 推薦值不為 0，所以我們這理是在 0 向量的基礎上再加 0.1
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    # 定義 Wx_plus_b 即神經網路未激活的值
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    # 當 activation_function 為 None 時，輸出就是現在的預測值 (Wx_plus_b)
    # 不為 None 時，就把 Wx_plus_b 傳到 activation_function 函數中得到輸出

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs

# https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/3-1-add-layer/
