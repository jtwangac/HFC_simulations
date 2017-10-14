import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.switch_backend('agg')
matplotlib.rcParams.update({'font.size': 14})

fold = "reports/"

spec = "(Beta(0.3_0.3)F_Pareto(1.16_1)W)"
#spec = "(Beta(1_0.2)F_Pareto(1.16_1)W)"

file = open("MnEx" + spec + ".npy", "rb")

spec = fold + spec.replace(".","dot")

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

max_gain_CSR = np.load(file)
max_gain_NAW = np.load(file)
max_gain_PPM = np.load(file)

min_gain_CSR = np.load(file)
min_gain_NAW = np.load(file)
min_gain_PPM = np.load(file)

file.close()

print(avg_MnEx_PPM)

n, d = np.shape(avg_MnEx_CSR)

plt.figure(1)
#plt.plot(range_n, avg_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, avg_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, avg_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Average Money Exchange")
plt.savefig(spec + "Avg_MnEx(X=1).jpg")

plt.figure(2)
#plt.plot(range_n, avg_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, avg_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, avg_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Average Money Exchange")
plt.savefig(spec + "Avg_MnEx(X=0).jpg")

plt.figure(3)
#plt.plot(range_n, max_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, max_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, max_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Max Money Exchange")
plt.savefig(spec + "Max_MnEx(X=1).jpg")

plt.figure(4)
#plt.plot(range_n, max_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, max_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, max_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Max Money Exchange")
plt.savefig(spec + "Max_MnEx(X=0).jpg")

plt.figure(5)
#plt.plot(range_n, min_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, min_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, min_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Min Money Exchange")
plt.savefig(spec + "Min_MnEx(X=1).jpg")

plt.figure(6)
#plt.plot(range_n, min_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, min_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, min_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Min Money Exchange")
plt.savefig(spec + "Min_MnEx(X=0).jpg")

'''
plt.figure(7)
plt.plot(range_n, max_gain_CSR, label="CSR")
plt.plot(range_n, max_gain_NAW, label="NAW")
plt.plot(range_n, max_gain_PPM, label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Max Gain of Forecasting 1")
plt.savefig(spec + "Max_gain_of_forecasting_1.jpg")

plt.figure(8)
plt.plot(range_n, min_gain_CSR, label="CSR")
plt.plot(range_n, min_gain_NAW, label="NAW")
plt.plot(range_n, min_gain_PPM, label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Max Lose of Forecasting 1")
plt.savefig(spec + "Max_lose_of_forecasting_1.jpg")
'''