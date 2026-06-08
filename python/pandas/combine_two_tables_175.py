""" Script for pandas practice question combine two tables 175 """

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    merged_df = pd.merge(person,address, on='personId', how='left')
    cleaned_df = merged_df[['firstName','lastName','city','state']]
    return cleaned_df