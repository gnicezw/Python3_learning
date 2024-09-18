import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

# Sample Data
x = ['define', 'measure', 'analyse', 'implement', 'verify','redesign', 'Success']
y1 = [1, 2, 0, 1, 4, 0, -2]
y2 = [1, 1, 3, 2, 2, 1, 5]

# Convert x to numerical values for spline interpolation
x_smooth = range(len(x))

# Create splines
spline1 = make_interp_spline(x_smooth, y1)
spline2 = make_interp_spline(x_smooth, y2)

# Sample new x values for smoother curve
x_new = np.linspace(0, len(x) - 1, num=100, endpoint=True)

# Generate interpolated y values
y1_smooth = spline1(x_new)
y2_smooth = spline2(x_new)

# Create the plot
plt.plot(x_new, y1_smooth, label="Emotional Rollercoaster", color='red')
plt.plot(x_new, y2_smooth, label="Stable Trajectory", color='blue')

# Label the axis
plt.xlabel('Project Phase')
plt.ylabel('Emotional States')
plt.title('Emotional Progression Through a Project')

# Show the plot
plt.show()
