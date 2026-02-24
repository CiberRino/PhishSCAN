def score(signs,score):

    if score <= 20:
        print(f"[*] possible low risk {signs} possible signs of phising")
    elif score <= 50:
        print(f"[:] possible mid-low risk {signs} possible signs of phising")
    elif score <= 75:
        print(f"[!] possible mid risk {signs} possible signs of phising")
    else:
        print(f"[!!] possible hight risk {signs} possible signs of phising")
     