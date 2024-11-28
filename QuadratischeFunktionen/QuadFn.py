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


def normalform(min=1, max=10):
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


def printnormalform(a, b, c):
    print("NF", a, b, c)
    mystring = f"f(x)={vorzeichen(a, np=True)}{vgl1(abs(a))}x^2"
    if not isclose(b, 0.0):
        mystring += f" {vorzeichen(b)} {vgl1(abs(b))}x"
    if not isclose(c, 0.0):
        mystring += f" {vorzeichen(c)} {abs(c)}"
    return mystring

def bestimme_nullstellen_nf(a, b, c):
    d = -c/a + (b/(2*a))**2
    if d < 0:
        return []
    elif isclose(d, 0.0):
        return [+b/(2*a)]
    else:
        return [math.sqrt(d)+b/(2*a), -math.sqrt(d)+b/(2*a)]

def nzuspform(a,b,c):
    return a, b/(2*a), c-(b**2)/(4*a)

def scheitelpunktform(min=1, max=10):
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

def printscheitelpunktform(a, d, e):
    print("SPF", a, d, e)
    mystring = f"f(x)={vorzeichen(a, np=True)}{vgl1(abs(a))}"
    if not isclose(d, 0.0):
        mystring += f"(x{vorzeichen(d*-1)}{(abs(d))})^2"
    else:
        mystring += "(x)^2"
    if not isclose(e, 0.0):
        mystring += f" {vorzeichen(e)}{(abs(e))}"
    return mystring

def spzunform(a, d, e):
    return a, 2*a*d, a*d**2+e

def bestimme_nullstellen_sf(a, d, e):
    e = -e/a
    if e < 0:
        return []
    elif isclose(e, 0.0):
        return [-d]
    else:
        return [math.sqrt(e)+d, -math.sqrt(e)+d]


def spzufform(a, d, e):
    ns = bestimme_nullstellen_sf(a, d, e)
    if len(ns) == 0:
        return None, None, None
    elif len(ns) == 1:
        return a, 0, -ns[0]
    else:
        return a, -ns[0], -ns[1]

def fzuspform(a, n1, n2):
    return a, (n1+n2)/2, a*(((n1+n2)/2)**2 - n1*n2)

def nzufform(a, b, c):
    ns = bestimme_nullstellen_nf(a, b, c)
    if len(ns) == 0:
        return None, None, None
    elif len(ns) == 1:
        return a, 0, -ns[0]
    else:
        return a, -ns[0], -ns[1]

def fzunform(a, n1, n2):
    return a, (n1+n2)*a, n1*n2*a


    

def faktorisierteform(min=1, max=10):
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

def printfaktorisierteform(a, n1, n2):
    print("FF", a, n1, n2)
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

def bestimme_nullstellen_ff(a, n1, n2):
    return [-n1, -n2]

def getfn3pkt(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    a = (y1-y3- (((x1-x3)*(y2-y3))/(x2-x3))) / (x1**2 -x3**2 + (x1-x3)*((x3**2-x2**2)/(x2-x3)))
    b = (y2-y3+a*(x3**2-x2**2))/(x2-x3)
    c = y3 - a*x3**2 - b*x3

    return a, b, c

def getfnSpPkt(sp, p):
    x1, y1 = sp
    x2, y2 = p

    a = (y1-y2) / (x1**2 - 2*x1**2 + 2*x1*x2 - x2**2)
    b = -2*a*x1
    c = y2 +2*a*x1*x2 - a*x2**2

    return a, b, c


def getnormalfunction(ns=[], yaa=None, pkt=[], sp=None):
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

def testGetNormalFunction():
    for i in range(1):
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




doc = Document()
thisuuid = str(uuid.uuid4())
doc.preamble.append(Command("title", NoEscape(r'Quadratische Funktionen - Aufgaben \newline '+thisuuid)))
doc.preamble.append(Command("date", NoEscape(r"\today")))
doc.packages.append(Package('xcolor'))
doc.append(NoEscape(r"\maketitle"))

doc2 = Document()
doc2.preamble.append(Command("title", NoEscape(r'Quadratische Funktionen - Lösungen \newline '+thisuuid)))
doc2.preamble.append(Command("date", NoEscape(r"\today")))
doc2.packages.append(Package('xcolor'))
doc2.append(NoEscape(r"\maketitle"))

numberofquestions = 3

with doc.create(Section('Normalform zu Scheitelpunktsform')), doc2.create(Section('Normalform zu Scheitelpunktsform')):
    doc.append(f"Gegeben ist die Normalform. Bestimme die jeweilige Scheitelpunktsform.")
    doc2.append(f"Für die Normalform ... ist die Scheitelpunktsform ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, b, c = normalform()
            a2, d, e = nzuspform(a, b, c)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r"\Leftrightarrow "+printscheitelpunktform(a2, d, e)+r"$"))


with doc.create(Section('Scheitelpunktsform zu Faktorisierten Form')), doc2.create(Section('Scheitelpunktsform zu Faktorisierten Form')):
    doc.append(f"Gegeben ist die Scheitelpunktsform. Bestimme die jeweilige Faktorisierte Form.")
    doc2.append(f"Für die Scheitelpunktsform ... ist die Faktorisierte Form ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, n1, n2 = faktorisierteform()
            a, d, e = fzuspform(a2, n1, n2)
           
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a, d, e)+r"\Leftrightarrow "+printfaktorisierteform(a2,n1,n2)+r"$"))

with doc.create(Section('Faktorisierte Form zu Normalform')), doc2.create(Section('Faktorisierte Form zu Normalform')):
    doc.append(f"Gegeben ist die Faktorisierte Form. Bestimme die jeweilige Normalform.")
    doc2.append(f"Für die Faktorisierte Form ... ist die Normalform ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            a2, b, c = fzunform(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r"\Leftrightarrow "+printnormalform(a2,b,c)+r"$"))

with doc.create(Section('Normalform zu Faktorisierter Form')), doc2.create(Section('Normalform zu Faktorisierter Form')):
    doc.append(f"Gegeben ist die Normalalsform. Bestimme die jeweilige Faktorisierte Form.")
    doc2.append(f"Für die Normalform ... ist die Faktorisierte Form ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, n1, n2 = faktorisierteform()
            a, b, c = fzunform(a2, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r"\Leftrightarrow "+printfaktorisierteform(a2,n1,n2)+r"$"))

with doc.create(Section('Scheitelpunktform zu Normalform')), doc2.create(Section('Scheitelpunktform zu Normalform')):
    doc.append(f"Gegeben ist die Scheitelpunktform. Bestimme die jeweilige Normalform.")
    doc2.append(f"Für die Scheitelpunktform ... ist die Normalform ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, d, e = scheitelpunktform()
            a, b, c = spzunform(a2, d, e)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a2,d,e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a2,d,e)+r"\Leftrightarrow "+printnormalform(a,b,c)+r"$"))

with doc.create(Section('Faktorisierte Form zu Scheitelpunktform')), doc2.create(Section('Faktorisierte Form zu Scheitelpunktform')):
    doc.append(f"Gegeben ist die Faktorisierte Form. Bestimme die jeweilige Scheitelpunktform.")
    doc2.append(f"Für die Faktorisierte Form ... ist die Scheitelpunktform ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            a2, d, e = fzuspform(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r"\Leftrightarrow "+printscheitelpunktform(a2,d,e)+r"$"))

with doc.create(Section('Scheitelpunktform: Bestimme den Scheitelpunkt')), doc2.create(Section('Scheitelpunktform: Bestimme den Scheitelpunkt')):
    doc.append(f"Gegeben ist die Scheitelpunktform. Bestimme den Scheitelpunkt.")
    doc2.append(f"Für die Scheitelpunktform ... ist der Scheitelpunkt ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, d, e = scheitelpunktform()

            d2 = d*-1

            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a2, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a2, d, e)+r" \Rightarrow SP("+str(d2)+r"|"+str(e)+r") $"))

with doc.create(Section('Normalform: Bestimme den Scheitelpunkt')), doc2.create(Section('Normalform: Bestimme den Scheitelpunkt')):
    doc.append(f"Gegeben ist die Normalform. Bestimme den Scheitelpunkt.")
    doc2.append(f"Für die Normalform ... ist der Scheitelpunkt ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a2, d, e = scheitelpunktform()
            a, b, c = spzunform(a2, d, e)
            d2 = d*-1

            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a,b,c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a,b,c)+r" \Rightarrow SP("+str(d2)+r"|"+str(e)+r") $"))

with doc.create(Section('Faktorisierte Form: Bestimme den Scheitelpunkt')), doc2.create(Section('Faktorisierte Form: Bestimme den Scheitelpunkt')):
    doc.append(f"Gegeben ist die Faktorisierte Form. Bestimme den Scheitelpunkt.")
    doc2.append(f"Für die Faktorisierte Form ... ist der Scheitelpunkt ....")

    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):

            a, n1, n2 = faktorisierteform()
            a2, d, e = fzuspform(a, n1, n2)
            d2 = d*-1

            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r" \Rightarrow SP("+str(d2)+r"|"+str(e)+r") $"))

with doc.create(Section('Faktorisierte Form: Bestimme die Nullstellen')), doc2.create(Section('Faktorisierte Form: Bestimme die Nullstellen')):
    doc.append(f"Gegeben ist die Faktorisierte Form. Bestimme die Nullstellen.")
    doc2.append(f"Für die Faktorisierte Form ... sind die Nullstellen ....")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            ns = bestimme_nullstellen_ff(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r" \Rightarrow "+anzahlns(ns)+r" $"))

with doc.create(Section('Normalform: Bestimme die Nullstellen')), doc2.create(Section('Normalform: Bestimme die Nullstellen')):
    doc.append(f"Gegeben ist die Normalform. Bestimme die Nullstellen.")
    doc2.append(f"Für die Normalform ... sind die Nullstellen ....")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions*2):
            a, b, c = normalform()
            ns = bestimme_nullstellen_nf(a, b, c)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r" \Rightarrow "+anzahlns(ns)+r" $"))

with doc.create(Section('Scheitelpunktform: Bestimme die Nullstellen')), doc2.create(Section('Scheitelpunktform: Bestimme die Nullstellen')):
    doc.append(f"Gegeben ist die Scheitelpunktform. Bestimme die Nullstellen.")
    doc2.append(f"Für die Scheitelpunktform ... sind die Nullstellen ....")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions*2):
            a, d, e = scheitelpunktform()
            ns = bestimme_nullstellen_sf(a, d, e)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a, d, e)+r" \Rightarrow "+anzahlns(ns)+r" $"))

with doc.create(Section('Normalform: Bestimme den Y-Achsenabschnitt')), doc2.create(Section('Normalform: Bestimme den Y-Achsenabschnitt')):
    doc.append(f"Gegeben ist die Normalform. Bestimme den Y-Achsenabschnitt.")
    doc2.append(f"Für die Normalform ...ist der Y-Achsenabschnitt ....")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, b, c = normalform()
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printnormalform(a, b, c)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printnormalform(a, b, c)+r" \Rightarrow $ Y-Achsenabschnitt: $ (0|"+str(c)+r") $"))

with doc.create(Section('Scheitelpunktform: Bestimme den Y-Achsenabschnitt')), doc2.create(Section('Scheitelpunktform: Bestimme den Y-Achsenabschnitt')):
    doc.append(f"Gegeben ist die Scheitelpunktform. Bestimme den Y-Achsenabschnitt.")
    doc2.append(f"Für die Scheitelpunktform ...ist der Y-Achsenabschnitt ....")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, d, e = scheitelpunktform()
            a2, b, c = spzunform(a, d, e)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printscheitelpunktform(a, d, e)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printscheitelpunktform(a, d, e)+r" \Rightarrow $ Y-Achsenabschnitt: $ (0|"+str(c)+r") $"))

with doc.create(Section('Faktorisierte Form: Bestimme den Y-Achsenabschnitt')), doc2.create(Section('Faktorisierte Form: Bestimme den Y-Achsenabschnitt')):
    doc.append(f"Gegeben ist die Faktorisierte Form. Bestimme den Y-Achsenabschnitt.")
    doc2.append(f"Für die Faktorisierte Form ...ist der Y-Achsenabschnitt ....")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            a, n1, n2 = faktorisierteform()
            a2, b, c = fzunform(a, n1, n2)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printfaktorisierteform(a, n1, n2)+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printfaktorisierteform(a, n1, n2)+r" \Rightarrow $ Y-Achsenabschnitt: $ (0|"+str(c)+r") $"))

with doc.create(Section('Finde die Funktionsgleichung')), doc2.create(Section('Finde die Funktionsgleichung')):
    doc.append(f"Finde die Funktionsgleichung.")
    doc2.append(f"Die Funktionsgleichung ist ...")
    with doc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, doc2.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions*3):
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
                enum1.add_item(NoEscape(r" Die Funktion geht durch den Punkt $("+str(x1)+r"|"+str(y1)+r")$ und hat den Scheitelpunkt $("+str(-d)+r"|"+str(e)+r")$"))
                enum2.add_item(NoEscape(r" Punkt $("+str(x1)+r"|"+str(y1)+r")$ und Scheitelpunkt $("+str(-d)+r"|"+str(e)+r") \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            elif chance(0.2):
                enum1.add_item(NoEscape(r" Die Funktion geht durch den Scheitelpunkt $("+str(-d)+r"|"+str(e)+r")$ und hat den Y-Achsenabschnitt $"+str(c)+r"$"))
                enum2.add_item(NoEscape(r" Punkt Scheitelpunkt $("+str(-d)+r"|"+str(e)+r")$ und Y-Achsenabschnitt $"+str(c)+r" \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            elif chance(0.2):
                enum1.add_item(NoEscape(r" Die Funktion geht durch den Punkt $("+str(x1)+r"|"+str(y1)+r")$ und hat die Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r"$"))
                enum2.add_item(NoEscape(r" Die Funktion geht durch den Punkt $("+str(x1)+r"|"+str(y1)+r")$ und hat die Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r" \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))
            else:
                enum1.add_item(NoEscape(r" Die Funktion hat die Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r"$ und den Scheitelpunkt $("+str(-d)+r"|"+str(e)+r")$"))
                enum2.add_item(NoEscape(r" Nullstellen $"+str(n1)+r"$ und $"+str(n2)+r"$ und Scheitelpunkt $("+str(-d)+r"|"+str(e)+r") \Rightarrow "+printnormalform(a, b, c)+r" ; "+printfaktorisierteform(a,n1,n2)+r" ; "+printscheitelpunktform(a,d,e)+r"$"))

try:
    doc.generate_pdf("QuadratischeFnAfg", clean_tex=True)
except Exception as e:
    print(e)
try:
    doc2.generate_pdf("QuadratischeFnLsg", clean_tex=True)
except Exception as e:
    print(e)