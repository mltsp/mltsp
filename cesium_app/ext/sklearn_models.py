import numpy as np


model_descriptions = [
    {"name": "RandomForestClassifier",
     "params": [
         {"name": "n_estimators", "type": int, "default": 10},
         {"name": "criterion", "type": str, "default": "gini"},
         {"name": "max_features", "type": [int, float, str],
          "default": "auto"},
         {"name": "max_depth", "type": int, "default": None},
         {"name": "min_samples_split", "type": int, "default": 2},
         {"name": "min_samples_leaf", "type": int, "default": 1},
         {"name": "min_weight_fraction_leaf", "type": float, "default": 0.},
         {"name": "max_leaf_nodes", "type": int, "default": None},
         {"name": "bootstrap", "type": bool, "default": True},
         {"name": "oob_score", "type": bool, "default": False},
         {"name": "random_state", "type": int, "default": None},
         {"name": "class_weight", "type": dict, "default": None}],
     "type": "classifier",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html"},

    {"name": "RandomForestRegressor",
     "params": [
         {"name": "n_estimators", "type": int, "default": 10},
         {"name": "criterion", "type": str, "default": "mse"},
         {"name": "max_features", "type": [int, float, str],
          "default": "auto"},
         {"name": "max_depth", "type": int, "default": None},
         {"name": "min_samples_split", "type": int, "default": 2},
         {"name": "min_samples_leaf", "type": int, "default": 1},
         {"name": "min_weight_fraction_leaf", "type": float, "default": 0.},
         {"name": "max_leaf_nodes", "type": int, "default": None},
         {"name": "bootstrap", "type": bool, "default": True},
         {"name": "oob_score", "type": bool, "default": False},
         {"name": "random_state", "type": int, "default": None}],
     "type": "regressor",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html"},

    {"name": "LinearSGDClassifier",
     "params": [
         {"name": "loss", "type": str, "default": "hinge"},
         {"name": "penalty", "type": str, "default": "l2"},
         {"name": "alpha", "type": float, "default": 0.0001},
         {"name": "l1_ratio", "type": float, "default": 0.15},
         {"name": "fit_intercept", "type": bool, "default": True},
         {"name": "n_iter", "type": int, "default": 5},
         {"name": "shuffle", "type": bool, "default": True},
         {"name": "random_state", "type": int, "default": None},
         {"name": "epsilon", "type": float, "default": 0.1},
         {"name": "learning_rate", "type": str, "default": "optimal"},
         {"name": "eta0", "type": float, "default": 0.0},
         {"name": "power_t", "type": float, "default": 0.5},
         {"name": "class_weight", "type": [dict, str], "default": None},
         {"name": "average", "type": [bool, int], "default": False}],
     "type": "classifier",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html"},

    {"name": "LinearRegressor",
     "params": [
         {"name": "fit_intercept", "type": bool, "default": True},
         {"name": "normalize", "type": bool, "default": False}],
     "type": "regressor",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html"},

    {"name": "RidgeClassifierCV",
     "params": [
         {"name": "alphas", "type": list,
          "default": [0.1, 1., 10.]},
         {"name": "fit_intercept", "type": bool, "default": True},
         {"name": "normalize", "type": bool, "default": False},
         {"name": "scoring", "type": str, "default": None},
         {"name": "cv", "type": "generator", "default": None},
         {"name": "class_weight", "type": dict, "default": None}],
     "type": "classifier",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html"},

    {"name": "BayesianARDRegressor",
     "params": [
         {"name": "n_inter", "type": int, "default": 300},
         {"name": "tol", "type": float, "default": 0.001},
         {"name": "alpha_1", "type": float, "default": 1.e-06},
         {"name": "alpha_2", "type": float, "default": 1.e-06},
         {"name": "lambda_1", "type": float, "default": 1.e-06},
         {"name": "lambda_2", "type": float, "default": 1.e-06},
         {"name": "compute_score", "type": bool, "default": False},
         {"name": "threshold_lambda", "type": float, "default": 10000.},
         {"name": "fit_intercept", "type": bool, "default": True},
         {"name": "normalize", "type": bool, "default": False}],
     "type": "regressor",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html"},

    {"name": "BayesianRidgeRegressor",
     "params": [
         {"name": "n_inter", "type": int, "default": 300},
         {"name": "tol", "type": float, "default": 0.001},
         {"name": "alpha_1", "type": float, "default": 1.e-06},
         {"name": "alpha_2", "type": float, "default": 1.e-06},
         {"name": "lambda_1", "type": float, "default": 1.e-06},
         {"name": "lambda_2", "type": float, "default": 1.e-06},
         {"name": "compute_score", "type": bool, "default": False},
         {"name": "fit_intercept", "type": bool, "default": True},
         {"name": "normalize", "type": bool, "default": False}],
     "type": "regressor",
     "url": "http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"}]
