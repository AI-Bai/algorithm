import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt

# data = [253993, 275396.2, 315229.5, 356949.6, 400158.2, 442431.7, 495102.9, 570164.8, 640993.1, 704250.4, 767455.4,
#         781807.8, 776332.3, 794161.7, 834177.7, 931651.5, 1028390, 1114914]

data = [676, 825, 774, 716, 940, 1159, 1384, 1542, 1668, 1688, 1958, 2031, 2234, 2566, 2820, 3006, 3093, 3277, 3514,
        3770, 4107]
plt.plot(data)

# Simple Exponential Smoothing(简单指数平滑)
# 在fit1中，我们明确地为模型提供了平滑参数α=0.2
fit1 = SimpleExpSmoothing(data).fit(smoothing_level=0.2, optimized=False)
# plot
l1, = plt.plot(list(fit1.fittedvalues) + list(fit1.forecast(5)), marker='o')

# 在fit2中，我们选择α=0.6
fit2 = SimpleExpSmoothing(data).fit(smoothing_level=0.6, optimized=False)
# plot
l2, = plt.plot(list(fit2.fittedvalues) + list(fit2.forecast(5)), marker='o')

# 在fit3中，我们使用自动优化，允许statsmodels自动为我们找到优化值。 这是推荐的方法。
fit3 = SimpleExpSmoothing(data).fit()
# plot
l3, = plt.plot(list(fit3.fittedvalues) + list(fit3.forecast(5)), marker='o')

l4, = plt.plot(data, marker='o')
plt.legend(handles=[l1, l2, l3, l4], labels=['a=0.2', 'a=0.6', 'auto', 'data'], loc='best', prop={'size': 7})
plt.show()

# Holt’s Method(二次指数平滑)
data_sr = pd.Series(data)

# 在fit1中，我们明确地为模型提供了平滑参数α=0.8，β∗=0.2。
fit1 = Holt(data_sr).fit(smoothing_level=0.8, smoothing_slope=0.2, optimized=False)
l1, = plt.plot(list(fit1.fittedvalues) + list(fit1.forecast(5)), marker='^')

# 在fit2中，我们使用指数模型而不是Holt的加法模型（默认值）。
fit2 = Holt(data_sr, exponential=True).fit(smoothing_level=0.8, smoothing_slope=0.2, optimized=False)
l2, = plt.plot(list(fit2.fittedvalues) + list(fit2.forecast(5)), marker='.')

# 在fit3中，我们使用阻尼版本的Holt附加模型，但允许优化阻尼参数φ，同时固定α=0.8，β∗=0.2的值。
fit3 = Holt(data_sr, damped=True).fit(smoothing_level=0.8, smoothing_slope=0.2)
l3, = plt.plot(list(fit3.fittedvalues) + list(fit3.forecast(5)), marker='.')

# 添加原始数据作为对比
l4, = plt.plot(data_sr, marker='.')
plt.legend(handles=[l1, l2, l3, l4],
           labels=["Holt's linear trend", "Exponential trend", "Additive damped trend", 'data'], loc='best',
           prop={'size': 7})
plt.show()

# Holt-Winters 方法(三次指数平滑)
data_sr = pd.Series(data)
# 在fit1中，我们使用加法趋势，周期season_length = 4的加性季节和Box-Cox变换。
fit1 = ExponentialSmoothing(data_sr, seasonal_periods=4, trend='add', seasonal='add').fit(use_boxcox=True)

# 在fit2中，我们使用加法趋势，周期season_length = 4的乘法季节和Box-Cox变换。
fit2 = ExponentialSmoothing(data_sr, seasonal_periods=4, trend='add', seasonal='mul').fit(use_boxcox=True)

# 在fit3中，我们使用加性阻尼趋势，周期season_length = 4的加性季节和Box-Cox变换。
fit3 = ExponentialSmoothing(data_sr, seasonal_periods=4, trend='add', seasonal='add', damped=True).fit(use_boxcox=True)

# 在fit4中，我们使用加性阻尼趋势，周期season_length = 4的乘法季节和Box-Cox变换。
fit4 = ExponentialSmoothing(data_sr, seasonal_periods=4, trend='add', seasonal='mul', damped=True).fit(use_boxcox=True)

l1, = plt.plot(list(fit1.fittedvalues) + list(fit1.forecast(5)), marker='^')
l2, = plt.plot(list(fit2.fittedvalues) + list(fit2.forecast(5)), marker='*')
l3, = plt.plot(list(fit3.fittedvalues) + list(fit3.forecast(5)), marker='.')
l4, = plt.plot(list(fit4.fittedvalues) + list(fit4.forecast(5)), marker='.')

l5, = plt.plot(data, marker='.')
plt.legend(handles=[l1, l2, l3, l4, l5], labels=["aa", "am", "aa damped", "am damped", "data"], loc='best',
           prop={'size': 7})

plt.show()
