import seaborn as sns #seaborn이라는 외부라이브러리를 sns 라는 이름으로 사용
import matplotlib.pyplot as plt #외부 라이브러리 matplotlib.pyplot 를 불러와서 plt 라는 이름으로 사용

sns.set_theme()
#seaborn에 기본테마로 시킨다

tips=sns.load_dataset("tips")
#Tips에 예제 데이터 집합들을 로드시킵니다.

sns.relplot(
    data=tips,
    x="total_bill",y="tip",col="time",
    hue="smoker",style="smoker",size="size"
)
#데이터는 tips에 데이터를 사용하고 x축의 이름은 total_bill y축의 이름은 tip
#time이라는 컬럼을 넘겨줌으로 점심/저녁 시간에 따른 데이터를 분류 할수있다
#색상은(hue)는 smoker색으로 마커의 모양도 smoker색으로 넣어준다

plt.show()
#그래프를 출력해주는 부분