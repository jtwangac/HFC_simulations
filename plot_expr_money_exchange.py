import numpy as np
import matplotlib.pyplot as plt

file = open("(Beta_1_0.2)expr_money_exchange.npy", "rb")
range_n = np.load(file)

avg_MnEx_CSR = np.load(file)
avg_MnEx_NAW = np.load(file)
avg_MnEx_PPM = np.load(file)

max_MnEx_CSR = np.load(file)
max_MnEx_NAW = np.load(file)
max_MnEx_PPM = np.load(file)

min_MnEx_CSR = np.load(file)
min_MnEx_NAW = np.load(file)
min_MnEx_PPM = np.load(file)

file.close()

print(avg_MnEx_PPM)

n, d = np.shape(avg_MnEx_CSR)

plt.figure(1)
plt.plot(range_n, avg_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, avg_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, avg_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Average Money Exchange")
plt.savefig("Avg_MnEx(X=1).jpg")

plt.figure(2)
plt.plot(range_n, avg_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, avg_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, avg_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Average Money Exchange")
plt.savefig("Avg_MnEx(X=0).jpg")

plt.figure(3)
plt.plot(range_n, max_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, max_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, max_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Max Money Exchange")
plt.savefig("Max_MnEx(X=1).jpg")

plt.figure(4)
plt.plot(range_n, max_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, max_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, max_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Max Money Exchange")
plt.savefig("Max_MnEx(X=0).jpg")

plt.figure(5)
plt.plot(range_n, min_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, min_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, min_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Min Money Exchange")
plt.savefig("Min_MnEx(X=1).jpg")

plt.figure(6)
plt.plot(range_n, min_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, min_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, min_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Min Money Exchange")
plt.savefig("Min_MnEx(X=0).jpg")
