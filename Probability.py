import numpy as np

pro = {'均匀分布：' : np.random.uniform(low=0, high=1, size=100),
       '二项分布：' : np.random.binomial(10, 0.5, 100),
       '标准正态分布：' : np.random.standard_normal(100),
       '正态分布：' : np.random.normal(0, 1, 100),
       '伽马分布：' : np.random.gamma(5, 0.5, 100),
       '贝塔分布：' : np.random.beta(5, 5, 100),
       '指数分布：' : np.random.exponential(0.5, 100),
       '卡方分布：' : np.random.chisquare(5, 100),
       'F分布：' : np.random.f(5, 5, 100),
       '泊松分布：' : np.random.poisson(5, 100)}

def calculate_values(random_data):
    print(f'它的均值为{np.mean(random_data)}')
    print(f'它的方差为{np.var(random_data)}')
    print(f'它的标准差为{np.std(random_data)}')
    print(f'它的极差为{np.ptp(random_data)}')

for i in pro:
    print(i)
    print(pro[i])
    calculate_values(pro[i])
    print()
