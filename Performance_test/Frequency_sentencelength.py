import numpy as np
import matplotlib.pyplot as plt

# Define the distribution function
def distribution_function(L):
    return 1.1 * L * (0.90 ** L)

# Generate a range of word counts (L values)
L_values = np.arange(1, 100)  # Assuming word counts range from 1 to 99 for illustration

# Calculate the frequency for each word count
frequencies = distribution_function(L_values)

# Plotting
def plot_with_params(font_size, font_weight, line_color):
    plt.plot(L_values, frequencies, marker='o', color=line_color)
    plt.xlabel('Length of sentence (words)', fontsize=font_size, fontweight=font_weight)
    plt.ylabel('Frequency(%)', fontsize=font_size, fontweight=font_weight)
    plt.title('Test set sentence structure', fontsize=font_size, fontweight=font_weight)
    plt.grid(False)
    plt.show()

# Example usage of the function
plot_with_params(font_size=10, font_weight='normal', line_color='black')

