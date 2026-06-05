""" Script for changing datatype using pandas 2886"""

import pandas as pd

def changeDataTypes(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

    # Can also use students = students.astype({"grade":int})