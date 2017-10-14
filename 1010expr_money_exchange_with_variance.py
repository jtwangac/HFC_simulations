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
range_n = range(5, 31, 5)

avg_MnEx_CSR = []; avg_MnEx_NAW = []; avg_MnEx_PPM = []
max_MnEx_CSR = []; max_MnEx_NAW = []; max_MnEx_PPM = []
min_MnEx_CSR = []; min_MnEx_NAW = []; min_MnEx_PPM = []
std_MnEx_CSR = []; std_MnEx_NAW = []; std_MnEx_PPM = []

max_gain_CSR = []; max_gain_NAW = []; max_gain_PPM = []
max_lose_CSR = []; max_lose_NAW = []; max_lose_PPM = []

avg_gain_CSR = []; avg_gain_NAW = []; avg_gain_PPM = []
avg_lose_CSR = []; avg_lose_NAW = []; avg_lose_PPM = []

std_gain_CSR = []; std_gain_NAW = []; std_gain_PPM = []
std_lose_CSR = []; std_lose_NAW = []; std_lose_PPM = []

for n in range_n:
    print("# of agents: ", n)
    MnEx_CSR = np.zeros((running_times, d))
    MnEx_NAW = np.zeros((running_times, d))
    MnEx_PPM = np.zeros((running_times, d))

    # forecast complete right or wrong by forecasting 1
    complete_right_CSR = np.zeros((running_times,))
    complete_wrong_CSR = np.zeros((running_times,))
    complete_right_NAW = np.zeros((running_times,))
    complete_wrong_NAW = np.zeros((running_times,))
    complete_right_PPM = np.zeros((running_times,))
    complete_wrong_PPM = np.zeros((running_times,))

    for t in range(running_times):
        # Generate forecasters' true believes and each row represents one belief
        # forecasts = np.random.dirichlet(np.ones((d,)), size=n)
        # forecasts = np.random.dirichlet([0.2, 1], size=n)
        forecasts = np.random.dirichlet([100, 100], size=n)
        # forecasts = np.random.dirichlet([0.3, 0.3], size=n)
        forecasts[0, :] = [1, 0]
        # print(forecasts)

        # Generate forecasters' wagers
        wagers = np.ones((n,))
        # wagers = np.random.beta(100, 100, size=n)
        # wagers = (np.random.pareto(1.16, size=n) + 1) * 1
        total_wager = np.sum(wagers)

        # Compute the outcome of no-arbitage wagering mechanism under each realization
        net_pays_CSR = sc.competitive_score_rule(sc.Brier_score(forecasts, 2, -1)) / 2
        net_pays_NAW = wg.no_arbitage_wagering(forecasts[:, 0], wagers)
        net_pays_PPM = wg.net_payoff_PPM(forecasts, wagers)

        # value duplication for further modification
        MnEx_CSR_PS, MnEx_NAW_PS, MnEx_PPM_PS = (np.array(net_pays_CSR),
                                                 np.array(net_pays_NAW),
                                                 np.array(net_pays_PPM))
        MnEx_CSR_NG, MnEx_NAW_NG, MnEx_PPM_NG = (np.array(net_pays_CSR),
                                                 np.array(net_pays_NAW),
                                                 np.array(net_pays_PPM))
        # print(net_pays_CSR)
        # print(net_pays_NAW)
        # print(net_pays_PPM)

        complete_right_CSR[t] = net_pays_CSR[0, 0]
        complete_wrong_CSR[t] = net_pays_CSR[0, 1]
        complete_right_NAW[t] = net_pays_NAW[0, 0]
        complete_wrong_NAW[t] = net_pays_NAW[0, 1]
        complete_right_PPM[t] = net_pays_PPM[0, 0]
        complete_wrong_PPM[t] = net_pays_PPM[0, 1]

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

    # Population statistics
    avg_MnEx_CSR.append(np.average(MnEx_CSR, axis=0))
    max_MnEx_CSR.append(np.max(MnEx_CSR, axis=0))
    min_MnEx_CSR.append(np.min(MnEx_CSR, axis=0))
    std_MnEx_CSR.append(np.std(MnEx_CSR, axis=0))

    avg_MnEx_NAW.append(np.average(MnEx_NAW, axis=0))
    max_MnEx_NAW.append(np.max(MnEx_NAW, axis=0))
    min_MnEx_NAW.append(np.min(MnEx_NAW, axis=0))
    std_MnEx_NAW.append(np.std(MnEx_NAW, axis=0))

    avg_MnEx_PPM.append(np.average(MnEx_PPM, axis=0))
    max_MnEx_PPM.append(np.max(MnEx_PPM, axis=0))
    min_MnEx_PPM.append(np.min(MnEx_PPM, axis=0))
    std_MnEx_PPM.append(np.std(MnEx_PPM, axis=0))

    # Individual statistics
    # convert min lose of neg value to max lose of absolue value
    max_gain_CSR.append(np.amax(complete_right_CSR) / wagers[0])
    max_lose_CSR.append(np.amax(-complete_wrong_CSR) / wagers[0])
    max_gain_NAW.append(np.amax(complete_right_NAW) / wagers[0])
    max_lose_NAW.append(np.amax(-complete_wrong_NAW) / wagers[0])
    max_gain_PPM.append(np.amax(complete_right_PPM) / wagers[0])
    max_lose_PPM.append(np.amax(-complete_wrong_PPM) / wagers[0])

    avg_gain_CSR.append(np.average(complete_right_CSR) / wagers[0])
    avg_lose_CSR.append(np.average(-complete_wrong_CSR) / wagers[0])
    avg_gain_NAW.append(np.average(complete_right_NAW) / wagers[0])
    avg_lose_NAW.append(np.average(-complete_wrong_NAW) / wagers[0])
    avg_gain_PPM.append(np.average(complete_right_PPM) / wagers[0])
    avg_lose_PPM.append(np.average(-complete_wrong_PPM) / wagers[0])


    std_gain_CSR.append(np.std(complete_right_CSR) / wagers[0])
    std_lose_CSR.append(np.std(-complete_wrong_CSR) / wagers[0])
    std_gain_NAW.append(np.std(complete_right_NAW) / wagers[0])
    std_lose_NAW.append(np.std(-complete_wrong_NAW) / wagers[0])
    std_gain_PPM.append(np.std(complete_right_PPM) / wagers[0])
    std_lose_PPM.append(np.std(-complete_wrong_PPM) / wagers[0])


loop_time = time.time() - start_time
print(loop_time)

avg_MnEx_CSR, max_MnEx_CSR, min_MnEx_CSR, std_MnEx_CSR = (
                                            np.array(avg_MnEx_CSR),
                                            np.array(max_MnEx_CSR),
                                            np.array(min_MnEx_CSR),
                                            np.array(std_MnEx_CSR))
avg_MnEx_NAW, max_MnEx_NAW, min_MnEx_NAW, std_MnEx_NAW = (
                                            np.array(avg_MnEx_NAW),
                                            np.array(max_MnEx_NAW),
                                            np.array(min_MnEx_NAW),
                                            np.array(std_MnEx_NAW))
avg_MnEx_PPM, max_MnEx_PPM, min_MnEx_PPM, std_MnEx_PPM = (
                                            np.array(avg_MnEx_PPM),
                                            np.array(max_MnEx_PPM),
                                            np.array(min_MnEx_PPM),
                                            np.array(std_MnEx_PPM))

max_gain_CSR, max_gain_NAW, max_gain_PPM = (np.array(max_gain_CSR),
                                            np.array(max_gain_NAW),
                                            np.array(max_gain_PPM))
max_lose_CSR, max_lose_NAW, max_lose_PPM = (np.array(max_lose_CSR),
                                            np.array(max_lose_NAW),
                                            np.array(max_lose_PPM))
std_gain_CSR, std_gain_NAW, std_gain_PPM = (np.array(std_gain_CSR),
                                            np.array(std_gain_NAW),
                                            np.array(std_gain_PPM))
std_lose_CSR, std_lose_NAW, std_lose_PPM = (np.array(std_lose_CSR),
                                            np.array(std_lose_NAW),
                                            np.array(std_lose_PPM))

file = open("Ind(Beta(100_100)F_UnifW).npy", "wb")
np.save(file, range_n)

# Population statistics
np.save(file, avg_MnEx_CSR)
np.save(file, avg_MnEx_NAW)
np.save(file, avg_MnEx_PPM)

np.save(file, max_MnEx_CSR)
np.save(file, max_MnEx_NAW)
np.save(file, max_MnEx_PPM)

np.save(file, min_MnEx_CSR)
np.save(file, min_MnEx_NAW)
np.save(file, min_MnEx_PPM)

np.save(file, std_MnEx_CSR)
np.save(file, std_MnEx_NAW)
np.save(file, std_MnEx_PPM)


# Individual statistics
np.save(file, max_gain_CSR)
np.save(file, max_gain_NAW)
np.save(file, max_gain_PPM)

np.save(file, max_lose_CSR)
np.save(file, max_lose_NAW)
np.save(file, max_lose_PPM)

np.save(file, avg_gain_CSR)
np.save(file, avg_gain_NAW)
np.save(file, avg_gain_PPM)

np.save(file, avg_lose_CSR)
np.save(file, avg_lose_NAW)
np.save(file, avg_lose_PPM)


np.save(file, std_gain_CSR)
np.save(file, std_gain_NAW)
np.save(file, std_gain_PPM)

np.save(file, std_lose_CSR)
np.save(file, std_lose_NAW)
np.save(file, std_lose_PPM)

file.close()
