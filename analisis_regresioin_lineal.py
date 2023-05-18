import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

symbol = "BTC-USD"
data = yf.download(symbol, start="2020-12-01", end="2023-05-15")
df = pd.DataFrame(data['Close'])
df.reset_index(inplace=True)

# Convertir la columna de fechas a un tipo de datos compatible con float64
X_train = (df['Date'][:int(len(df)*0.8)].values.astype(np.int64) // 10**9).reshape(-1, 1)
y_train = df['Close'][:int(len(df)*0.8)].values.reshape(-1,1)

X_test = (df['Date'][int(len(df)*0.8):].values.astype(np.int64) // 10**9).reshape(-1, 1)
y_test = df['Close'][int(len(df)*0.8):].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)

plt.scatter(X_train, y_train, color='blue')
plt.scatter(X_test, y_test, color='green')
plt.plot(X_test, y_pred, color='red')
plt.show()

print(" A predicted price of: $", int(y_pred[0][0]) )