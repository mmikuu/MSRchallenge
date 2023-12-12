from sklearn.metrics import cohen_kappa_score

def calc_kappa(eval,eva2,title):
    # Cohen's Kappa
    kappa = cohen_kappa_score(eval, eva2, weights='linear')
    print(title, kappa)

if __name__ == '__main__':
    # （6x6）
    Mevaluator1 = [46,16,9,48,10,3,1]
    Kevaluator2 = [43,15,10,49,10,5,1]

    Musage = [16,5,20,1,3,2,9,9,14,7,12,6,2,4,14,3,6]
    Kusage = [18,4,22,1,3,2,10,9,16,6,10,4,2,5,12,3,6]

    Mnegative = [3,1,2,2,3,1,1,1,0]
    Knegative = [5,1,2,1,2,1,0,1,1]

    calc_kappa(Mevaluator1,Kevaluator2,"positive/negative")
    calc_kappa(Musage, Kusage, "usage")
    calc_kappa(Mnegative, Knegative, "negative")

