from math import radians, sin, cos, asin, sqrt
import matplotlib.pyplot as plt
import seaborn as sns


def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Compute distance between two pairs of (lat, lng)
    See - (https://en.wikipedia.org/wiki/Haversine_formula)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))


def text_scatterplot(df, x, y):
    """
    For a Dataframe df, create a scatterplot with the index
    as text label.
    """
    f, ax = plt.subplots(figsize=(15, 10))

    f = sns.scatterplot(x=x,
                        y=y,
                        data=df,
                        ax=ax)

    # For each point, we add a text inside the bubble
    for i in df.index:
        f.text(df.loc[i][x],
               df.loc[i][y],
               i,
               horizontalalignment='left')


def return_significative_coef(model):
    """
    Returns p_value, lower and upper bound coefficients
    from a statsmodels object.
    """
    # Extract p_values
    p_values = model.pvalues.reset_index()
    p_values.columns = ['variable', 'p_value']

    # Extract coef_int
    coef_int = model.conf_int().reset_index()
    coef_int.columns = ['variable', 'lower', 'upper']
    return p_values.merge(coef_int,
                          on='variable')\
                   .query("p_value<0.05").sort_values(by='lower',
                                                      ascending=False)


def plot_kde_plot(df, variable, dimension):
    """
    Plot a side by side kdeplot for `variable`, split
    by `dimension`.
    """
    g = sns.FacetGrid(df,
                      hue=dimension,
                      col=dimension)
    g.map(sns.kdeplot, variable)
