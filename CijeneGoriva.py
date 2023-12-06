import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates


data = {
    'Datumi': ['20/1', '30/1/','14/2','27/2','14/3','27/3', '10/4','25/4','9/5', '23/5', '6/6', '20/6', '6/4', '18/7', '10/8', '14/8', '29/8', '12/09', '29/09', '10/10', '24/10', '07/11', '21/11', '5/12'],
    'Cijene Dizela':  [1.46, 1.51, 1.39, 1.38, 1.33, 1.34, 1.33, 1.31, 1.23, 1.24, 1.28, 1.30, 1.34, 1.36, 1.41, 1.51, 1.52, 1.55, 1.62, 1.59, 1.56, 1.52, 1.46, 1.44]
}

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(left=0.1, bottom=0.15, right=0.9, top=0.9)

# Create a scatter plot and line plot of the gas prices over time

#ax.scatter(data['Datumi'], data['Cijene Benzina'])
#ax.plot(data['Datumi'], data['Cijene Benzina'], label='Benzin', color='g')

# Create a scatter plot and line plot of the diesel prices over time
ax.scatter(data['Datumi'], data['Cijene Dizela'])
ax.plot(data['Datumi'], data['Cijene Dizela'], label='Dizel', color='r')

#ax.scatter(data['Datumi'], data['Plavi'])
#ax.plot(data['Datumi'], data['Plavi'], label='Plavi', color='b')

# Add labels and title
ax.set_xlabel('Datum')
ax.set_ylabel('Cijena (€)')
ax.set_title('Cijene Goriva Po Litri')

# Add annotations for each point
for i in range(len(data['Datumi'])):
    
    ax.annotate(f"{data['Cijene Dizela'][i]:.2f}", (data['Datumi'][i], data['Cijene Dizela'][i]))
plt.xticks(rotation=45)

# Add a legend
ax.legend()

# Display the plot
plt.show()
"""



# Example data
data = {
    'Datumi': ['20/1', '30/1/','14/2','27/2','14/3','27/3', '10/4','25/4','9/5', '23/5', '6/6', '20/6', '6/4', '18/7', '10/8', '14/8', '29/8', '12/09', '27/09', '10/10', '24/10', '07/11', '21/11', '5/12'],
    'Cijene Dizela':  [1.46, 1.51, 1.39, 1.38, 1.33, 1.34, 1.33, 1.31, 1.23, 1.24, 1.28, 1.30, 1.34, 1.36, 1.41, 1.51, 1.52, 1.55, 1.62, 1.59, 1.56, 1.52, 1.46, 1.44],
    'Cijene Benzina': [1.34, 1.41, 1.38, 1.38, 1.43, 1.39, 1.43, 1.4, 1.32, 1.32, 1.38, 1.40, 1.44, 1.46, 1.51, 1.54, 1.57, 1.58, 1.62, 1.51, 1.46, 1.46, 1.44, 1.43],
    'Plavi': [0.96, 1.01, 0.89, 0.88, 0.83, 0.84, 0.83, 0.81, 0.73, 0.74, 0.78, 0.8, 0.8, 0.83, 0.87, 0.98, 0.99, 1.01, 1.08, 1.05, 1.02, 0.98, 0.92, 0.90]
}

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(left=0.1, bottom=0.15, right=0.9, top=0.9)

# Create a scatter plot and line plot of the gas prices over time

ax.scatter(data['Datumi'], data['Cijene Benzina'])
ax.plot(data['Datumi'], data['Cijene Benzina'], label='Benzin', color='g')

# Create a scatter plot and line plot of the diesel prices over time
ax.scatter(data['Datumi'], data['Cijene Dizela'])
ax.plot(data['Datumi'], data['Cijene Dizela'], label='Dizel', color='r')

ax.scatter(data['Datumi'], data['Plavi'])
ax.plot(data['Datumi'], data['Plavi'], label='Plavi', color='b')

# Add labels and title
ax.set_xlabel('Datum')
ax.set_ylabel('Cijena (€)')
ax.set_title('Cijene Goriva Po Litri')

# Add annotations for each point
for i in range(len(data['Datumi'])):
    
    ax.annotate(f"{data['Cijene Dizela'][i]:.2f}", (data['Datumi'][i], data['Cijene Dizela'][i]))

    ax.annotate(f"{data['Cijene Benzina'][i]:.2f}", (data['Datumi'][i], data['Cijene Benzina'][i]))
    ax.annotate(f"{data['Cijene Dizela'][i]:.2f}", (data['Datumi'][i], data['Cijene Dizela'][i]))
    ax.annotate(f"{data['Plavi'][i]:.2f}", (data['Datumi'][i], data['Plavi'][i]))
plt.xticks(rotation=45)

# Add a legend
ax.legend()

# Display the plot
plt.show()

"""