from statistics import mean
import requests

comps = ['GOOGL', 'FB', 'AMZN', 'NFLX', 'AAPL']
evaluation = 'MSFT'


def calc_multiples(main, c_list):
    ev_list = []
    ebitda_list = []
    rev_list = []
    for k in c_list:
        EVURL = f"https://financialmodelingprep.com/api/v3/enterprise-value/{k}?period=quarter"
        FSURL = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{k}?period=quarter"
        evdata = requests.get(EVURL).json()
        fsdata = requests.get(FSURL).json()

        EV = evdata['enterpriseValues'][0]['Enterprise Value']
        ebitda = float(fsdata['financials'][0]['EBITDA'])
        revenue = float(fsdata['financials'][0]['Revenue'])
        ebit = float(fsdata['financials'][0]['EBIT'])

        ev_list.append(EV / ebit)
        ebitda_list.append(EV / ebitda)
        rev_list.append(EV / revenue)
    print(f"EV/EBIT average is {mean(ev_list)}")
    print(f"EV/EBITDA average is {mean(ebitda_list)}")
    print(f"EV/REVENUE average is {mean(rev_list)}")

    EVURL = f"https://financialmodelingprep.com/api/v3/enterprise-value/{main}?period=quarter"
    FSURL = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{main}?period=quarter"
    BSURL = f"https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{main}?period=quarter"
    evdata = requests.get(EVURL).json()
    fsdata = requests.get(FSURL).json()
    bsdata = requests.get(BSURL).json()

    ebitda_EV = (float(fsdata['financials'][0]['EBITDA'])) * mean(ebitda_list)
    revenue_EV = (float(fsdata['financials'][0]['Revenue'])) * mean(rev_list)
    ebit_EV = (float(fsdata['financials'][0]['EBIT'])) * mean(ev_list)
    cash = float(bsdata['financials'][0]['Cash and short-term investments'])
    debt = float(bsdata['financials'][0]['Long-term debt'])
    avg_EV = mean([ebitda_EV, revenue_EV, ebit_EV])
    market_cap = avg_EV + cash - debt
    price = market_cap / float(evdata['enterpriseValues'][0]['Number of Shares'])
    print(' ')
    print(f"EBITDA EV is {ebitda_EV}")
    print(f"Revenue EV is {revenue_EV}")
    print(f"EBIT EV is {ebit_EV}")
    print(' ')
    print(f"Average EV is {avg_EV}")
    print(f"Market Cap is {market_cap}")
    print(f"Estimated Stock Price based on the chosen comps is {price}")


calc_multiples(evaluation, comps)