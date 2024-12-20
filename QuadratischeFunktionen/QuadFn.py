from pylatex import (
    Document,
    Section,
    Command,
    NoEscape,
    Tabular,
    Package,
    utils,
    Math,
    Enumerate
)

import uuid
import random
import math
import numpy as np


def chance(p):
    return random.random() < p

def vorzeichen(v, np=False):
    if v<0:
        return "-"
    else:
        if np:
            return ""
        else:
            return "+"
        
def isclose(a, b, rel_tol=1e-6, abs_tol=0.1):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def vgl1(var):
    return "" if var == 1 else var

def anzahlns(ns):
    if len(ns) == 0:
        return r" $ Keine Lösung/Keine Nullstellen $"
    elif len(ns) == 1:
        return r"$ Eine Nullstelle $: ("+str(ns[0])+r"|0)"
    else:
        return r"$ Zwei Nullstellen $: ("+str(ns[0])+r"|0) $ und $ ("+str(ns[1])+r"|0)"


def normalform(min=1, max=10): # a*x^2 + b*x + c
    a = random.randint(1,4)*random.choice([-1, 1])
    b = random.randint(min, max)*2*a*random.choice([-1, 1])
    c = random.randint(min, max)*random.choice([-1, 1])
    if a == 0:
        a = 1
    if chance(0.1):
        c = 0
    if chance(0.1):
        b = 0

    return a, b, c


def printnormalform(a, b, c): #  gibt die normalform als string zurück
    print("NF", a, b, c)
    mystring = f"f(x)={vorzeichen(a, np=True)}{vgl1(abs(a))}x^2"
    if not isclose(b, 0.0):
        mystring += f" {vorzeichen(b)} {vgl1(abs(b))}x"
    if not isclose(c, 0.0):
        mystring += f" {vorzeichen(c)} {abs(c)}"
    return mystring

def bestimme_nullstellen_nf(a, b, c):  # gibt die nullstellen der normalform zurück
    d = -c/a + (b/(2*a))**2
    if d < 0:
        return []
    elif isclose(d, 0.0):
        return [-b/(2*a)]
    else:
        return [math.sqrt(d)-b/(2*a), -math.sqrt(d)-b/(2*a)]
    

def nzuspform(a,b,c): # gibt die scheitelpunktsform zurück
    return a, -b/(2*a), c-(b**2)/(4*a)

def scheitelpunktform(min=1, max=10): # a*(x-d)^2 + e
    a = random.randint(1,4)*random.choice([-1, 1])
    d = random.randint(min, max)*random.choice([-1, 1])
    e = random.randint(min, max)*random.choice([-1, 1])
    if a == 0:
        a = 1
    if chance(0.1):
        d = 0
    if chance(0.1):
        e = 0

    return a, d, e

def printscheitelpunktform(a, d, e): # gibt die scheitelpunktsform als string zurück
    print("SPF", a, d, e)
    mystring = f"f(x)={vorzeichen(a, np=True)}{vgl1(abs(a))}"
    if not isclose(d, 0.0):
        mystring += f"(x{vorzeichen(d*-1)}{(abs(d))})^2"
    else:
        mystring += "(x)^2"
    if not isclose(e, 0.0):
        mystring += f" {vorzeichen(e)}{(abs(e))}"
    return mystring

def spzunform(a, d, e): # gibt die normalform zurück
    return a, -2*a*d, a*d**2+e

def bestimme_nullstellen_sf(a, d, e): # gibt die nullstellen der scheitelpunktsform zurück
    e = -e/a
    if e < 0:
        return []
    elif isclose(e, 0.0):
        return [d]
    else:
        return [math.sqrt(e)+d, -math.sqrt(e)+d]


def spzufform(a, d, e): # gibt die faktorisierte form zurück
    ns = bestimme_nullstellen_sf(a, d, e)
    if len(ns) == 0:
        return None, None, None
    elif len(ns) == 1:
        return a, ns[0], ns[0]
    else:
        return a, ns[0], ns[1]

def fzuspform(a, n1, n2): # gibt die scheitelpunktsform zurück
    return a, (n1+n2)/2, -a*(((n1+n2)/2)**2 - n1*n2)

def nzufform(a, b, c): # gibt die faktorisierte form zurück
    ns = bestimme_nullstellen_nf(a, b, c)
    if len(ns) == 0:
        return None, None, None
    elif len(ns) == 1:
        return a, ns[0], ns[0]
    else:
        return a, ns[0], ns[1]

def fzunform(a, n1, n2): # gibt die normalform zurück
    return a, -(n1+n2)*a, n1*n2*a


    

def faktorisierteform(min=1, max=10): # a*(x-n1)*(x-n2)
    a = random.randint(1,4)*random.choice([-1, 1])
    n1 = random.randint(min, max)*random.choice([-1, 1])
    n2 = random.randint(min, max)*random.choice([-1, 1])
    if a == 0:
        a = 1
    if chance(0.1):
        n1 = 0
    if chance(0.1):
        n2 = 0

    return a, n1, n2

def printfaktorisierteform(a, n1, n2): # gibt die faktorisierte form als string zurück
    print("FF", a, n1, n2)
    n1 = -n1
    n2 = -n2
    if a is None or n1 is None or n2 is None:
        return r"\text{Keine Lösung}"
    mystring = f"f(x)={vorzeichen(a, np=True)}{vgl1(abs(a))}"
    if not isclose(n1, 0.0):
        mystring += f"(x{vorzeichen(n1)}{(abs(n1))})"
    else:
        mystring += "(x)"
    if not isclose(n2, 0.0):
        mystring += f"(x{vorzeichen(n2)}{(abs(n2))})"
    else:
        mystring += "(x)"
    return mystring

def bestimme_nullstellen_ff(a, n1, n2): # gibt die nullstellen der faktorisierten form zurück
    return [n1, n2]

def getfn3pkt(p1, p2, p3): # gibt die normalform zurück anhand von 3 punkten auf der parabel
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    a = (y1-y3- (((x1-x3)*(y2-y3))/(x2-x3))) / (x1**2 -x3**2 + (x1-x3)*((x3**2-x2**2)/(x2-x3)))
    b = (y2-y3+a*(x3**2-x2**2))/(x2-x3)
    c = y3 - a*x3**2 - b*x3

    return a, b, c

def getfnSpPkt(sp, p): # gibt die normalform zurück anhand eines scheitelpunktes und einem punkt auf der parabel
    x1, y1 = sp
    x2, y2 = p

    a = (y1-y2) / (x1**2 - 2*x1**2 + 2*x1*x2 - x2**2)
    b = -2*a*x1
    c = y2 +2*a*x1*x2 - a*x2**2

    return a, b, c


def getnormalfunction(ns=[], yaa=None, pkt=[], sp=None): # gibt die normalform zurück anhand von nullstellen, einem y-achsenabschnitt, punkten auf der parabel oder einem scheitelpunkt
    mypkt = []
    if len(ns) > 0:
        for n in ns:
            mypkt.append((n, 0))
    if yaa is not None:
        mypkt.append((0, yaa))
    if len(pkt) > 0:
        mypkt.extend(pkt)
    if len(mypkt) >= 3:
        return getfn3pkt(*mypkt)
    if sp is not None and len(mypkt) >= 1:
        return getfnSpPkt(sp, mypkt[0])


TESTNUMBER = 10
def testGetNormalFunction(): # teste die funktion getnormalfunction
    for i in range(TESTNUMBER):
        a,b,c = normalform()
        a2, n1, n2 = nzufform(a,b,c)
        a3, d, e = nzuspform(a,b,c)
        while a2 is None or isclose(d, 0.0):
            a,b,c = normalform()
            a2, n1, n2 = nzufform(a,b,c)
            a3, d, e = nzuspform(a,b,c)


        print(a,b,c)
        def f(x):
            return a*x**2 + b*x + c

        x1, x2, x3 = random.sample(range(-100, 100), 3)
        while x1 == x2 or x2 == x3 or x1 == x3:
            x1, x2, x3 = random.sample(range(-100, 100), 3)
        y1, y2, y3 = f(x1), f(x2), f(x3)
        print(i, "3pkt", getnormalfunction(pkt=[(x1, y1), (x2, y2), (x3, y3)]))

        a3, d, e = nzuspform(a,b,c)
        x1 = random.randint(-100, 100)
        while x1 == -d:
            x1 = random.randint(-100, 100)
        y1 = f(x1)
        print(i, "sp, pkt", getnormalfunction(sp=(-d, e), pkt=[(x1, y1)]))

        x1 = 0
        y1 = f(x1)
        print(i, "sp, yaa", getnormalfunction(sp=(-d, e), yaa=y1))

        a2, n1, n2 = nzufform(a,b,c)
        x1 = random.randint(-100, 100)
        while x1 == n1 or x1 == n2:
            x1 = random.randint(-100, 100)
        y1 = f(x1)
        print(i, "pkt, ns", getnormalfunction(ns=[n1, n2], pkt=[(x1, y1)]))


def Sekantensuchfunktion(f, x_0, tol=1e-8, maxiterations=1000, maxtries=5): # sucht die nullstelle einer funktion für die tests später
  n = 0 # Number of iteration
  Nullstelle = 0
  if (f(x_0+0.0001)-f(x_0)!=0):
        while n<maxiterations:
            x_Nullstelle = x_0-(f(x_0)*0.0001/(f(x_0+0.0001)-f(x_0)))
            x_0 = x_Nullstelle
            n+=1
            Iterationsnummer=n
            if f(x_Nullstelle) == 0 or np.abs(f(x_Nullstelle)) <= tol:
                Nullstelle = x_Nullstelle
                break
  else:
        Iterationsnummer = 0
        Nullstelle = 0
        print(f"Fehler: Steigung der Sekante ist gleich 0")
        if maxtries > 0: #recursice retry
            return Sekantensuchfunktion(f, x_0+1, tol, maxiterations, maxtries-1)
        if maxtries == 0:
            print("Maximale Anzahl an Versuchen erreicht")

  
  return Nullstelle, Iterationsnummer


def comparens(ns, ns2):
    print(ns, ns2)
    if len(ns) > 1:
        assert isclose(ns[0], ns2[0], abs_tol=0.01) or isclose(ns[1], ns2[0], abs_tol=0.01)
    elif len(ns) == 1:
        assert isclose(ns[0], ns2[0], abs_tol=0.01)

def testNormalform():
     for i in range(TESTNUMBER):
        a, b, c = normalform() # Normalform
        f1 = lambda x: a*x**2 + b*x + c
        nsNF = bestimme_nullstellen_nf(a, b, c)

        print("nullstellen NF", nsNF)
        ns = Sekantensuchfunktion(f1, random.randint(-10, 10))
        comparens(nsNF, ns)


        a2, d, e = nzuspform(a, b, c) # Normal zu Sp form
        f2 = lambda x: a2*(x-d)**2 + e

        for j in range(TESTNUMBER):
            # teste ob die funktionen gleich sind
            x = random.randint(-10, 10)
            print(x, f1(x), f2(x))
            assert isclose(f1(x), f2(x))


        
        nsSF = bestimme_nullstellen_sf(a2, d, e) # Nullstellen der Scheitelpunktsform
        print("nullstellen SPF", nsSF)
        ns = Sekantensuchfunktion(f2, random.randint(-10, 10)) # Nullstellen der Funktion
        comparens(nsSF, ns) # Vergleiche die Nullstellen
        comparens(nsNF, nsSF) # Vergleiche die Nullstellen

        assert isclose(f1(d), e) # korrekter scheitelpunkt
        assert isclose(f2(d), e) # korrekter scheitelpunkt
        assert isclose(f1(0), c)
        assert isclose(f2(0), c)

        a3, n1, n2 = nzufform(a, b, c) # Normal zu Faktorisierte Form

        if n1 is None or n2 is None: # Lösung nicht möglich
            continue
        f3 = lambda x: a3*(x-n1)*(x-n2)
        for j in range(10):
            x = random.randint(-10, 10)
            print(x, f1(x), f3(x))
            assert isclose(f1(x), f3(x))

        nsFF = bestimme_nullstellen_ff(a3, n1, n2)
        print("nullstellen FF", nsFF)
        ns = Sekantensuchfunktion(f3, random.randint(-10, 10))
        comparens(nsFF, ns)
        comparens(nsNF, nsFF)

        
        assert isclose(f3(d), e) # korrekter scheitelpunkt
        assert isclose(f3(0), c)

def testScheitelpunktform():
     for i in range(TESTNUMBER):
        a, d, e = scheitelpunktform() # Scheitelpunktsform
        print(a, d, e)
        print(printscheitelpunktform(a, d, e))
        f1 = lambda x: a*(x-d)**2 + e # Funktion

        nsSF = bestimme_nullstellen_sf(a, d, e) # Nullstellen der Scheitelpunktsform
        ns = Sekantensuchfunktion(f1, random.randint(-10, 10)) 
        comparens(nsSF, ns)

        print("nullstellen SPF", nsSF)

        a2, b, c = spzunform(a, d, e) # Sp zu Normalform
        f2 = lambda x: a2*x**2 + b*x + c 

        for j in range(TESTNUMBER):
            # teste ob die funktionen gleich sind
            x = random.randint(-10, 10)
            print(x, f1(x), f2(x))
            assert isclose(f1(x), f2(x))
        
        nsNF = bestimme_nullstellen_nf(a2, b, c)

        print("nullstellen NF", nsNF)
        ns = Sekantensuchfunktion(f2, random.randint(-10, 10))
        comparens(nsNF, ns) # Vergleiche die Nullstellen
        comparens(nsSF, nsNF) # Vergleiche die Nullstellen

        assert isclose(f1(d), e)
        assert isclose(f2(d), e)
        assert isclose(f1(0), c)
        assert isclose(f2(0), c)

        a3, n1, n2 = spzufform(a, d, e) # Sp zu Faktorisierte Form
        if n1 is None or n2 is None:
            continue
        f3 = lambda x: a3*(x-n1)*(x-n2) # faktoisierte Form

        print(a3, n1, n2)
        print(a2, b, c)
        print(a, d, e)
        for j in range(10):
            # teste ob die funktionen gleich sind
            x = random.randint(-10, 10)
            print(x, f1(x), f3(x))
            assert isclose(f1(x), f3(x))

        nsFF = bestimme_nullstellen_ff(a3, n1, n2) # Nullstellen der Faktorisierten Form
        print("nullstellen FF", nsFF)
        ns = Sekantensuchfunktion(f3, random.randint(-10, 10))
        comparens(nsFF, ns) # Vergleiche die Nullstellen
        comparens(nsSF, nsFF)

        assert isclose(f3(d), e) # korrekter scheitelpunkt
        assert isclose(f3(0), c) # korrekter Y-Achsenabschnitt

def testFaktorisierteForm():
     for i in range(TESTNUMBER):
        a, n1, n2 = faktorisierteform() # Faktorisierte Form
        print(a, n1, n2)
        print(printfaktorisierteform(a, n1, n2))
        f1 = lambda x: a*(x-n1)*(x-n2) # Funktion

        nsFF = bestimme_nullstellen_ff(a, n1, n2) # Nullstellen der Faktorisierten Form
        ns = Sekantensuchfunktion(f1, random.randint(-10, 10)) 
        comparens(nsFF, ns) # Vergleiche die Nullstellen

        print("nullstellen FF", nsFF)

        a2, d, e = fzuspform(a, n1, n2) # Faktorisierte zu Sp Form
        f2 = lambda x: a2*(x-d)**2 + e # Scheitelpunktform

        print(printscheitelpunktform(a2, d, e))

        print(a2, d, e)

        for j in range(TESTNUMBER):
            # teste ob die funktionen gleich sind
            x = random.randint(-10, 10)
            print(x, f1(x), f2(x))
            assert isclose(f1(x), f2(x))
        
        nsSF = bestimme_nullstellen_sf(a2, d, e) # Nullstellen der Scheitelpunktsform

        print("nullstellen SPF", nsSF)
        ns = Sekantensuchfunktion(f2, random.randint(-10, 10))

        comparens(nsSF, ns)
        comparens(nsFF, nsSF)

        assert isclose(f1(d), e) # korrekter scheitelpunkt
        assert isclose(f2(d), e) # korrekter scheitelpunkt
        

        a3, b, c = fzunform(a, n1, n2) # Faktorisierte zu Normalform
        f3 = lambda x: a3*x**2 + b*x + c

        print(printnormalform(a3, b, c))


        for j in range(10):
            # teste ob die funktionen gleich sind
            x = random.randint(-10, 10)
            print(x, f1(x), f3(x))
            assert isclose(f1(x), f3(x))

        nsNF = bestimme_nullstellen_nf(a3, b, c)

        print("nullstellen NF", nsNF)
        ns = Sekantensuchfunktion(f3, random.randint(-10, 10))
        comparens(nsNF, ns) # Vergleiche die Nullstellen
        comparens(nsSF, nsNF) # Vergleiche die Nullstellen

        assert isclose(f3(d), e)
        assert isclose(f3(0), c)
        assert isclose(f1(0), c)
        assert isclose(f2(0), c)

def tests():
    # teste die funktionen
    testNormalform()
    testScheitelpunktform()
    testFaktorisierteForm()
    testGetNormalFunction()

tests()



problemsDoc = Document() # Aufgaben dokument
thisuuid = str(uuid.uuid4())
problemsDoc.preamble.append(Command("title", NoEscape(r'Quadratische Funktionen - Aufgaben \newline '+thisuuid)))
problemsDoc.preamble.append(Command("date", NoEscape(r"\today")))
problemsDoc.packages.append(Package('xcolor'))
problemsDoc.append(NoEscape(r"\maketitle"))

solutionsDoc = Document() # Lösungen dokument
solutionsDoc.preamble.append(Command("title", NoEscape(r'Quadratische Funktionen - Lösungen \newline '+thisuuid)))
solutionsDoc.preamble.append(Command("date", NoEscape(r"\today")))
solutionsDoc.packages.append(Package('xcolor'))
solutionsDoc.append(NoEscape(r"\maketitle"))

numberofquestions = 10 # Anzahl der Fragen in jedem Abschnitt

with problemsDoc.create(Section('Normalform zu Scheitelpunktsform')), solutionsDoc.create(Section('Normalform zu Scheitelpunktsform')):
    problemsDoc.append(f"Gegeben ist die Normalform. Bestimme die jeweilige Scheitelpunktsform.")
    solutionsDoc.append(f"Für die Normalform ... ist die Scheitelpunktsform ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, b, c = normalform()
            a2, d, e = nzuspform(a, b, c)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r"\Leftrightarrow "+printscheitelpunktform(a2, d, e)+r"$"))


with problemsDoc.create(Section('Scheitelpunktsform zu Faktorisierten Form')), solutionsDoc.create(Section('Scheitelpunktsform zu Faktorisierten Form')):
    problemsDoc.append(f"Gegeben ist die Scheitelpunktsform. Bestimme die jeweilige Faktorisierte Form.")
    solutionsDoc.append(f"Für die Scheitelpunktsform ... ist die Faktorisierte Form ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, n1, n2 = faktorisierteform()
            a, d, e = fzuspform(a2, n1, n2)
           
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a, d, e)+r"\Leftrightarrow "+printfaktorisierteform(a2,n1,n2)+r"$"))

with problemsDoc.create(Section('Faktorisierte Form zu Normalform')), solutionsDoc.create(Section('Faktorisierte Form zu Normalform')):
    problemsDoc.append(f"Gegeben ist die Faktorisierte Form. Bestimme die jeweilige Normalform.")
    solutionsDoc.append(f"Für die Faktorisierte Form ... ist die Normalform ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            a2, b, c = fzunform(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r"\Leftrightarrow "+printnormalform(a2,b,c)+r"$"))

with problemsDoc.create(Section('Normalform zu Faktorisierter Form')), solutionsDoc.create(Section('Normalform zu Faktorisierter Form')):
    problemsDoc.append(f"Gegeben ist die Normalalsform. Bestimme die jeweilige Faktorisierte Form.")
    solutionsDoc.append(f"Für die Normalform ... ist die Faktorisierte Form ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, n1, n2 = faktorisierteform()
            a, b, c = fzunform(a2, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r"\Leftrightarrow "+printfaktorisierteform(a2,n1,n2)+r"$"))

with problemsDoc.create(Section('Scheitelpunktform zu Normalform')), solutionsDoc.create(Section('Scheitelpunktform zu Normalform')):
    problemsDoc.append(f"Gegeben ist die Scheitelpunktform. Bestimme die jeweilige Normalform.")
    solutionsDoc.append(f"Für die Scheitelpunktform ... ist die Normalform ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, d, e = scheitelpunktform()
            a, b, c = spzunform(a2, d, e)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a2,d,e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a2,d,e)+r"\Leftrightarrow "+printnormalform(a,b,c)+r"$"))

with problemsDoc.create(Section('Faktorisierte Form zu Scheitelpunktform')), solutionsDoc.create(Section('Faktorisierte Form zu Scheitelpunktform')):
    problemsDoc.append(f"Gegeben ist die Faktorisierte Form. Bestimme die jeweilige Scheitelpunktform.")
    solutionsDoc.append(f"Für die Faktorisierte Form ... ist die Scheitelpunktform ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            a2, d, e = fzuspform(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r"\Leftrightarrow "+printscheitelpunktform(a2,d,e)+r"$"))

with problemsDoc.create(Section('Scheitelpunktform: Bestimme den Scheitelpunkt')), solutionsDoc.create(Section('Scheitelpunktform: Bestimme den Scheitelpunkt')):
    problemsDoc.append(f"Gegeben ist die Scheitelpunktform. Bestimme den Scheitelpunkt.")
    solutionsDoc.append(f"Für die Scheitelpunktform ... ist der Scheitelpunkt ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, d, e = scheitelpunktform()

            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a2, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a2, d, e)+r" \Rightarrow SP("+str(d)+r"|"+str(e)+r") $"))

with problemsDoc.create(Section('Normalform: Bestimme den Scheitelpunkt')), solutionsDoc.create(Section('Normalform: Bestimme den Scheitelpunkt')):
    problemsDoc.append(f"Gegeben ist die Normalform. Bestimme den Scheitelpunkt.")
    solutionsDoc.append(f"Für die Normalform ... ist der Scheitelpunkt ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, d, e = scheitelpunktform()
            a, b, c = spzunform(a2, d, e)

            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a,b,c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a,b,c)+r" \Rightarrow SP("+str(d)+r"|"+str(e)+r") $"))

with problemsDoc.create(Section('Faktorisierte Form: Bestimme den Scheitelpunkt')), solutionsDoc.create(Section('Faktorisierte Form: Bestimme den Scheitelpunkt')):
    problemsDoc.append(f"Gegeben ist die Faktorisierte Form. Bestimme den Scheitelpunkt.")
    solutionsDoc.append(f"Für die Faktorisierte Form ... ist der Scheitelpunkt ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):

            a, n1, n2 = faktorisierteform()
            a2, d, e = fzuspform(a, n1, n2)

            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r" \Rightarrow SP("+str(d)+r"|"+str(e)+r") $"))

with problemsDoc.create(Section('Faktorisierte Form: Bestimme die Nullstellen')), solutionsDoc.create(Section('Faktorisierte Form: Bestimme die Nullstellen')):
    problemsDoc.append(f"Gegeben ist die Faktorisierte Form. Bestimme die Nullstellen.")
    solutionsDoc.append(f"Für die Faktorisierte Form ... sind die Nullstellen ....")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            ns = bestimme_nullstellen_ff(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r" \Rightarrow "+anzahlns(ns)+r" $"))

with problemsDoc.create(Section('Normalform: Bestimme die Nullstellen')), solutionsDoc.create(Section('Normalform: Bestimme die Nullstellen')):
    problemsDoc.append(f"Gegeben ist die Normalform. Bestimme die Nullstellen.")
    solutionsDoc.append(f"Für die Normalform ... sind die Nullstellen ....")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions*2):
            a, b, c = normalform()
            ns = bestimme_nullstellen_nf(a, b, c)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r" \Rightarrow "+anzahlns(ns)+r" $"))

with problemsDoc.create(Section('Scheitelpunktform: Bestimme die Nullstellen')), solutionsDoc.create(Section('Scheitelpunktform: Bestimme die Nullstellen')):
    problemsDoc.append(f"Gegeben ist die Scheitelpunktform. Bestimme die Nullstellen.")
    solutionsDoc.append(f"Für die Scheitelpunktform ... sind die Nullstellen ....")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions*2):
            a, d, e = scheitelpunktform()
            ns = bestimme_nullstellen_sf(a, d, e)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a, d, e)+r" \Rightarrow "+anzahlns(ns)+r" $"))

with problemsDoc.create(Section('Normalform: Bestimme den Y-Achsenabschnitt')), solutionsDoc.create(Section('Normalform: Bestimme den Y-Achsenabschnitt')):
    problemsDoc.append(f"Gegeben ist die Normalform. Bestimme den Y-Achsenabschnitt.")
    solutionsDoc.append(f"Für die Normalform ...ist der Y-Achsenabschnitt ....")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, b, c = normalform()
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r" \Rightarrow $ Y-Achsenabschnitt: $ (0|"+str(c)+r") $"))

with problemsDoc.create(Section('Scheitelpunktform: Bestimme den Y-Achsenabschnitt')), solutionsDoc.create(Section('Scheitelpunktform: Bestimme den Y-Achsenabschnitt')):
    problemsDoc.append(f"Gegeben ist die Scheitelpunktform. Bestimme den Y-Achsenabschnitt.")
    solutionsDoc.append(f"Für die Scheitelpunktform ...ist der Y-Achsenabschnitt ....")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, d, e = scheitelpunktform()
            a2, b, c = spzunform(a, d, e)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a, d, e)+r" \Rightarrow $ Y-Achsenabschnitt: $ (0|"+str(c)+r") $"))

with problemsDoc.create(Section('Faktorisierte Form: Bestimme den Y-Achsenabschnitt')), solutionsDoc.create(Section('Faktorisierte Form: Bestimme den Y-Achsenabschnitt')):
    problemsDoc.append(f"Gegeben ist die Faktorisierte Form. Bestimme den Y-Achsenabschnitt.")
    solutionsDoc.append(f"Für die Faktorisierte Form ...ist der Y-Achsenabschnitt ....")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            a2, b, c = fzunform(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r" \Rightarrow $ Y-Achsenabschnitt: $ (0|"+str(c)+r") $"))

with problemsDoc.create(Section('Finde die Funktionsgleichung')), solutionsDoc.create(Section('Finde die Funktionsgleichung')):
    problemsDoc.append(f"Finde die Funktionsgleichung.")
    solutionsDoc.append(f"Die Funktionsgleichung ist ...")
    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions*2):
            a2, n1, n2 = faktorisierteform()
            a, b, c = fzunform(a2, n1, n2)
            a3, d, e = nzuspform(a,b,c)
            while a2 is None or isclose(d, 0.0) or not float(d).is_integer() or not float(e).is_integer():
                a2, n1, n2 = faktorisierteform()
                a, b, c = fzunform(a2, n1, n2)
                a3, d, e = nzuspform(a,b,c)

            x1, x2, x3 = random.sample(range(-100, 100), 3)
            while x1 == x2 or x2 == x3 or x1 == x3:
                x1, x2, x3 = random.sample(range(-100, 100), 3)
            y1, y2, y3 = a*x1**2 + b*x1 + c, a*x2**2 + b*x2 + c, a*x3**2 + b*x3 + c
            
            if chance(0.2):
                enum1.add_item(NoEscape(r" Die Funktion geht durch die Punkte $("+str(x1)+r"|"+str(y1)+r"),("+str(x2)+r"|"+str(y2)+r")$ und $("+str(x3)+r"|"+str(y3)+r")$"))
                enum2.add_item(NoEscape(r" Punkte $("+str(x1)+r"|"+str(y1)+r"),("+str(x2)+r"|"+str(y2)+r")$ und $("+str(x3)+r"|"+str(y3)+r") \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            elif chance(0.2):
                enum1.add_item(NoEscape(r" Die Funktion geht durch den Punkt $("+str(x1)+r"|"+str(y1)+r")$ und hat den Scheitelpunkt $("+str(d)+r"|"+str(e)+r")$"))
                enum2.add_item(NoEscape(r" Punkt $("+str(x1)+r"|"+str(y1)+r")$ und Scheitelpunkt $("+str(d)+r"|"+str(e)+r") \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            elif chance(0.2):
                enum1.add_item(NoEscape(r" Die Funktion geht durch den Scheitelpunkt $("+str(d)+r"|"+str(e)+r")$ und hat den Y-Achsenabschnitt $"+str(c)+r"$"))
                enum2.add_item(NoEscape(r" Punkt Scheitelpunkt $("+str(d)+r"|"+str(e)+r")$ und Y-Achsenabschnitt $"+str(c)+r" \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            elif chance(0.2):
                enum1.add_item(NoEscape(r" Die Funktion geht durch den Punkt $("+str(x1)+r"|"+str(y1)+r")$ und hat die Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r"$"))
                enum2.add_item(NoEscape(r" Die Funktion geht durch den Punkt $("+str(x1)+r"|"+str(y1)+r")$ und hat die Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r" \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            else:
                enum1.add_item(NoEscape(r" Die Funktion hat die Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r"$ und den Scheitelpunkt $("+str(d)+r"|"+str(e)+r")$"))
                enum2.add_item(NoEscape(r" Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r"$ und Scheitelpunkt $("+str(d)+r"|"+str(e)+r") \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))

try:
    problemsDoc.generate_pdf("QuadratischeFnAfg", clean_tex=True)
except Exception as e:
    print(e)
try:
    solutionsDoc.generate_pdf("QuadratischeFnLsg", clean_tex=True)
except Exception as e:
    print(e)