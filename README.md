# ads_stats.py
The python code analyzes user data across four weeks to compare the effectiveness of YouTube and Facebook ads. It calculates weekly totals, averages, and peak users, then determines which ad platform contributed more users in April. Please note data is not real.

Key steps include:

1. **Data Input**: Four lists (`week1_users` to `week4_users`) store daily user counts.
2. **Totals & Averages**: Sums (`sum_week1` etc.) and averages (`avg_week1` etc.) are computed for each week.
3. **Monthly Total**: `month_april` aggregates all weekly totals.
4. **Ad Platform Comparison**: 
   - YouTube ads (weeks 1 & 4) total: `sum_week1 + sum_week4`
   - Facebook ads (weeks 2 & 3) total: `sum_week2 + sum_week3`
5. **Percentage Calculation**: 
   - YouTube: `((sum_week1 + sum_week4) / month_april) * 100`
   - Facebook: `((sum_week2 + sum_week3) / month_april) * 100`
6. **Conclusion**: Prints which platform had higher user contribution based on percentages.

The script concludes that YouTube ads were more effective if their percentage exceeds Facebook's, otherwise Facebook is deemed better. This analysis helps decide future ad strategies.
