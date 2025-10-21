
from sklearn.base import BaseEstimator, TransformerMixin
import streamlit as st
import pandas as pd
import numpy as np


class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # Handle both Series and DataFrame
        if isinstance(X, pd.Series):
            self.n_features_in_ = 1
        else:
            self.n_features_in_ = X.shape[1]
        return self

    def transform(self, X, y=None):
        # Convert Series to DataFrame to handle single column safely
        if isinstance(X, pd.Series):
            X = X.to_frame()
        assert X.shape[1] == self.n_features_in_
        X = np.where(X < 0, 0, X)  # remove negatives before log
        return np.log1p(X)
log_transformer = LogTransformer()

class Handle_outliers_lb_ub(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
      
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X)
        
        self.bounds_ = {}
        for col in X.columns:
            q1 = X[col].quantile(0.25)
            q3 = X[col].quantile(0.75)
            iqr = q3 - q1
            lb = q1 - 1.5 * iqr
            ub = q3 + 1.5 * iqr
            self.bounds_[col] = (lb, ub)
        return self

    def transform(self, X, y=None):
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X)
        
        X = X.copy()
        for col, (lb, ub) in self.bounds_.items():
            X[col] = np.clip(X[col], lb, ub)
        return X
h_lb_ub = Handle_outliers_lb_ub()

class FrequencyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns
        self.freq_maps = {}

    def fit(self, X, y=None):
        # Create a mapping of value_counts for each column
        for col in self.columns:
            self.freq_maps[col] = X[col].value_counts(normalize=True)
        return self

    def transform(self, X):
        X = X.copy()
        # Apply frequency encoding to each column
        for col in self.columns:
            X[col + '_freq'] = X[col].map(self.freq_maps[col]).fillna(0)
            X.drop(col, axis=1, inplace=True)
        return X
frequency_encoder = FrequencyEncoder()
