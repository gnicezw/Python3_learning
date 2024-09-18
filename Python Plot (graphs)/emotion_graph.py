import matplotlib.pyplot as plt

# Sample Data
x = ['Start', 'Planning', 'Implementation', 'Failure', 'Re-research', 'Success']
y1 = [1, 2, 4, 1, 0, -2]
y2 = [2, 1, 3, 2, 1, 5]

# Create the plot
plt.plot(x, y1, label="Emotional Rollercoaster", color='blue')
plt.plot(x, y2, label="Stable Trajectory", color='orange')

# Label the axis
plt.xlabel('Project Phase')
plt.ylabel('Emotional States')
plt.title('Emotional Progression Through a Project')

# Show the plot
plt.show()