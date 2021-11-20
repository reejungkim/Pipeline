#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:07:16 2021

@author: reejungkim
"""


#Custom Transformer that fills missing ages
class CustomImputer(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()
        self.age_means_ = {}

    def fit(self, X, y=None):
        self.age_means_ = X.groupby(['Pclass', 'Sex']).Age.mean()

        return self

    def transform(self, X, y=None):
        # fill Age
        for key, value in self.age_means_.items():
            X.loc[((np.isnan(X["Age"])) & (X.Pclass == key[0]) & (X.Sex == key[1])), 'Age'] = value

        return X
