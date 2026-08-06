from universe import companies
from market import get_quote

print(f"{'Symbol':<8} {'Ratio':>8} {'Volume':>12} {'Average':>12}")

for company in companies():
    quote = get_quote(company.symbol)

    if quote is None:
        continue

    print(
        f"{company.symbol:<8} "
        f"{quote['volume_ratio']:>8.2f} "
        f"{quote['volume']:>12,} "
        f"{quote['average_volume']:>12,}"
    )