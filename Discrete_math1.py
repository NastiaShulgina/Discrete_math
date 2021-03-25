mnozhyna_1 = [-2, 4, 3]
mnozhyna_2 = [1, 4, -1]

def dekart_dob (mnozhyna_1, mnozhyna_2):
    dekartovyy_dobutok = []
    for m in mnozhyna_1:
        for k in mnozhyna_2:
            dekartovyy_dobutok.append([m,k])
    return dekartovyy_dobutok

def absolut_dopovn(mnozhyna_1):
    absolutne_dopovnennya = []
    for i in range(-5, 5):
        if i not in mnozhyna_1:
            absolutne_dopovnennya.append(i)
    return absolutne_dopovnennya

if __name__ == "__main__":
    print(dekart_dob(mnozhyna_1, mnozhyna_2))
    print(absolut_dopovn(mnozhyna_1))


            

            