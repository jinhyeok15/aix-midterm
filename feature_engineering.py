"""
* 관찰
예측하기 힘든 범주에 대한 정보 수집하기 (보너스 번호 제외)
ex) 1 2 3 4 5 6

* 가설
normal state의 lottery numbers는 어느정도 예측 가능한 범주의 유형을 보유한다.
유형 labeling 하기
-> 로또 번호들 중 가장 낮은 숫자 범주와 가장 높은 숫자범주를 string 문자열로 합친 것을 feature로 활용

* 결과
```
{
    '1030': 65, 
    '0140': 424, 
    '0130': 262, 
    '1040': 157, 
    '2040': 18, 
    '0120': 50, 
    '1020': 4, 
    '0110': 3, 
    '2030': 5, 
    '3040': 1
}
```
최소 01부터 최대 40까지의 범주를 가진 lottery가 424로 가장 많았고,
'2040', '1020', '2030', '1020', '0110', '3040' 순으로 가장 낮았으며
위의 6개 범주는 예외사항으로 분류할 수 있음: 확률상 제거 가능
"""

import pandas as pd


def calc_range(num):
    return str(int(num/10)*10) if num>=10 else "01"


df = pd.read_csv("src/lottery.csv", header=0, index_col='round')

df['feature'] = df.apply(lambda x: calc_range(x['first'])+calc_range(x['sixth']), axis=1)

print(df.head(10))

# feature의 각 type별 개수 조사
from collections import defaultdict

count_dict = defaultdict(int)

for k in df['feature'].tolist():
    count_dict[k] += 1

print(count_dict)
