import pandas as pd
import numpy as np


chat_id = 134277149

def solution(x: np.array) -> float:
    lambda_mom = np.mean(x) / 28

    return lambda_mom
