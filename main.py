import tensorflow as tf

#tansor는 이러한 데이터가 있을때 같은 행끼리 더해줌
tansor=tf.constant([3,4,5])
tansor2 =tf.constant([6,7,8])

tansor3=tf.constant([[1,2],[3,4]])

#0이 10개인 녀석을 만들어줌
#행이 3개인 열 2줄 짜리를 2개 만들어줌
print(tf.zeros(10),tf.zeros([2,2,3]))

#몇개의 열인지 알아줌 몇 차원인지 알려주는 녀석
print(tansor.shape)

#텐서플로우의 변수를 지정하는 방법
w=tf.Variable(1.0)
#변수 수정하는 방법
w.assign(2)
#일부 값만 뽑아내주기
print(w.numpy())
