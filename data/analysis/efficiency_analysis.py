import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/operations_data.csv')

data['Defect_Rate (%)'] = (data['Defective_Units'] / data['Units_Produced']) * 100

print(data)

plt.figure()
plt.plot(data['Day'], data['Defect_Rate (%)'])
plt.xlabel('Day')
plt.ylabel('Defect Rate (%)')
plt.title('Daily Defect Rate Trend')
plt.show()
