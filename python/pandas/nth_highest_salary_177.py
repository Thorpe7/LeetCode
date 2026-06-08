import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee.drop_duplicates(subset='salary', inplace=True)
    if len(employee['salary'].unique()) < N or N<=0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [np.NaN]})

    employee.drop('id',axis=1,inplace=True)
    employee.sort_values('salary', ascending=False,inplace=True)
    employee.rename({'salary':f'getNthHighestSalary({N})'}, axis=1, inplace=True)
    return employee.head(N).tail(1)