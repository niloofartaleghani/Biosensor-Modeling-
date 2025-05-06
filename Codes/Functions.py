def explicit_fdm_with_inhibition(X, xnum, tnum, Si, Ii, beta, sigma, sigma_prime, K_prime, dt, dx, SN_list):
    results = {}

    for SN in SN_list:
        S = np.zeros((tnum + 1, xnum))
        P = np.zeros((tnum + 1, xnum))
        I = np.zeros((tnum + 1, xnum))

        # Initial conditions
        S[0, :] = Si
        I[0, :] = Ii
        S[:, -1] = SN  # Dirichlet BC at x = L

        for t_step in range(1, tnum + 1):
            # Step 1: update inhibitor first
            for j in range(1, xnum - 1):
                inhibitor_term = 1 + I[t_step - 1, j] / K_prime
                reaction = S[t_step - 1, j] / ((S[t_step - 1, j] + 1) * inhibitor_term)
                I[t_step, j] = beta * Ri * (I[t_step - 1, j + 1] + I[t_step - 1, j - 1]) + \
                               (1 - 2 * beta * Ri) * I[t_step - 1, j] - (sigma ** 2) * reaction * dt
            I[t_step, 0] = I[t_step, 1]  # Neumann BC

            # Step 2: update substrate and product using new I[t_step]
            for j in range(1, xnum - 1):
                inhibitor_term = 1 + I[t_step, j] / K_prime
                reaction = S[t_step - 1, j] / ((S[t_step - 1, j] + 1) * inhibitor_term)

                S[t_step, j] = beta * (S[t_step - 1, j + 1] + S[t_step - 1, j - 1]) + \
                               (1 - 2 * beta) * S[t_step - 1, j] - (sigma ** 2) * reaction * dt

                P[t_step, j] = beta * R * (P[t_step - 1, j + 1] + P[t_step - 1, j - 1]) + \
                               (1 - 2 * beta * R) * P[t_step - 1, j] + (sigma_prime ** 2) * reaction * dt

            S[t_step, 0] = S[t_step, 1]  # Neumann BC
            P[t_step, 0] = P[t_step, 1]  # Neumann BC

        results[SN] = {'S': S, 'P': P, 'I': I}

    return results
