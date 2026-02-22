def score(found,score):
    signs = 0
    for search in found:
        if "shorteners" in search:
            print("[*] Un enlace acortado no siempre es phishing; depende del contexto y la situación. Ante la duda, no lo abras y consulta con tu equipo.")
            signs += 1        
        if "http" in search:
            print("[!] Si un enlace usa HTTP, no compartas datos sensibles; depende del contexto y la situación. Ante la duda, no lo abras y consulta con tu equipo.")
            signs += 1

    if score <= 30:
        print(f"[*] possible low risk {signs} possible signs of phising")
    elif score >= 80:
        print(f"[!] possible hight risk {signs} possible signs of phising")
    else:
        print(f"[:] possible mid risk {signs} possible signs of phising")
     