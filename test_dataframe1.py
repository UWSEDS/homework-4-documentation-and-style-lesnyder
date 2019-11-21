"""This file improves the homework3 tests to ensure that they are PEP8 compliant"""

import pandas as pd

LINK = "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"

DF = pd.read_csv(LINK)

"""This test  all columns have values of the corect type"""
def test_columns(types):
    """Check that the column names are the same type as rows"""
    assert list(DF.dtypes.values) == types

"""Check for nan values."""
def test_nan():
    """checks whole DF for nan then compresses"""
    assert DF.isnan().any().any()

"""Verify that the dataframe has at least one row."""
def test_row():
    """ensures that the number of rows is not 0"""
    value = DF.test_creat_dataframe([])
    assert value == 0
