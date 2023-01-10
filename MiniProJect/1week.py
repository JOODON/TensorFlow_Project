import matplotlib.pyplot as plt #외부 라이브러리 matplotlib.pyplot 를 불러와서 plt 라는 이름으로 사용
import numpy as np #외부 라이브러리 numpy 를 불러와서 np 라는 이름으로 사용
plt.style.use("_mpl-gallery")#plt에 사용 스타일을 _mpl-gallery 형식으로 사용함

np.random.seed(3)#Numpy라는 라이브러리에서 가장 기능적으로 와 가까운 특정수 3개를 랜덤으로 추출
x=0.5+np.arange(8)#0.5부터 7.5까지 1씩 증가하는값 8개를 리스트로 생성해서 X에 저장

y=np.random.uniform(2,7,len(x))#2~7까지에 실수중에 랜덤값으로 x에 길이 만큼 추출하여 y에 저장
fig,ax=plt.subplots()#프레임(fig) 과 그림을 그릴수 있는 캔버스인 (ax)를 plt.subplots()라는 함수를 통해서 생성해줌

ax.bar(x,y, width=1, edgecolor="white",linewidth=0.7)
#x와y의 막대그래프에 높이를 1 색상은 흰색 라인의 길이는 0.7로 설정해준다

ax.set(xlim=(0,8),xticks=np.arange(1,8),
       ylim=(0,8),yticks=np.arange(1,8))

#X축 제한을 (0,8) Y축 제한을 (0,8)로 지정
#X축 눈금값 (1,8) Y축 눈금값 (1,8)로 지정

plt.show()
#그래프를 출력해주는 부분

