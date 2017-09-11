import tensorflow as tf

op = tf.matmul(2, 3)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

print(sess.run(op))