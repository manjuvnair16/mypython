def compute_pay(hrs, rt):
    if hrs > 40:
        print('Overtime')
        regPay = 40 * rt
        overPay = (hrs-40) * rt * 0.5
        pay = regPay + overPay
    else:
        print('Regular')
        pay = hrs * rt
    return pay

hours = input('Enter number of hours:')

try:
    hrs = float(hours)
except:
    print('Enter a numeric input for hours')
else:
    rate = input('Enter the rate:')
    try:
        rt = float(rate)
    except:
        print('Enter a numeric input for rate')
    else:
        pay = compute_pay(hrs, rt)
        print('Pay:', pay)
