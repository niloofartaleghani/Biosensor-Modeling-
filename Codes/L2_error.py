def calculate_error(fine, coarse, x_fine, x_coarse):
    # Initialize an array to store interpolated coarse values
    interpolated_coarse = np.zeros_like(fine)

    # Loop through all fine grid points
    fine_len = len(x_fine)
    coarse_len = len(x_coarse)
    
    for i in range(fine_len):
        x_f = x_fine[i]
        
        # Find the closest left and right coarse grid points
        for j in range(coarse_len - 1):
            if x_coarse[j] <= x_f <= x_coarse[j + 1]:
                # Linear interpolation formula
                x_left, x_right = x_coarse[j], x_coarse[j + 1]
                f_left, f_right = coarse[j], coarse[j + 1]
                
                # Calculate the interpolated value
                interpolated_value = f_left + (f_right - f_left) * (x_f - x_left) / (x_right - x_left)
                interpolated_coarse[i] = interpolated_value
                break

    # Calculate the L2 error norm
    error = np.sqrt(np.sum((fine - interpolated_coarse) ** 2) / fine_len)
    
    return error
