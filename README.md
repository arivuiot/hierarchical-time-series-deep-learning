Advanced Time Series Forecasting with Hierarchical Data and Deep Learning

This repository contains a full academic project including:
- Synthetic hierarchical dataset generation
- Feature engineering and preprocessing
- Multi-horizon deep learning forecasting model
- ETS baseline comparison
- Rolling-origin cross-validation
- Final academic report

## Project Overview
Advanced hierarchical time series forecasting using a multi-horizon deep learning model.

## Hierarchy
SKU → Store → Region

## Models
- Multi-Horizon LSTM (Deep Learning)
- ETS (Baseline)

## Evaluation
- Metric: MASE
- Strategy: Rolling-Origin Cross-Validation

## Results Summary
| Level  | ETS_MASE | DL_MASE |
|-------|----------|---------|
| Total | 1.00     | 0.82    |
| SKU   | 1.09     | 0.70    |

## How to Run
1. Generate data
2. Run preprocessing
3. Train model
4. Evaluate results
