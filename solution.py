import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import scipy.stats
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 813595623 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.01
    p0 = x_success / x_cnt
    p1 = y_success / y_cnt
    f0 = norm.cdf(np.sqrt(x_cnt) 
                    * (p0 - alpha)
                    / np.sqrt(p0 * (1 - p0)))
    f1 = norm.cdf(np.sqrt(y_cnt)
                    * (p1 - alpha)
                    / np.sqrt(p1 * (1 - p1)))
  
    return f1 > f0 # Ваш ответ, True или False
