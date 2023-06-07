loan_amount = 1000
years = 10
for years in range(10):
    arp = loan_amount * 0.05
    loan_amount = arp + loan_amount
    years += 1
    print(f"For Year {years} you will own ${round(loan_amount, 2)}")
