import time
import numpy as np
import scores as sc  # source: scores.py
import wager as wg  # source: wagers.py
import matplotlib.pyplot as plt

np.set_printoptions(precision=5, suppress=True)

n_other = 3
f_other = np.random.rand(n_other)
w_other = np.ones((n_other,))
f = 0.6
forecasts = np.hstack((f, f_other))

w_samples = np.linspace(0.1, 100, num=1000)

pay = np.zeros((2, len(w_samples)))
for i, w in enumerate(w_samples):
    wagers = np.hstack((w, w_other))
    net_pay = wg.no_arbitage_wagering(forecasts, wagers)
    pay[:, i] = net_pay[0, :]


plt.figure(1)
plt.plot(w_samples, pay[0, :])
plt.plot(w_samples, pay[1, :])
plt.show()


#net_pay = wg.no_arbitage_wagering(forecasts, wagers)
#print(net_pay)

'''
fRange = [0.05 * i for i in range(21)]
wRange = [i + 1 for i in range(3)]
botFRange = [0.1 * i for i in range(11)]

for f1 in fRange:
    for w1 in wRange:
        for f2 in botFRange:
            for f3 in botFRange:
                for w2 in wRange:
                    for w3 in wRange:
                        forecasts = np.array([[f1, 1 - f1],
                                              [f2, 1 - f2],
                                              [f3, 1 - f3]])
                        wagers = np.array([w1 * 1.0, w2, w3])
                        net_pay, bet = wg.net_payoff_PPM(forecasts, wagers)
                        p1, p2, p3 = net_pay[0, :], net_pay[1, :], net_pay[2, :]
                        db.insert({'worker_forecast': "%.2f" % f1,
                                   'worker_wager': "%.2f" % w1,
                                   'worker_netpay0': "%.2f" % p1[0],
                                   'worker_netpay1': "%.2f" % p1[1],
                                   'worker_bets': ["%.2f" % bet[0, 0], "%.2f" % bet[0, 1]],
                                   'bot1_forecast': "%.2f" % f2,
                                   'bot1_wager': "%.2f" % w2,
                                   'bot1_netpay0': "%.2f" % p2[0],
                                   'bot1_netpay1': "%.2f" % p2[1],
                                   'bot1_bets': ["%.2f" % bet[1, 0], "%.2f" % bet[1, 1]],
                                   'bot2_forecast': "%.2f" % f3,
                                   'bot2_wager': "%.2f" % w3,
                                   'bot2_netpay0': "%.2f" % p3[0],
                                   'bot2_netpay1': "%.2f" % p3[1],
                                   'bot2_bets': ["%.2f" % bet[2, 0], "%.2f" % bet[2, 1]]
                                   })
                        print(forecasts)
                        print(p1, p2, p3)
'''