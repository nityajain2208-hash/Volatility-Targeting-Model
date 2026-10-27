# Volatility Targeting Model

A Python-based quantitative investment model that adjusts portfolio exposure according to estimated market volatility. The project explores the relationship between risk, position sizing, and investment performance through historical market data and strategy backtesting.

## Project Overview

Volatility targeting is a portfolio management technique that adjusts exposure to an asset based on its estimated volatility. When estimated volatility rises, the strategy reduces exposure; when volatility falls, it may increase exposure, subject to a predefined leverage limit.

This project implements a volatility-targeting strategy alongside a baseline strategy, allowing their performance and risk characteristics to be compared over historical market data.

## Key Features

- Retrieves historical market data using Yahoo Finance.
- Calculates rolling volatility estimates from historical returns.
- Implements a momentum-based investment signal.
- Adjusts portfolio exposure to target a specified volatility level.
- Applies a maximum leverage constraint.
- Calculates risk and performance metrics.
- Visualizes cumulative returns and realized volatility.
- Compares the volatility-targeting strategy against a baseline.

## Methodology

### 1. Data Collection

Historical price data is obtained using the `yfinance` library and processed using pandas.

Daily returns are calculated from consecutive asset prices and used to estimate recent volatility.

### 2. Momentum Signal

The strategy uses a 252-trading-day lookback period to determine market direction.

- If the trailing 252-day return is positive, the strategy takes a long position.
- Otherwise, the strategy moves to cash.

This signal determines whether the strategy is invested in the asset.

### 3. Volatility Estimation

The model estimates recent volatility using a rolling 20-trading-day window.

**Annualized Volatility = Standard Deviation of Daily Returns × Square Root of 252**

The annualization factor converts daily volatility into an approximate annualized measure, assuming 252 trading days per year.

### 4. Volatility Targeting and Position Sizing

The strategy aims for an annualized volatility target of 10%.

The position multiplier is calculated as follows:

**Position Multiplier = Minimum(Target Volatility / Estimated Volatility, Maximum Leverage)**

Default parameters:

- **Target Volatility:** 10% annually.
- **Volatility Lookback:** 20 trading days.
- **Maximum Leverage:** 2 times the portfolio's capital exposure.

The final position combines the momentum signal with the volatility-based position multiplier.

When estimated volatility increases, the model reduces exposure. When estimated volatility decreases, the model may increase exposure, subject to the leverage cap.

*Implementation note: volatility estimates must use only information available at the time the position is established. Signal timing should be checked carefully to avoid look-ahead bias.*

## Backtesting and Performance Evaluation

The strategy is evaluated using historical data and compared against a baseline strategy.
The following metrics help assess its performance:

- **Cumulative Returns:** Tracks the growth of the portfolio over the backtest period.
- **Sharpe Ratio:** Measures risk-adjusted performance relative to return volatility.
- **Maximum Drawdown:** Measures the largest peak-to-trough decline in portfolio value.
- **Realized Volatility:** Measures the volatility actually experienced by the strategy.

### Backtesting Results

The backtest produced the following results:
Metric

Metric | Baseline Strategy | Volatility-Targeting Strategy |
|---|---:|---:|
Sharpe Ratio | 0.74 | 0.89 |
Maximum Drawdown | -31.17% | -13.10% |

## Key Observations

1. Improved risk-adjusted performance

The Sharpe ratio increased from 0.74 to 0.89, an improvement of approximately 20.3% relative to the baseline.

2. Reduced maximum drawdown

Maximum drawdown decreased in magnitude from 31.17% to 13.10%, an improvement of 18.07 percentage points.

3. Improved historical risk-return profile

The results indicate that volatility targeting improved the strategy's historical Sharpe ratio while substantially reducing its maximum drawdown over the evaluated period.

These results are specific to the tested dataset, evaluation period, and implementation assumptions. They do not guarantee future performance.

### Visualizations
Plots:

- **Cumulative Returns:** Compares the growth of the volatility-targeting strategy against the baseline.
- **Realized Volatility:** Shows how the strategy's volatility changes over time relative to the target.

(vol_targeting.png)

## Technology Stack

- Python
- yfinance
- pandas
- NumPy
- Matplotlib

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/nityajain2208-hash/Volatility-Targeting-Model.git
cd Volatility-Targeting-Model
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the model using the project's main Python script:

```bash
python model.py
```

If your entry-point script has a different name, replace `model.py` with the correct filename.

## Assumptions and Limitations

- Historical data is used to evaluate a simulated investment strategy.
- Historical performance does not guarantee future results.
- Volatility estimates depend on the selected lookback window and estimator.
- A momentum signal can perform poorly during choppy or rapidly reversing markets.
- Leverage can amplify both gains and losses.
- Results may be affected by transaction costs, slippage, financing costs, and execution assumptions.
- Backtest results should be interpreted in light of the costs and assumptions actually implemented in the code.

## Future Improvements

- Compare different volatility estimators and lookback periods.
- Evaluate alternative volatility targets and leverage constraints.
- Include transaction costs and realistic financing assumptions.
- Test the strategy across multiple assets and market regimes.
- Add rolling Sharpe ratio and drawdown analysis.
- Perform sensitivity analysis on key strategy parameters.
- Evaluate performance using out-of-sample data.

## Learning Outcomes

This project explores volatility estimation, momentum-based signals, dynamic position sizing, historical backtesting, and risk-adjusted portfolio evaluation — core concepts in quantitative research and systematic investing.
