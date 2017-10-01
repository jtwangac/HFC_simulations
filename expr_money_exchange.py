import time
import numpy as np
import scores as sc  # source: scores.py
import wager as wg  # source: wagers.py
# import matplotlib.pyplot as plt


np.set_printoptions(precision=3, suppress=True)

start_time = time.time()

# Set the number of realizations of a future event
EPS = 0.00001
d = 2  # # of realizations of a future event

running_times = 1000
range_n = range(5, 51, 5)

avg_MnEx_CSR = []; avg_MnEx_NAW = []; avg_MnEx_PPM = []
max_MnEx_CSR = []; max_MnEx_NAW = []; max_MnEx_PPM = []
min_MnEx_CSR = []; min_MnEx_NAW = []; min_MnEx_PPM = []

for n in range_n:
    print("# of agents: ", n)
    MnEx_CSR = np.zeros((running_times, d))
    MnEx_NAW = np.zeros((running_times, d))
    MnEx_PPM = np.zeros((running_times, d))
    for t in range(running_times):
        # Generate forecasters' true believes and each row represents one belief
        # forecasts = np.random.dirichlet(np.ones((d,)), size=n)
        forecasts = np.random.dirichlet([1,0.2], size=n)
        # forecasts = np.random.beta(0.3, 0.3, size=n)
        # print(forecasts)

        # Generate forecasters' wagers
        wagers = np.ones((n,))
        total_wager = np.sum(wagers)

        # Compute the outcome of no-arbitage wagering mechanism under each realization
        net_pays_CSR = sc.competitive_score_rule(sc.Brier_score(forecasts, 2, -1)) / 2
        net_pays_NAW = wg.no_arbitage_wagering(forecasts[:, 0], wagers)
        net_pays_PPM = wg.net_payoff_PPM(forecasts, wagers)
        MnEx_CSR_PS, MnEx_NAW_PS, MnEx_PPM_PS = (np.array(net_pays_CSR),
                                                 np.array(net_pays_NAW),
                                                 np.array(net_pays_PPM))
        MnEx_CSR_NG, MnEx_NAW_NG, MnEx_PPM_NG = (np.array(net_pays_CSR),
                                                 np.array(net_pays_NAW),
                                                 np.array(net_pays_PPM))
        # print(net_pays_CSR)
        # print(net_pays_NAW)
        # print(net_pays_PPM)

        MnEx_CSR_PS[MnEx_CSR_PS <= EPS] = 0; MnEx_CSR_NG[MnEx_CSR_NG > EPS] = 0
        MnEx_NAW_PS[MnEx_NAW_PS <= EPS] = 0; MnEx_NAW_NG[MnEx_NAW_NG > EPS] = 0
        MnEx_PPM_PS[MnEx_PPM_PS <= EPS] = 0; MnEx_PPM_NG[MnEx_PPM_NG > EPS] = 0

        MnEx_CSR_PS = np.sum(MnEx_CSR_PS, axis=0) / total_wager
        MnEx_CSR_NG = np.sum(MnEx_CSR_NG, axis=0) / total_wager
        MnEx_NAW_PS = np.sum(MnEx_NAW_PS, axis=0) / total_wager
        MnEx_NAW_NG = np.sum(MnEx_NAW_NG, axis=0) / total_wager
        MnEx_PPM_PS = np.sum(MnEx_PPM_PS, axis=0) / total_wager
        MnEx_PPM_NG = np.sum(MnEx_PPM_NG, axis=0) / total_wager
        # print(MnEx_CSR_PS, MnEx_CSR_NG)
        # print(MnEx_NAW_PS, MnEx_NAW_NG)
        # print(MnEx_PPM_PS, MnEx_PPM_NG)

        MnEx_CSR[t, :] = MnEx_CSR_PS
        MnEx_NAW[t, :] = -MnEx_NAW_NG
        MnEx_PPM[t, :] = MnEx_PPM_PS

    avg_MnEx_CSR.append(np.average(MnEx_CSR, axis=0))
    max_MnEx_CSR.append(np.max(MnEx_CSR, axis=0))
    min_MnEx_CSR.append(np.min(MnEx_CSR, axis=0))

    avg_MnEx_NAW.append(np.average(MnEx_NAW, axis=0))
    max_MnEx_NAW.append(np.max(MnEx_NAW, axis=0))
    min_MnEx_NAW.append(np.min(MnEx_NAW, axis=0))

    avg_MnEx_PPM.append(np.average(MnEx_PPM, axis=0))
    max_MnEx_PPM.append(np.max(MnEx_PPM, axis=0))
    min_MnEx_PPM.append(np.min(MnEx_PPM, axis=0))

loop_time = time.time() - start_time
print(loop_time)

avg_MnEx_CSR, max_MnEx_CSR, min_MnEx_CSR = (np.array(avg_MnEx_CSR),
                                            np.array(max_MnEx_CSR),
                                            np.array(min_MnEx_CSR))
avg_MnEx_NAW, max_MnEx_NAW, min_MnEx_NAW = (np.array(avg_MnEx_NAW),
                                            np.array(max_MnEx_NAW),
                                            np.array(min_MnEx_NAW))
avg_MnEx_PPM, max_MnEx_PPM, min_MnEx_PPM = (np.array(avg_MnEx_PPM),
                                            np.array(max_MnEx_PPM),
                                            np.array(min_MnEx_PPM))

file = open("(Beta_1_0.2)expr_money_exchange.npy", "wb")
np.save(file, range_n)

np.save(file, avg_MnEx_CSR)
np.save(file, avg_MnEx_NAW)
np.save(file, avg_MnEx_PPM)

np.save(file, max_MnEx_CSR)
np.save(file, max_MnEx_NAW)
np.save(file, max_MnEx_PPM)

np.save(file, min_MnEx_CSR)
np.save(file, min_MnEx_NAW)
np.save(file, min_MnEx_PPM)

file.close()

'''
file = open("expr_money_exchange.npy","rb")
print(np.load(file))
print(np.load(file))
print(np.load(file))
print(avg_MnEx_CSR)

plt.figure(1)
plt.plot(range_n, avg_MnEx_CSR[:, 0], label="CSR")
plt.plot(range_n, avg_MnEx_NAW[:, 0], label="NAW")
plt.plot(range_n, avg_MnEx_PPM[:, 0], label="PPM")
plt.legend()
plt.xlabel("# of forecasters")
plt.ylabel("Average Money Exchange if the event happens")
plt.show()
'''