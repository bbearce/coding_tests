import pytest
from datetime import datetime
import pandas as pd, numpy as np

def group_adjust(vals, groups, weights):
    """
    Calculate a group adjustment (demean).

    Parameters
    ----------

    vals    : List of floats/ints

        The original values to adjust

    groups  : List of Lists

        A list of groups. Each group will be a list of ints

    weights : List of floats

        A list of weights for the groupings.

    Returns
    -------

    A list-like demeaned version of the input values
    """
    # raise NotImplementedError # I believe this is how the code starts and should not run

vals       = [  1  ,   2  ,   3  ]
ctry_grp   = ['USA', 'USA', 'USA']
state_grp  = ['MA' , 'MA' ,  'CT' ]
weights = [.35, .65] # [COUNTRY, STATE]
weights = pd.DataFrame({'country': [weights[0]], 'state': [weights[1]]})

table = pd.DataFrame({'vals':vals, 'ctry_grp':ctry_grp, 'state_grp':state_grp})

ctry_means = table.groupby('ctry_grp')['vals'].mean().reset_index()
ctry_means = ctry_means.rename(columns={'vals':'ctry_means'})
table = pd.merge(table,ctry_means, on='ctry_grp', how='left')

state_means = table.groupby('state_grp')['vals'].mean().reset_index()
state_means = state_means.rename(columns={'vals':'state_means'})
table = pd.merge(table,state_means, on='state_grp', how='left')

table['weighted_means'] = table['ctry_means']*float(weights['country']) + table['state_means']*float(weights['state'])
table['demeaned'] = table['vals'] - table['weighted_means']
demeaded = [i for i in table['demeaned']]












