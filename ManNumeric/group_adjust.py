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

    ### Error Handling ###

    # Check that weights length equals group length
    if len(weights) != len(groups):
        raise ValueError("Need to have 1 weight for each group")

    # Check that groups have the same length
    group_lengths = [len(grp) for grp in groups]
    if all([group_length == len(vals) for group_length in group_lengths]) != True:
        raise ValueError("The groups need to be same shape as vals")

    # Store groups as dictionary converted to dataframe
    # Use this dict as the basis for main data table
    table = {'group_{}'.format(id+1):val for id, val in enumerate(groups)}
    table = pd.DataFrame(table)
    # Do the same for weights
    weights_per_group = {'weight_group_{}'.format(id+1):[val] for id, val in enumerate(weights)}
    weights = pd.DataFrame(weights_per_group)
    # ...and for vals
    vals = pd.DataFrame({'vals':vals})

    # Put vals and groups together together
    table = pd.concat([vals, table], axis = 1)

    # Find the group means...by using transform (window function), we can avoid a group by and then a join.
    # Now the grouped means can be expanded with duplicates for each member of the group.
    for i in range(len(groups)):
        table['group{}_means'.format(i+1)] = table.groupby('group_{}'.format(i+1))['vals'].transform(lambda x: x.mean())

    # Create an empty weighted means column to store the weighted means
    table['weighted_means'] = pd.DataFrame({'weighted_means':[0]*len(vals)})
    # Fill that column with each group's mean times its associated weight
    for id,weight in enumerate(weights.columns.sort_values()):
        table['weighted_means'] += table['group{}_means'.format(id+1)]*float(weights[weight])

    # Finally create a demeaned column that is equal to all vals minus weighted_means
    table['demeaned'] = table['vals'] - table['weighted_means']

    return list(table['demeaned'])



def test_three_groups():
    vals = [1, 2, 3, 8, 5]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'MA', 'MA', 'RI', 'RI']
    grps_3 = ['WEYMOUTH', 'BOSTON', 'BOSTON', 'PROVIDENCE', 'PROVIDENCE']
    weights = [.15, .35, .5]

    adj_vals = group_adjust(vals, [grps_1, grps_2, grps_3], weights)
    # 1 - (USA_mean*.15 + MA_mean * .35 + WEYMOUTH_mean * .5)
    # 2 - (USA_mean*.15 + MA_mean * .35 + BOSTON_mean * .5)
    # 3 - (USA_mean*.15 + MA_mean * .35 + BOSTON_mean * .5)
    # etc ...
    # Plug in the numbers ...
    # 1 - (.15 * 3.8 + .35 * 2.0 + .5 * 1.0) = -0.770
    # 2 - (.15 * 3.8 + .35 * 2.0 + .5 * 2.5) = -0.520
    # 3 - (.15 * 3.8 + .35 * 2.0 + .5 * 2.5) =  0.480
    # etc...

    answer = [-0.770, -0.520, 0.480, 1.905, -1.095]
    for ans, res in zip(answer, adj_vals):
        assert abs(ans - res) < 1e-5


def test_two_groups():
    vals = [1, 2, 3, 8, 5]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'RI', 'CT', 'CT', 'CT']
    weights = [.65, .35]

    adj_vals = group_adjust(vals, [grps_1, grps_2], weights)
    # 1 - (.65 * 3.8 + .35 * 1.0) = -1.82
    # 2 - (.65 * 3.8 + .35 * 2.0) = -1.17
    # 3 - (.65 * 3.8 + .35 * 5.33333) = -1.33666
    answer = [-1.82, -1.17, -1.33666, 3.66333, 0.66333]
    for ans, res in zip(answer, adj_vals):
        assert abs(ans - res) < 1e-5
    # return adj_vals

def test_missing_vals():
    # If you're using NumPy or Pandas, use np.NaN
    # If you're writing pyton, use None
    vals = [1, np.NaN, 3, 5, 8, 7]
    # vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65, .35]

    adj_vals = group_adjust(vals, [grps_1, grps_2], weights)

    # This should be None or np.NaN depending on your implementation
    # please feel free to change this line to match yours
    answer = [-2.47, np.NaN, -1.170, -0.4533333, 2.54666666, 1.54666666]
    # answer = [-2.47, None, -1.170, -0.4533333, 2.54666666, 1.54666666]

    for ans, res in zip(answer, adj_vals):
        if ans is None:
            assert res is None
        elif np.isnan(ans):
            assert np.isnan(res)
        else:
            assert abs(ans - res) < 1e-5


def test_weights_len_equals_group_len():
    # Need to have 1 weight for each group

    # vals = [1, np.NaN, 3, 5, 8, 7]
    vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65]

    with pytest.raises(ValueError):
        group_adjust(vals, [grps_1, grps_2], weights)


def test_group_len_equals_vals_len():
    # The groups need to be same shape as vals
    vals = [1, None, 3, 5, 8, 7]
    grps_1 = ['USA']
    grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65]

    with pytest.raises(ValueError):
        group_adjust(vals, [grps_1, grps_2], weights)


def test_performance():
    # vals = 1000000*[1, None, 3, 5, 8, 7]
    # If you're doing numpy, use the np.NaN instead
    vals = 1000000 * [1, np.NaN, 3, 5, 8, 7]
    grps_1 = 1000000 * [1, 1, 1, 1, 1, 1]
    grps_2 = 1000000 * [1, 1, 1, 1, 2, 2]
    grps_3 = 1000000 * [1, 2, 2, 3, 4, 5]
    weights = [.20, .30, .50]

    start = datetime.now()
    group_adjust(vals, [grps_1, grps_2, grps_3], weights)
    end = datetime.now()
    diff = end - start
    # return diff











