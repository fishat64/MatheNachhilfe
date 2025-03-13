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

def getLGS(noUnbekannte):
    xs = np.random.randint(1, 10, (noUnbekannte,1))
    wxs = np.random.randint(1, 10, (noUnbekannte, noUnbekannte+1))
    print(xs.shape, wxs.shape)
    #wxs[:,:-1] = wxs[:,:-1].T
    ys = np.dot(xs.T[:], wxs[:,:-1])+wxs[:,-1]

    print(xs.T[:], wxs[:,:-1], wxs[:, -1], ys)
    wxs[:,:-1] = wxs[:,:-1].T
    return xs, wxs, ys

def printlinearegleichung(a, b, c):
    return f"{vorzeichen(a, np=True)}{abs(a)}x{vorzeichen(b)}{abs(b)}={c}"

variables = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

def printegleichung(wxs, ys):
    s = ""
    for i in range(0, len(wxs)-1):
        s += f"{vorzeichen(wxs[i], np=(i==0))}{abs(wxs[i])}{variables[i]}"
    s += f"{vorzeichen(wxs[-1])}{abs(wxs[-1])}"
    s += f"={ys[0]}"
    return s

problemsDoc = Document() # Aufgaben dokument
thisuuid = str(uuid.uuid4())
problemsDoc.preamble.append(Command("title", NoEscape(r'Lineare Gleichungssysteme - Aufgaben \newline '+thisuuid)))
problemsDoc.preamble.append(Command("date", NoEscape(r"\today")))
problemsDoc.packages.append(Package('xcolor'))
problemsDoc.append(NoEscape(r"\maketitle"))

solutionsDoc = Document() # Lösungen dokument
solutionsDoc.preamble.append(Command("title", NoEscape(r'Lineare Gleichungssysteme - Lösungen \newline '+thisuuid)))
solutionsDoc.preamble.append(Command("date", NoEscape(r"\today")))
solutionsDoc.packages.append(Package('xcolor'))
solutionsDoc.append(NoEscape(r"\maketitle"))

numberofquestions = 15 # Anzahl der Fragen in jedem Abschnitt

with problemsDoc.create(Section('Lineare Gleichungen mit einer Variablen')), solutionsDoc.create(Section('Lineare Gleichungen mit einer Variablen')):
    problemsDoc.append(f"Bestimme X.")
    solutionsDoc.append(f"Für die Gleichung ... ist die Lösungsmenge ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            xs, wxs, ys = getLGS(1)
            enum1.add_item(NoEscape(r"\newline\vspace{0.5cm} $"+printlinearegleichung(wxs[0,0], wxs[0,1], ys[0,0])+r"$"))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+printlinearegleichung(wxs[0,0], wxs[0,1], ys[0, 0])+r"\Leftrightarrow x="+str(xs[0,0])+r"$"))

with problemsDoc.create(Section('Lineare Gleichungssysteme mit zwei Variablen')), solutionsDoc.create(Section('Lineare Gleichungssysteme mit zwei Variablen')):
    def verfahren():
        return "Additionsverfahren" if chance(0.3) else "Einsetzungsverfahren" if chance(0.5) else "Gleichsetzungsverfahren" if chance(0.7) else "Verfahren deiner Wahl"
    problemsDoc.append(f"Bestimme die Unbekannten, wende das ... an.")
    solutionsDoc.append(f"Für die Gleichung ... ist die Lösungsmenge ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            num = 2
            xs, wxs, ys = getLGS(num)
            s1 = r"\newline\vspace{0.5cm} $"
            for i in range(0, num):
                s1 += printegleichung(wxs[i], ys.T[i]) + r"\newline"
            s1+=r"$"

            s2 = ""
            for i in range(0, num):
                s2 += f"{variables[i]}={xs[i][0]}, "

            enum1.add_item(NoEscape(verfahren()+" "+s1))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+s1+r"\Leftrightarrow "+s2+r"$"))

with problemsDoc.create(Section('Lineare Gleichungssysteme mit drei Variablen')), solutionsDoc.create(Section('Lineare Gleichungssysteme mit drei Variablen')):
    problemsDoc.append(f"Bestimme die Unbekannten.")
    solutionsDoc.append(f"Für die Gleichung ... ist die Lösungsmenge ....")

    with problemsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum1, solutionsDoc.create(
        Enumerate(enumeration_symbol=r"\alph*)")
    ) as enum2:
        for i in range(numberofquestions):
            num = 3
            xs, wxs, ys = getLGS(num)
            s1 = r"\newline\vspace{0.5cm} $"
            for i in range(0, num):
                s1 += printegleichung(wxs[i], ys.T[i]) + r"\newline"
            s1+=r"$"

            s2 = ""
            for i in range(0, num):
                s2 += f"{variables[i]}={xs[i][0]}, "

            enum1.add_item(NoEscape(s1))
            enum2.add_item(NoEscape(r"\newline\vspace{0.5cm}$"+s1+r"\Leftrightarrow "+s2+r"$"))
try:
    problemsDoc.generate_pdf("LinGSAfg", clean_tex=True)
except Exception as e:
    print(e)
try:
    solutionsDoc.generate_pdf("LinGSLsg", clean_tex=True)
except Exception as e:
    print(e)