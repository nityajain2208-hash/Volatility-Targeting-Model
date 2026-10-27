import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = yf.download('SPY', start='2015-01-01', end='', progress=False)
data = data[['Close']].copy()
data['return'] = data['Close'].pct_change()

data['momentum'] = data['Close'].pct_change(252)
data['base_position'] = np.where(data['momentum'].shift(1) > 0, 1, 0)

target_vol = 0.10  # 10% annualised target
lookback = 20
data['realised_vol'] = data['return'].rolling(lookback).std() * np.sqrt(252)
data['vol_scalar'] = (target_vol / data['realised_vol']).clip(upper=2.0)

data['vt_position'] = data['base_position'] * data['vol_scalar']
data['vt_return']   = data['vt_position'].shift(1) * data['return']
data['base_return'] = data['base_position'] * data['return']
data.dropna(inplace=True)

def sharpe(r, p=252): return r.mean()*p / (r.std()*np.sqrt(p))
def max_dd(r):
    c = (1+r).cumprod()
    return ((c - c.cummax()) / c.cummax()).min()

print(f'Base Sharpe:           {sharpe(data["base_return"]):.2f}')
print(f'Vol Targeted Sharpe:   {sharpe(data["vt_return"]):.2f}')
print(f'Base Max Drawdown:     {max_dd(data["base_return"]):.2%}')
print(f'VT Max Drawdown:       {max_dd(data["vt_return"]):.2%}')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
fig.patch.set_facecolor('#0D1B2A')
for ax in [ax1, ax2]:
    ax.set_facecolor('#0D1B2A')
    ax.tick_params(colors='white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#4a5a6a')
    ax.spines['left'].set_color('#4a5a6a')

(1+data['base_return']).cumprod().plot(ax=ax1, color='white', alpha=0.7, label='Base')
(1+data['vt_return']).cumprod().plot(ax=ax1, color='#00D4FF', label='Vol Targeted')
ax1.set_title('Base vs Volatility Targeted Strategy', color='white', fontweight='bold')
ax1.legend(facecolor='#1a2a3a', labelcolor='white')

data['realised_vol'].plot(ax=ax2, color='#00D4FF')
ax2.set_title('Realised Volatility (20-day rolling)', color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('vol_targeting.png', dpi=150, bbox_inches='tight', facecolor='#0D1B2A')
plt.show()