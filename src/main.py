import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet

print("Hello, TAWBA!")

# Sample data creation
dates = pd.date_range(start='2020-01-01', periods=100)
data = np.random.randn(100)

df = pd.DataFrame({'ds': dates, 'y': data})

# Plot the data
plt.figure(figsize=(10, 6))
sns.lineplot(x='ds', y='y', data=df)
plt.title('Sample Data')
plt.show()

# Fit a simple Prophet model
model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
