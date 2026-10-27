# Volatility-Targeting-Model
Python implementation of a quantitative risk management strategy that scales position sizes dynamically to match a constant annualized volatility target, improving Sharpe ratios and dampening drawdowns.

A Python backtest evaluating a volatility-scaled momentum strategy on SPY. 
The strategy dynamically scales leverage up or down based on trailing annualized volatility, aiming to cut severe drawdowns during market shocks while improving overall risk-adjusted returns (Sharpe ratio).

## How It Works
1. **Trend Signal:** Uses a 252-day (1-year) total return as a simple trend indicator.
   - Long (`1.0`) if 252-day return > 0.
   - Cash (`0.0`) otherwise.

2. **Volatility Scaling:** 
   - Calculates 20-day annualized realized volatility.
   - Targets a baseline volatility of **10%**.
   - Scales exposure up or down inversely to realized volatility:
     $$\text{Scalar} = \min\left(\frac{0.10}{\sigma_{\text{20d}}}, 2.0\right)$$
   - Hard capped at **2.0x leverage**.

3. **Execution Position:** $\text{Base Trend} \times \text{Volatility Scalar}$

## Performance Summary

Backtested on SPY (2015 – Present):

| Metric | Unscaled Momentum | Vol-Targeted Momentum |

| **Sharpe Ratio** | 0.74 | **0.89** |
| **Max Drawdown** | -31.17% | **-13.10%** |

## File Structure
- `model.py`: Data retrieval, signal generation, & performance calculation
- `vol_targeting.png`: Performance chart output
- `README.md`: Project documentation

## Usage
1. **Install required packages:**
   ```bash
   pip install yfinance pandas numpy matplotlib