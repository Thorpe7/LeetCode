''' Leetcode question Rename Columns 2885 '''

import pandas as pd

def renameColumns1(students: pd.DataFrame) -> pd.DataFrame:

    # Significantly Faster
    # students.columns replace w/ list
    students.columns = ["student_id", "first_name", "last_name", "age_in_years"]

    return students

def renameColumns2(students: pd.DataFrame) -> pd.DataFrame:

    # rename method
    students.rename(columns={"id":"student_id", "first":"first_name","last":"last_name", "age":"age_in_years"})

    return students