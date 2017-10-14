import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.switch_backend('agg')
matplotlib.rcParams.update({'font.size': 14})

fold = "reports/"

spec = "(Beta(100_100)F_UnifW)"
#spec = "(BETA(1_0.2)F_Pareto(1.16_1)W)"

file = open("Ind" + spec + ".npy", "rb")

# spec = fold + spec.replace(".","dot")
spec = "tmp/Ind" + spec.replace(".","dot")

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

std_MnEx_CSR = np.load(file)
std_MnEx_NAW = np.load(file)
std_MnEx_PPM = np.load(file)

max_gain_CSR = np.load(file)
max_gain_NAW = np.load(file)
max_gain_PPM = np.load(file)

max_lose_CSR = np.load(file)
max_lose_NAW = np.load(file)
max_lose_PPM = np.load(file)

avg_gain_CSR = np.load(file)
avg_gain_NAW = np.load(file)
avg_gain_PPM = np.load(file)

avg_lose_CSR = np.load(file)
avg_lose_NAW = np.load(file)
avg_lose_PPM = np.load(file)

std_gain_CSR = np.load(file)
std_gain_NAW = np.load(file)
std_gain_PPM = np.load(file)

std_lose_CSR = np.load(file)
std_lose_NAW = np.load(file)
std_lose_PPM = np.load(file)

file.close()

print(avg_MnEx_PPM)

n, d = np.shape(avg_MnEx_CSR)

# Population statistics

plt.figure(1)
plt.errorbar(range_n, avg_MnEx_CSR[:, 0], yerr=std_MnEx_CSR[:, 0], label="CSR", capsize=5)
plt.errorbar(range_n, avg_MnEx_NAW[:, 0], yerr=std_MnEx_NAW[:, 0], label="NAW", capsize=5)
plt.errorbar(range_n, avg_MnEx_PPM[:, 0], yerr=std_MnEx_PPM[:, 0], label="PPM", capsize=5)
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Average Money Exchange")
plt.savefig(spec + "Avg_MnEx(X=1).jpg")

plt.figure(2)
plt.errorbar(range_n, avg_MnEx_CSR[:, 1], yerr=std_MnEx_CSR[:, 1], label="CSR", capsize=5)
plt.errorbar(range_n, avg_MnEx_NAW[:, 1], yerr=std_MnEx_NAW[:, 1], label="NAW", capsize=5)
plt.errorbar(range_n, avg_MnEx_PPM[:, 1], yerr=std_MnEx_PPM[:, 1], label="PPM", capsize=5)
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Average Money Exchange")
plt.savefig(spec + "Avg_MnEx(X=0).jpg")

plt.figure(3)
plt.plot(range_n, max_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, max_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, max_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Max Money Exchange")
plt.savefig(spec + "Max_MnEx(X=1).jpg")

plt.figure(4)
plt.plot(range_n, max_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, max_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, max_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Max Money Exchange")
plt.savefig(spec + "Max_MnEx(X=0).jpg")

plt.figure(5)
plt.plot(range_n, min_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, min_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, min_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Min Money Exchange")
plt.savefig(spec + "Min_MnEx(X=1).jpg")

plt.figure(6)
plt.plot(range_n, min_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, min_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, min_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Min Money Exchange")
plt.savefig(spec + "Min_MnEx(X=0).jpg")

plt.figure(7)
plt.plot(range_n, std_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, std_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, std_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Std of Average Money Exchange")
plt.savefig(spec + "Std_MnEx(X=1).jpg")

plt.figure(8)
plt.plot(range_n, std_MnEx_CSR[:, 1], label="CSR")
plt.plot(range_n, std_MnEx_NAW[:, 1], label="NAW")
plt.plot(range_n, std_MnEx_PPM[:, 1], label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Std of Average Money Exchange")
plt.savefig(spec + "Std_MnEx(X=0).jpg")



# Individual statistics

plt.figure(9)
plt.plot(range_n, max_gain_CSR, label="CSR")
plt.plot(range_n, max_gain_NAW, label="NAW")
plt.plot(range_n, max_gain_PPM, label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Max Gain of Forecasting 1")
plt.savefig(spec + "Max_gain_of_forecasting_1.jpg")

plt.figure(10)
plt.plot(range_n, max_lose_CSR, label="CSR")
plt.plot(range_n, max_lose_NAW, label="NAW")
plt.plot(range_n, max_lose_PPM, label="PPM")
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Max Lose of Forecasting 1")
plt.savefig(spec + "Max_lose_of_forecasting_1.jpg")

plt.figure(11)
plt.errorbar(range_n, avg_gain_CSR, yerr=std_gain_CSR, label="CSR", capsize=5)
plt.errorbar(range_n, avg_gain_NAW, yerr=std_gain_NAW, label="NAW", capsize=5)
plt.errorbar(range_n, avg_gain_PPM, yerr=std_gain_PPM, label="PPM", capsize=5)
plt.legend()
plt.xlabel("# of forecasters (X=1)")
plt.ylabel("Average Gain of Forecasting 1")
plt.savefig(spec + "Avg_gain_of_forecasting_1.jpg")

plt.figure(12)
plt.errorbar(range_n, avg_lose_CSR, yerr=std_lose_CSR, label="CSR", capsize=5)
plt.errorbar(range_n, avg_lose_NAW, yerr=std_lose_NAW, label="NAW", capsize=5)
plt.errorbar(range_n, avg_lose_PPM, yerr=std_lose_PPM, label="PPM", capsize=5)
plt.legend()
plt.xlabel("# of forecasters (X=0)")
plt.ylabel("Average Lose of Forecasting 1")
plt.savefig(spec + "Avg_lose_of_forecasting_1.jpg")
