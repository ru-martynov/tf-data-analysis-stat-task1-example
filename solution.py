import pandas as pd
import numpy as np


chat_id = 303100650 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    errors = np.random.laplace(loc = 0, scale = 0, size = len(x))
    v_mean = np.mean(x + errors)
    answer = v_mean / 22
    return answer
