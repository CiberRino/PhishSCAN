def score(signs,score):

    if score <= 15:
        print(f"[*] possible low risk {signs} possible signs of phising")
    elif score <= 25:
        print(f"[:] possible mid risk {signs} possible signs of phising")
    elif score <= 45:
        print(f"[!] possible hight risk {signs} possible signs of phising")
    