import numpy as np

from sklearn import preprocessing

def norm_cols(df, col_names):
    """
    
    Parameters
    ----------
    
    df: a copy of the training set, no labels, non-normalised columns will be overwritten
    col_names: array of col_names to be normalised
    
    Returns
    -------
    None. The df columns are replaced with normalised columns
    
    """
    
    min_max_scaler = preprocessing.MinMaxScaler()
    
    for col in col_names:
        x_np = np.array(df[col]) # returns a numpy array
        x_scaled = min_max_scaler.fit_transform(x_np.reshape(-1, 1))
        x_scaled = [x[0] for x in x_scaled]
        
        df[col] = x_scaled