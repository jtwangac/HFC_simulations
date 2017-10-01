import numpy as np
import scores as sc  #source: scores.py
import wager as wg  #source: wagers.py
import matplotlib.pyplot as plt


# Set the number of realizations of a future event
d = 2  # # of realizations of a future event

running_times = 1000
range_n = range(5, 51, 5)
average_average = []
average_max = []
average_min = []
max_max = []
for n in range_n:
    forecaster_average_risk = np.zeros((running_times,))
    forecaster_max_risk = np.zeros((running_times,))
    forecaster_min_risk = np.zeros((running_times,))
    for t in range(running_times):
        # Generate forecasters' true believes and each row represents one belief
        forecasts = np.random.dirichlet(np.ones((d,)), size=n)

        # Generate forecasters' wagers
        wagers = np.random.rand(n)
        wagers = np.ones((n,))

        # Compute the outcome of no-arbitage wagering mechanism under each realization
        net_payoffs = wg.no_arbitage_wagering(forecasts[:, 0], wagers)
        # print(net_payoffs)
        # exchanges = np.absolute(net_payoffs[:,0]/wagers)
        # print(exchanges)
        risks = np.max(-net_payoffs, axis=1)
        forecaster_average_risk[t] = np.sum(risks) / np.sum(wagers)
        forecaster_max_risk[t] = np.max(risks)
        forecaster_min_risk[t] = np.min(risks)
    average_average.append(np.average(forecaster_average_risk))
    average_max.append(np.average(forecaster_max_risk))
    average_min.append(np.average(forecaster_min_risk))
    max_max.append(np.max(forecaster_max_risk))

#print(average_average)
plt.plot(range_n, average_average, label="average sum(risks)/sum(wagers)")
plt.legend()
plt.xlabel("# of forecasters")
plt.ylabel("sum(risks)/sum(wagers)")
plt.show()
