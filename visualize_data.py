import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data from the database
conn = sqlite3.connect('sensor_data.db')
data = pd.read_sql_query("SELECT * FROM data", conn)

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data['timestamp'], data['turbidity'], label='Turbidity')
plt.xlabel('Time')
plt.ylabel('Turbidity Value')
plt.title('Water Turbidity Over Time')
plt.legend()
plt.show()
