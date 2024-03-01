
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("dark")
# Create data for the scatter plot
ECT_P = [22, 2, 3, 29, 23, 21]
PST_P = [41/100, 29/100, 38/100, 66/100, 55/100, 55/100]

ECT_NP = [30]
PST_NP = [50/100]

ECT_NF = [31]
PST_NF = [95/100]

# Create scatter plot
plt.figure(figsize=(8, 6))

# Add horizontal line at y=0.5 with text label
# plt.axhline(y=0.5, color='red', linestyle='--', linewidth=1)
plt.text(.2, 0.46, 'PST indicates likely propagation', color='red')

# Add vertical lines at x=10 and x=20 with text labels
plt.text(4, 0.05, 'Hand', color='green')
plt.axvline(x=10, color='green', linestyle='--', linewidth=1)
plt.text(14, 0.05, 'Elbow', color='green')

plt.axvline(x=20, color='green', linestyle='--', linewidth=1)
plt.text(24, 0.05, 'Shoulder', color='green')

sns.scatterplot(x=ECT_P, y=PST_P, label = "ECT propagation")
sns.scatterplot(x=ECT_NP, y=PST_NP, label = "ECT no propagation")
sns.scatterplot(x=ECT_NF, y=PST_NF, label = "ECT no failure")

# Plot linear regression line
sns.regplot(x=ECT_P, y=PST_P, scatter=False, color='blue', label = "Propagation Linear Fit", ci=None)

# Shade the area between y=0 and y=0.5 in red
plt.fill_between(x=range(31), y1=0.49, y2=0, color='red', alpha=0.1)


# Set axis limits
plt.xlim(0, 32)
plt.ylim(0, 1)

# Set axis labels and title
plt.xlabel('ECT Taps')
plt.ylabel('PST Ratio')
plt.title('Comparison of ECT and PST Results')
plt.legend(loc=2)

# Show plot
# plt.grid(True)
plt.show()


# using theil sen and mann-kendall
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import TheilSenRegressor
from scipy.stats import kendalltau
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("dark")
# Create data for the scatter plot
ECT_P = np.array([22, 2, 3, 29, 23, 21])
PST_P = np.array([41/100, 29/100, 38/100, 66/100, 55/100, 55/100])

ECT_NP = [30]
PST_NP = [50/100]

ECT_NF = [31]
PST_NF = [95/100]

# Create scatter plot
plt.figure(figsize=(8, 6))

# Add horizontal line at y=0.5 with text label
plt.text(.2, 0.46, 'PST indicates likely propagation', color='red')

# Shade the area between y=0 and y=0.5 in red
plt.fill_between(x=range(31), y1=0.49, y2=0, color='red', alpha=0.1)


# Add vertical lines at x=10 and x=20 with text labels
plt.text(4, 0.05, 'Hand', color='green')
plt.axvline(x=10, color='green', linestyle='--', linewidth=1)
plt.text(14, 0.05, 'Elbow', color='green')

plt.axvline(x=20, color='green', linestyle='--', linewidth=1)
plt.text(24, 0.05, 'Shoulder', color='green')

sns.scatterplot(x=ECT_P, y=PST_P, label = "ECT propagation")
sns.scatterplot(x=ECT_NP, y=PST_NP, label = "ECT no propagation")
sns.scatterplot(x=ECT_NF, y=PST_NF, label = "ECT no failure")

# Perform Theil-Sen regression
model = TheilSenRegressor()
model.fit(ECT_P.reshape(-1, 1), PST_P)
predicted_values = model.predict(ECT_P.reshape(-1, 1))

# Calculate Kendall's tau and p-value
tau, p_value = kendalltau(ECT_P, PST_P)

# Plot Theil-Sen regression line
plt.plot(ECT_P, predicted_values, color='blue', label=f"Theil-Sen Regression \n Kendall's tau: {tau:.2f}, P-val: {p_value:.2f}")




# Set axis limits
plt.xlim(0, 32)
plt.ylim(0, 1)

# Set axis labels and title
plt.xlabel('ECT Taps')
plt.ylabel('PST Ratio')
plt.title('Comparison of ECT and PST Results')
plt.legend(loc=2)

# Show plot
# plt.grid(True)
plt.show()