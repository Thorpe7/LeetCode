""" Script for Drop Duplicate Rows 2882 """

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:

    cleaned_df = customers.drop_duplicates(subsets=["email"])
    # Can also use "Keep" and "inplace" for modifyin how to handle the removed items
    return cleaned_df
