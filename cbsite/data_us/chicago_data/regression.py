import numpy as np 
import pandas as pd 
import statsmodels.api as sm


def lin_regression(x, y):
    '''
    Makes a linear regression between x and y
    '''

    x = sm.add_constant(x)

    model = sm.OLS(y,x)

    results = model.fit()

    hat_vals = results.predict()

    r_sq = results.rsquared

    beta_1 = results.params[1]

    return(beta_1, r_sq, hat_vals)