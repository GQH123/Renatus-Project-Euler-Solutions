x = 1
bouncy_number_count = 0


def is_bouncy(x):
    inc, dec = True, True
    x = str(x)
    last_digit = int(x[0])
    for c in x[1:]:
        if int(c) > last_digit:
            dec = False
        if int(c) < last_digit:
            inc = False
        last_digit = int(c)
    return not (inc or dec)


report_50_percent = False
report_90_percent = False
report_99_percent = False

while True:
    if x % 10000 == 0:
        print(f'checking {x}')
    if is_bouncy(x):  # TODO: implement
        bouncy_number_count += 1
    if bouncy_number_count / x >= 0.5:
        if not report_50_percent:
            print(f'bouncy number count reach 50% at {x} as {bouncy_number_count}/{x}')
            report_50_percent = True
            input()
    if bouncy_number_count / x >= 0.9:
        if not report_90_percent:
            print(f'bouncy number count reach 90% at {x} as {bouncy_number_count}/{x}')
            report_90_percent = True
            input()
    if bouncy_number_count / x >= 0.99:
        if not report_99_percent:
            print(f'bouncy number count reach 99% at {x} as {bouncy_number_count}/{x}')
            report_99_percent = True
            input()   
    if bouncy_number_count / x == 0.99:
        print(f'bouncy number count equals exactly 99% at {x} as {bouncy_number_count}/{x}')
        break
    x += 1
