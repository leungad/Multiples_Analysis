# Multiples_Analysis
Multiples Analysis Function

This is a small function I created to calculate and evaluate a chosen company using multiples analysis. Once chosen companies are
selected to evaluate, the function gathers the data from FinancialModelingPrep's API on various statistics for each
company. The function then calculates EV/EBITDA, EV/EBIT, and EV/Revenue to calculate the main companies Enterprise
Value and averages those EV's. Once that number is calculated, we add back Cash, and subtract Long Term Debt to get the estimated 
market cap. Finally we multiply the market cap by the number of oustanding shares to get the estimated stock price
given the chosen comparison companies.

The analysis is not completely accurate as it is decided by what companies you choose to compare, but it gives a rough estimate to the 
Enterprise Value, Market Cap, and Share Price given competitor's numbers. It is useful when a company being evaluated is not public, 
in which you would need to find that companies' EBITDA, Revenue, EBIT, Cash & Equivalents, and Debt to continue to
find the estimations.
