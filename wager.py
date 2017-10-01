import sys
import numpy as np
import scores as sc
from scipy import optimize as opt


def f_norm_Brier_subgradient(data, weights):
    # return f^-1(weighted average(f(data)))
    # for f = Brier_subgradient, f = 2*data - 1 and f^-1 = (1+f)/2
    return (1 + np.average(2 * data - 1, weights=weights)) / 2


def no_arbitage_wagering(forecasts, wagers, f_norm=f_norm_Brier_subgradient):
    # forecasters - the predicted probability of a binary random variable
    #               by each forecasters
    # f_norm - f_norm_function()
    # !!! requires normalizing the range of score rule to [0,1]

    if np.ndim(forecasts) > 1:
        print("No_arbitage_wagering(): forecasters dimension error!")
        return 0

    n = np.shape(forecasts)[0]
    w = wagers
    sum_w = np.sum(w)
    p = forecasts
    P_matrix = np.column_stack((p, 1 - p))
    coefficient = np.multiply(w, sum_w - w) / sum_w
    p_bar = np.zeros(n)
    for i in range(n):
        w_zero_i = np.array(w)
        w_zero_i[i] = 0
        p_bar[i] = f_norm(p, w_zero_i)
    P_bar_matrix = np.column_stack((p_bar, 1 - p_bar))
    # print("p and p_bar:")
    # print(P_matrix[:,0],P_bar_matrix[:,0])
    scores = (sc.Brier_score(P_matrix, b=0.5, a=-0.5) -
              sc.Brier_score(P_bar_matrix, b=0.5, a=-0.5))
    # print(scores)
    # print(coefficient)
    # print(coefficient[:,None]*scores)
    return coefficient[:, None] * scores


def PPM_potiential_func(x, p, b):
    # p_ij the forecast of forecaster i on outcome j
    # b_i the budget of forecaster i

    # n = # of forecasters, m =# of realizations
    n, m = np.shape(p)
    ret = 0
    for i in range(n):
        temp = np.dot(x[i * m:(i + 1) * m], p[i, :])
        if (temp < 0.00000001):
            ret += -1000000  # log(0)
        else:
            ret += b[i] * np.log(np.dot(x[i * m:(i + 1) * m], p[i, :]))
        # if (np.dot(x[i * m:(i + 1) * m], p[i, :]) < 0.00000001):
        #      print('i: ', i)
        #      print('x_i: ', x[i * m:(i + 1) * m])
        #      print('p_i: ', p[i, :])
        #      sys.exit()
        # print(np.dot(x[i * m:(i + 1) * m], p[i, :]))
        # print('loop: ', i, b[i], p[i, :], x[i * m:(i + 1) * m], np.dot(x[i * m:(i + 1) * m], p[i, :]))
    # print(x)
    # print('func: ', ret)
    return -ret


def PPM_jac_potiential_func(x, p, b):
    # p_ij the forecast of forecaster i on outcome j
    # b_i the budget of forecaster i

    n, m = np.shape(p)
    ret = np.zeros((n * m,))
    ind = 0
    for i in range(n):
        s = np.dot(x[i * m:(i + 1) * m], p[i, :])
        for j in range(m):
            ret[ind] = b[i] * p[i, j] / s
            ind += 1
    # print(x)
    # print('jac: ', ret)
    return -ret


def PPM_postive_constraint(x):
    return x


def PPM_jac_postive_constraint(x):
    return np.identity(np.size(x))


def PPM_normality_constraint(x, n, m):
    # n = # of forecasters, m =# of realizations
    # constraint: 1 - sum_i xij = 0
    ret = np.ones((m,))
    for j in range(m):
        for i in range(n):
            ret[j] -= x[i * m + j]
    # print(x)
    # print('nor: ', ret)
    return ret


def PPM_jac_normality_constraint(x, n, m):
    # n = # of forecasters, m =# of realizations
    # constraint: 1 - sum_i xij = 0
    ret = np.zeros((m, n * m))
    for j in range(m):
        for i in range(n):
            ret[j, i * m + j] = -1
    return ret


def PPM_feasible_constraint(x, n, m):
    # n = # of forecasters, m =# of realizations
    # constraint: sum_j xij - 1/n >= 0 (not a tight bound)
    # guarantee the log in the potential function is always
    #           valid during optimization
    ret = -np.ones((n,)) / n
    for i in range(n):
        for j in range(m):
            ret[i] += x[i * m + j]
    return ret


def PPM_jac_feasible_constraint(x, n, m):
    # n = # of forecasters, m =# of realizations
    # constraint: sum_j xij - 1/n >= 0 (not a tight bound)
    # guarantee the log in the potential function is always
    #           valid during optimization
    ret = np.zeros((n, n * m))
    for i in range(n):
        for j in range(m):
            ret[i, i * m + j] = 1
    return ret


def proxy_parimutuel_eq(forecasts, wagers, maxiter=1000):
    n, d = np.shape(forecasts)

    PPM_x0 = np.ones((n * d,)) / d

    PPM_cons = ({'type': 'ineq',
                 'fun': PPM_postive_constraint,
                 'jac': PPM_jac_postive_constraint},
                {'type': 'eq',
                 'fun': PPM_normality_constraint,
                 'jac': PPM_jac_normality_constraint,
                 'args': (n, d)},
                {'type': 'ineq',
                 'fun': PPM_feasible_constraint,
                 'jac': PPM_jac_feasible_constraint,
                 'args': (n, d)})

    PPM_res = opt.minimize(
        PPM_potiential_func,
        x0=PPM_x0,
        args=(forecasts, wagers),
        constraints=PPM_cons,
        jac=PPM_jac_potiential_func,
        method='SLSQP',
        options={'disp': True, 'maxiter': maxiter})

    PPM_x = PPM_res.x.reshape((n, d))

    # Compute the total bet on realization j
    PPM_pi = np.zeros((d,))
    for j in range(d):
        for i in range(n):
            temp = (wagers[i] * forecasts[i, j] /
                    np.dot(forecasts[i, :], PPM_x[i, :]))
            PPM_pi[j] = np.max([temp, PPM_pi[j]])

    PPM_beta = PPM_x * PPM_pi

    return PPM_beta, PPM_x


def net_payoff_PPM(forecasts, wagers, maxiter=1000):
    n, d = np.shape(forecasts)
    beta, x = proxy_parimutuel_eq(forecasts, wagers, maxiter)
    total_wager = np.sum(wagers)
    net_payoff_PPM = np.tile(-wagers[:, None], d)
    for i in range(d):
        net_payoff_PPM[:, i] += total_wager * x[:, i]
    return net_payoff_PPM


'''

np.set_printoptions(precision=3, suppress=True)

# Set the outcome and participant
d = 2  # # of realizations of outcome
n = 100  # # of participants


# Generate participants' true believes and each row represents one belief
forecasts = np.random.dirichlet(np.ones((d,)), size=n)
# forecasts[0,:] = [0.5, 0.5]
wagers = np.random.rand(n)
wagers = np.ones((n,))
print(forecasts)

PPM_x0 = np.ones((n * d,)) / d

PPM_cons = ({'type': 'ineq',
             'fun': PPM_postive_constraint,
             'jac': PPM_jac_postive_constraint},
            {'type': 'eq',
             'fun': PPM_normality_constraint,
             'jac': PPM_jac_normality_constraint,
             'args': (n, d)},
            {'type': 'ineq',
             'fun': PPM_feasible_constraint,
             'jac': PPM_jac_feasible_constraint,
             'args': (n, d)})


PPM_res = opt.minimize(
    PPM_potiential_func,
    x0=PPM_x0,
    args=(forecasts, wagers),
    constraints=PPM_cons,
    jac=PPM_jac_potiential_func,
    method='SLSQP',
    options={'disp': True, 'maxiter': 1000})

PPM_x = PPM_res.x.reshape((n, d))

# Compute the total bet on realization j
PPM_pi = np.zeros((d,))
for j in range(d):
    for i in range(n):
        temp = (wagers[i] * forecasts[i, j] /
                np.dot(forecasts[i, :], PPM_x[i, :]))
        PPM_pi[j] = np.max([temp, PPM_pi[j]])

PPM_beta = PPM_x * PPM_pi

print(PPM_x)
print(PPM_beta)

# net_payoffs = no_arbitage_wagering(forecasts[:, 0], wagers)

# print(np.column_stack((quadratic_scores[:,0],competitive_quadratic_scores[:,0])))
# print(np.reshape(quadratic_scores[:,0]-competitive_quadratic_scores[:,0]-(quadratic_scores[0,0]-competitive_quadratic_scores[0,0]),(-1,1)))
'''
