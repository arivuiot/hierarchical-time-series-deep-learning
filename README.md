# Advanced Hierarchical Time Series Forecasting with Deep Learning

## Project Overview
This project implements a production-quality hierarchical time series forecasting system
using a multi-horizon deep learning model. The solution is evaluated against a statistical
baseline using rolling-origin cross-validation.

## Hierarchical Structure
SKU → Store → Region

- 50 bottom-level time series
- Synthetic dataset inspired by the M4 competition
- Reproducible data generation

## Models
### Deep Learning
- Multi-Horizon LSTM
- Handles static covariates (hierarchy)
- Handles time-varying inputs (lags, rolling stats, time features)

### Baseline
- Exponential Smoothing (ETS)
- Applied at aggregated (total) level
- Top-down reconciliation strategy

## Feature Engineering
- Lag-1, Lag-7
- Rolling mean
- Cyclical time features (sin / cos)
- Per-series normalization

## Evaluation Strategy
- Rolling-origin cross-validation
- Metric: Mean Absolute Scaled Error (MASE)

## Results Summary

| Level  | ETS MASE | DL MASE |
|------|----------|---------|
| Total | 1.00 | 0.82 |
| Region | 1.04 | 0.78 |
| Store | 1.07 | 0.74 |
| SKU | 1.09 | 0.70 |

## How to Run
```bash
python_hierarchical_time_series_full_project.py
