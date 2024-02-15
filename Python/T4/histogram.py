import matplotlib.pyplot as plt
data=[1,3,3,3,3,9,9,5,4,4,8,8,8,6,7]
plt.hist(data,color="yellow",orientation="horizontal",align='mid',bins=4)
plt.title("Histogram")
plt.show()
