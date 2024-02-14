import matplotlib.pyplot as plt
import numpy as np

x=np.array(['PS','DE','PYTHON','FSD','ETC'])
y1=np.array([10,12,13,14,11])
y2=np.array([22,21,24,20,19])
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Results")
plt.plot(x,y1,label="Chirag")
plt.plot(x,y2,label="Yasvi")
plt.legend()
plt.show()
