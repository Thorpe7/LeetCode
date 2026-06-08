""" Script for problem 176 return second highest salary"""

import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee.drop_duplicates('salary', inplace=True)
    if len(employee['salary'].unique()) < 2:
        return pd.DataFrame({'SecondHighestSalary':[np.NaN]})
    employee.drop('id', inplace=True)
    employee.sort_values('salary', ascending=False,inplace=True)
    return employee.head(2).tail(1)