Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import numpy as np
... import matplotlib.pyplot as plt
... from scipy.stats import norm
... 
... # 1. Read data
... df = pd.read_csv('data.csv')
... data = df['values'].dropna().values
... 
... # 2. Create histogram
... plt.figure(figsize=(8, 5))
... count, bins, ignored = plt.hist(data, bins=10, density=True, alpha=0.6, color='g')
... 
... # 3. Fit a normal distribution
... mu, sigma = norm.fit(data)
... 
... # 4. Create a range of x values and calculate the PDF
... xmin, xmax = np.min(data), np.max(data)
... x = np.linspace(xmin, xmax, 1000)
... pdf = norm.pdf(x, mu, sigma)
... 
... # 5. Plot the PDF curve
... plt.plot(x, pdf, 'b', linewidth=2, label=f'Normal fit: $\mu={mu:.2f}, \sigma={sigma:.2f}$')
... 
... # 6. Customize and show the plot
... plt.xlabel('Value')
... plt.ylabel('Frequency or Probability')
... plt.title('Histogram with Normal Distribution Fit')
... plt.legend()
... plt.show()
