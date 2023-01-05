import numpy as np
import pandas as pd

data=pd.read_csv("gpascore.csv")

data=data.dropna()

ydata=data['admit'].values

xdata=[]

for i,rows in data.iterrows():
    xdata.append([rows['gre'],rows['gre'],rows['rank']])

# data.fillna() 데이터빈 값을 자동으로 채워줌 (이안에 들어간 값으로)

import tensorflow as tf

#자동으로 딥러닝 모델 만드는 방법
model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(64,activation='tanh'),
    tf.keras.layers.Dense(128,activation='tanh'),
    tf.keras.layers.Dense(1,activation='sigmoid'),#0과 1사이에 값을 뱉고 싶으면 sigmoid를 써줌
    #마지막에는 1로 되는 노드가 나와야함
])

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#알아서 학습해줌
#Xdata는추론이고 Y데이터는 결과값을 넣어주기 epochs는 몇번 반복 시킬건지
model.fit(np.array(xdata),np.array(ydata),epochs=10)

predict=model.predict([[750,3.70,3],[400,2.2,1]])
print(predict)