import pandas as pd
import matplotlib.pylab as plt


from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
datas = pd.read_csv('data/RhodeIslandCO.csv', header=0, usecols=['Date Local', 'CO Mean'], parse_dates=['Date Local'], index_col='Date Local', date_parser=dateparse)
print(datas)


dataValues = datas.values
train, test = dataValues[0:int(len(dataValues) * 0.80)], dataValues[int(len(dataValues) * 0.80):len(dataValues)]
trainingData = [x for x in train]
predictions = []

for item in range(len(test)):
    model = ARIMA(trainingData, order=(5,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    predicted = output[0]
    predictions.append(predicted)
    observation = test[item]
    trainingData.append(observation)
    print('predicted=%f, expected=%f' % (predicted, observation))

error = mean_squared_error(test[0:960], predictions)
print('Test MSE: %.3f' % error)

plt.plot(test, label='Actual')
plt.title('ARIMA Predictions Rhode Island')
plt.ylabel('CO')
plt.xlabel('Number of Months')
plt.plot(predictions, color='Brown',label='Prediction')
plt.legend(loc='best')
plt.show()
plt.savefig('Test_MSE.png')
