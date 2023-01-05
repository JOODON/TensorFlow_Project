import tensorflow as tf

tall=170
shose=260


#미지수는 변수로 지정
a=tf.Variable(0.1)
b=tf.Variable(0.2)

def Loss_function():
    # 실제값에서 예측 값을 뺀거
    loss_val=tall*a+b
    return tf.square(260-(loss_val))

#경사 하강법을 통해 알아서 구해줌
opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(Loss_function,var_list=[a,b])
    # 손실함수랑 varList
    # print(a.numpy(),b.numpy())

print(tall)
print(a.numpy())
print(b.numpy())

value=tall*a.numpy()+b.numpy()

print(value)