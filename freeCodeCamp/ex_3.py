hours = input('Enter number of hours:')
hrs = float(hours)
rate = input('Enter the rate:')
rt = float(rate)
if hrs > 40:
    print('Overtime')
    regPay = 40 * rt
    overPay = (hrs-40) * rt * 0.5
    pay = regPay + overPay
    print('Pay:', pay)
else:
    print('Regular')
    pay = hrs * rt
    print('Pay:', pay)
