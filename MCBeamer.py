8*20*5# -*- coding: utf-8 -*-
"""
Created on Monday Dec 19, 2016 8:58:00

@author: Celso Co
"""

from ccoLatex import *  #This is the library for Python-Tex coding.

from Figure import *

from sympy import Union, Intersection


#Carriage Return Short Cuts
cR="\ \\newline\n\n\\noindent "

#initialize the PyLx as class PyLatex

author="Engr Celso Bation Co, Ph.D, PECE"
title="Switch Mode Power Supply (SMP) Electronics: An Alternative Perspective"
subtitle=""
institute="Technological Institute of the Philippines"
subject=""
date=""
logo="\includegraphics[width=.15\linewidth,height=.4cm]{LogoNTS2019.png}"
TitlePage="TitlePageMCS2019.png"

#Begin To be filled up by the user
headers="\
\\documentclass[11pt]{beamer}\n\
\\usetheme{default}\n\
\\usepackage[ascii]{inputenc}\n\
\\usepackage[T1]{fontenc}\n\
\\usepackage{amsmath}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{graphicx}\n\
\\begin{document}\n\
\\begin{center}\n\
\\includegraphics[width=11cm,height=8cm,clip]{"+TitlePage+"}\n\
\\end{center}\n\
\\author{"+author+"}\n\
\\title{"+title+"}\n\
\\subtitle{"+subtitle+"}\n\
\\logo{"+logo+"}\n\
\\institute{"+institute+"}\n\
\\date{"+date+"}\n\
\\subject{"+subject+"}\n\
\\setbeamercovered{transparent}\n\
\\setbeamertemplate{navigation symbols}{}\n\
%\\maketitle\n\n"


title="Title"
author_data="Author"
#End To be filled by the user



#\\documentclass[10pt,a4paper]{article}\n\

PyBe=PyBeamer(Headers=headers)

At=PyBe.Append_Text            #Append Frame variable
Cf=PyBe.Create_Frame                 #create Frame
LT=laplace_transform
ILT=inverse_laplace_transform
Ae=PyBe.Append_Expression      #Short cut for Atf(Ae(s,n='',c-''))
Ce=PyBe.Append_Equation        #Short cut for At(Ae(Eq(left,right),n="",c=""))
Pb=PyBe.Build                        #Build Latex File
Lx=PyBe.Adjust_Latex                 #Convert text to Latex with adjustment
If=PyBe.Insert_Figure                       #Insert figure
eQ=PyBe.eQ                           #Equation List
Se=PyBe.Split_Expression             #Split the varialbe into n segments for display
FD=PyBe.FrameData                    #Contend of Frame

#Carriage Return Short Cuts
cR="\\newline\n\n\\noindent "



#Symbols

lT, ilT, a, b, n, dlt =symbols("\\mathcal{L}_{t} \\mathcal{L}_{t}^{-1} \
                                a b n \\delta")


#Content

#Begin to be filled by user

#Abstract
Abstract=\
"The processs variability covers typically the material, equipment, method, \
 and man, the so-called 4 Ms'.  A simple process of cutting a 10-meter rod into \
 two equal halves is illustrated where all the 4Ms were treated. The simulation \
 of variability for the 4 Ms' were discussed. The theoretical perspective \
 has caveat on matter of mathematical expressions that are realistics. The \
 algorith used was Monte Carlo Simulation based on random number generation that \
 fit Gaussian Curve. The python programming language was used with symbolic \
 math library, the sympy. Although the industry is used to 99.99\%, for the \
 sake tutotial the academe toys around 50\%. "


At("Process of Cutting a number of 10-meter Rods  \\\  \ \\\ \
    $\\bullet$ Material \\\ \
    $\\bullet$ Machine \\\ \
    $\\bullet$ Method \\\ \
    $\\bullet$ Man ")

#End to be filled by user

#Begin Slide 1
#Begin to be filled by user

#Keywords
Keywords=\
   "variability, Normal Distribution, Gausian, Man, Machine, Method, Material, \
    4Ms."
#End to be filled by user

At("\\\ \ \\\Keywords: "+Keywords)
Cf(title="Abstract")
#End Slide 1


#Begind Slide 2

#1 Introduction
At("\\section{Introduction}")

#Begin to be filled by user

from ccoLatex import *  #This is the library for Python-Tex coding.
from sympy.stats import Normal, density, E, std, cdf, skewness
from sympy import Symbol, simplify, pprint, factor, together, factor_terms, symbols

f, x, sigma, mu, fx = symbols("f x \\sigma \\mu f(x)")


Ce(fx,1/(sigma*sqrt(2*pi))*exp(-(x-mu)**2/(2*sigma**2)).simplify())  #1

At("where :	\\\ \
$\\mu$    : Real number or a list representing the mean or the mean vector \\\ \
$\\sigma$ : Real number or a positive definite square matrix, \\\ "+
Lx(Gt(sigma**2, 0))+" the variance \\\ \
Returns: A Random Symbol. \\\ \ \\\ ")

z, zi, zf, y, d, f1, f2, f3, p, X = symbols("z z_i z_f y density f1 f2 f3 p X")
f2x, f1z, f1x, f2z, f3z = symbols("f(x) f{_1}(z) f{_1}(x) f{_2}(z) f{_3}(z)")
from sympy.stats import Normal, density, E, std, cdf, skewness
from sympy import Symbol, simplify, pprint, factor, together, factor_terms


X = Normal("x", mu, sigma)
sf1=simplify(density(X))
Cf(title="Introduction: Gaussian Distribution Function")
#End Slide 2


#Begin Slide 3

At("The sympy function ")
Ce(f1,sf1)  #2
At("declares "+Lx(f1)+" as the normal distribution function. The random \
    variable of "+Lx(z)+" of it is expressed as follows.")
sf1z=eQ[1].rhs.subs(x,z)
Ce(f1z,sf1z)  #3


At("Integratinng (3), we have the following.")
sf2z=sf1z.integrate((z,zi,zf))
Ae(latex(Eq(f2z,Integral(f1z,(z,zi,zf))))+" = \\\ "+
   latex(sf2z))  #4
Cf(title="Introduction: Gaussian Distribution Sympy Function")
#End Slide 3


#Begin Slide 4
At("Let "+Lx(Eq(mu,0))+" and "+Lx(Eq(sigma,1))+" then  "+Lx(f2)+
   " from "+Lx(Eq(zi,-oo))+" to "+Lx(Eq(zf,+oo))+" we have normal probability \
   distribution as follows.")
Ce(Eq(f2z,Integral(f1z,(z,-oo,oo))),
   sf2z.subs(zi,-oo).subs(zf,oo).subs(sigma,1).subs(mu,0))  #5

At("Probabilities of Multiple of $\\sigma$ ")

Ce(Eq(Integral(f1z,(z,-1,1)),
      sf2z.subs(zi,-1).subs(zf,1).subs(sigma,1).subs(mu,0)),
      sf2z.subs(zi,-1).subs(zf,1).subs(sigma,1).subs(mu,0).evalf())  #6

Ce(Eq(Integral(f1z,(z,-3,3)),
      sf2z.subs(zi,-3).subs(zf,3).subs(sigma,1).subs(mu,0)),
      sf2z.subs(zi,-3).subs(zf,3).subs(sigma,1).subs(mu,0).evalf())  #7

Ce(Eq(Integral(f1z,(z,-6,6)),
      sf2z.subs(zi,-6).subs(zf,6).subs(sigma,1).subs(mu,0)),
      sf2z.subs(zi,-6).subs(zf,6).subs(sigma,1).subs(mu,0).evalf())  #8

Cf(title="Introduction: Gaussian Distribution Normalized Function")
#End Slide 4


#Begin Slide 5
dpm = symbols("DPM")

Ce(dpm,(1-eQ[6].rhs)*1e6)    #9
Ce(dpm,(1-eQ[7].rhs)*1e6)    #10
Ce(dpm,(1-eQ[8].rhs)*1e6)    #11
Cf(title="Introduction: DPM")
#End Slide 5


#Begin Slide 6
At("$\\bullet$The variablilities are quantified in terms of variance.  \\\ \ \\\ \
    $\\bullet$The variance are associated with tolerances and/or errors \\\ \ \\\ \
    $\\bullet$Let 10000 be the number of instances.")

Cf(title="Simulation of Variables")
#End Slide 6

#Begin Slide 7
nrodmu=10
nrodsigma=1
count=10000
At("A set of values of $z$ can be generated randomly by the sympy function \
   \\\ \ \\\  $Normal(\\mu, \\sigma)$. Given  "+ Lx(Eq(mu,nrodmu))+" and "+
   Lx(Eq(sigma,nrodsigma))+" then for "+str(count)+ " pieces we have \\\ ")

nN=[]
dm=linspace(0,count,count)

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2

nrod = random.normal(nrodmu,nrodsigma,count)

rd = symbols("Rods")

Ae(latex(rd)+" = random.normal(nrodmu, nrodsigma, count) \\\ = ["+
   str(round(nrod[0],6))+", "+str(round(nrod[1],6))+" \\dots " +
   str(round(nrod[count-1],6))+"]. ")   #12

figure(num=1)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title(" Histogram of Rods for Cuttings")
ax.set_ylabel("Counts")
ax.set_xlabel("Bin")
#plot(domain array,range array,"color",lw=2)


# Plot a normalized histogram with 50 bins
h =hist(nrod, bins=25) # matplotlib version (plot)

savefig('Fig01')

GoodRod=[]

for i in nrod:
    if Ge(i,9) and Le(i,11):
        GoodRod.append(i)

ct = symbols("Cut_{event}")
nGoodRod=len(GoodRod)
nYield=nGoodRod/count
ncutmu=.5;ncutsigma=.1

At("Question: Given the specification of $\\pm 1$, how many are good and what is the \
   yield? \\\ \ \\\ \
   Answer: The number of good rods = "+str(nGoodRod)+", yield = "
   +str(round(nYield*100,4))+"\%. ")


Cf(title="Materials")
#End Slide 7


#Begin Slide 8



At("The histogram of (15) is shown in Figure 1.")
If("Fig01",width=.7,height=.5,caption="1. Histogram Rods Variation")

Cf(title="Material Yield")
#End Slide 8

#Begin Slide 9
Y=Normal("y", ncutmu, ncutsigma)
s1Y=simplify(density(Y))
s2Y=s1Y(z)
s3Y=s2Y.integrate(z)
Ce(f1,s1Y)   #13
Ce(f1z,s2Y)   #14
Ce(f2z,Integral(f1z,(z,zi,zf)))   #15
nCutCount=len(GoodRod)
nct=random.normal(ncutmu, ncutsigma, nCutCount)

Ae(latex(ct) +" = random.normal("+str(ncutmu)+", "+str(ncutsigma)+", "+
   str(nCutCount)+") =  \\newline  ["+ latex(nct[0])+", "+ latex(nct[1])+", "+
   "\\dots \\\ "+ latex(nct[nCutCount-1])+"] ") #16)

figure(num=2)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title(" Histogram Halves Cuttings ")
ax.set_ylabel("Counts")
ax.set_xlabel("Bin")
#plot(domain array,range array,"color",lw=2)


# Plot a normalized histogram with 50 bins
h2 =hist(nct, bins=25) # matplotlib version (plot)
savefig('Fig02')
Cf(title="Equipment")
#End Slide 9

#Begin Slide 10
At("The histogram of (19) is shown in Figure 2.")
If("Fig02",width=1,height=.7,caption="2. Histogram of Cutter Variation")
Cf(title="Equipment Variable Histogram")
#End Slide 10


#Begin Slide 11

At("Method 1\\\ \ \\\ \
    From an end point the cutter is placed 5m away. The rod is placed against \
    that end point.\\\ \ \\\ \
    Method 2 \\\ \ \\\ \
    The cutter is located at the center of two end points. The rod is placed \
    between the end ponts. The end points are moved to hold the rod at the \
    center of the cutter. \\\ \ \\\ \
    Question: Determine the formula for each and justify it.")

Cf(title="Method")
#End Slide 11


#Begin Slide 12
At("Answers: \\\ \ \\\  1. The cutter with variation, i.e., $0.5 \\pm .1$  is \
   multiplied by the perfect dimension of rod that is 10. Why perfect 10? \
   Then the answer is substracted from a rod with variation. The two answers \
   are the cut products. \\\ \ \\\ \
   2. The rod with variation, i.e., $ 10 \\pm 1$ is multiplied by the \
   cutter with variation, i.e., $0.5 \\pm .1$. The answer is substracted from \
   the rod with variation. The two cuts are products. \\\ ")

Cf(title="Method Variable")
#End Slide 12


#Begin Slide 13

count2=len(nct)
HalfRod1=[]
HalfRod2=[]
for i in range(count2):
    m1=10*nct[i]
    HalfRod1.append(m1);HalfRod1.append(nrod[i]-m1)
    m2=nrod[i]*nct[i]
    HalfRod2.append(m2);HalfRod2.append(nrod[i]-m2)

figure(num=3)
subplot(2,1,1)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title(" Histogram Halves Cut by Method 1 ")
ax.set_ylabel("Counts")
ax.set_xlabel("Bin")
#plot(domain array,range array,"color",lw=2)


# Plot a normalized histogram with 50 bins
hm1 =hist(HalfRod1, bins=25) # matplotlib version (plot)

subplot(2,1,2)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title(" Histogram Halves Cut by Method 2 ")
ax.set_ylabel("Counts")
ax.set_xlabel("Bin")
#plot(domain array,range array,"color",lw=2)


# Plot a normalized histogram with 50 bins
hm2 =hist(HalfRod2, bins=25) # matplotlib version (plot)
savefig('Fig03')
At("The histograms of Method 1 and 2 are shown in Figure 3.")
If("Fig03",width=1,height=.7,caption="3. Histogram of Cut Rods")

Cf(title="Method Histogram")
#End Slide 13


#Begin Slide 14


At("Question: \\\ \ \\\ \
   Assuming that the cut specification is $5 \\pm .5$, \
   determine the number of good cut and the yield for each method \\\ \ \\\ ")

cm1=[]
cm2=[]
count3=count2*2
for i in range(count3):
    if Ge(HalfRod1[i],4.5) and Le(HalfRod1[i],5.5):
        cm1.append(HalfRod1[i])
    if Ge(HalfRod2[i],4.5) and Le(HalfRod2[i],5.5):
        cm2.append(HalfRod2[i])

ym1=round(len(cm1)*100/count3,4)
ym2=round(len(cm2)*100/count3,4)

At("Answer: \\\ \ \\\ 1. The number of good cut for method 1 is "+
    Lx(len(cm1))+" while for method 2 "+
    Lx(len(cm2)) + " respectively. \\\ \ \\\ ")
nOPsigma=.1; nOPmu=.4
nOP = random.normal(nOPmu,nOPsigma,len(GoodRod))
At("2. The yield for method 1 is "+Lx(ym1)+"\% while for method 2 is " +
   Lx(ym2)+"\% respectively. Why is it method 2 has higher yield? \\\ \ \\\ \
   \\subsection{Operator} ")

Cf(title="Method Yield")
#End Slide 14




#Begin Slide 15


OPHalfRod1=[]
OPHalfRod2=[]
for i in range(len(nOP)):
    OPHalfRod1.append(HalfRod1[i]-nOP[i])
    OPHalfRod1.append(HalfRod1[i+1]+nOP[i])
    OPHalfRod2.append(HalfRod2[i]-nOP[i])
    OPHalfRod2.append(HalfRod2[i+1]+nOP[i])

figure(num=4)
subplot(2,1,1)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title(" Histogram Halves Cut by Method 1 ")
ax.set_ylabel("Counts")
ax.set_xlabel("Bin")
#plot(domain array,range array,"color",lw=2)


# Plot a normalized histogram with 50 bins
hOP1 =hist(OPHalfRod1, bins=25) # matplotlib version (plot)

subplot(2,1,2)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title(" Histogram Halves Cut by Method 2 ")
ax.set_ylabel("Counts")
ax.set_xlabel("Bin")
#plot(domain array,range array,"color",lw=2)


# Plot a normalized histogram with 50 bins
hOP2 =hist(OPHalfRod2, bins=25) # matplotlib version (plot)
savefig('Fig04')


l1=len(OPHalfRod1)
l2=len(OPHalfRod2)

cOPm1=[]
cOPm2=[]
for i in range(l1):
    if Ge(OPHalfRod1[i],4.5) and Le(OPHalfRod1[i],5.5):
        cOPm1.append(OPHalfRod1[i])
for i in range(l2):
    if Ge(OPHalfRod2[i],4.5) and Le(OPHalfRod2[i],5.5):
        cOPm2.append(OPHalfRod2[i])

yOPm1=round(len(cOPm1)*100/l1)
yOPm2=round(len(cOPm2)*100/l2)

At("Assume and operator makes the loading with error of "+Lx(Eq(mu,nOPmu))+
   " and "+Lx(Eq(sigma,nOPsigma))+". \\\ \ \\\ \ The histograms with operator \
   handling for Method 1 and 2 are shown in Figure 4. \\\ \ \\\ \
   The yield with operator's handling errors for method 1 is "+Lx(yOPm1)+
   "\% while for method 2 is " + Lx(yOPm2)+"\% respectively.")


Cf(title="Operator Handling")
#End Slide 15




#Begin Slide 16

If("Fig04",width=1,height=.6,caption="4. Histogram of Cut Rods with \
   Operator's Handling")


Cf(title="Operator Handling Impact")
#End Slide 16



#Begin Slide 17

At("$\\bullet$Material mitigated by tighter tolerance with increased cost \\\ \ \\\ \
    $\\bullet$Machine mitigated by maintenance and continuous improvements \\\ \ \\\ \
    $\\bullet$Method generally difficult to observe and isolate and modelled,  \\\ \ \\\ \
    $\\bullet$Man mitigated by error proofing or Poka Yoke.")


Cf(title="Discussion on Sources of Variation")
#End Slide 17



#Begin Slide 18

At("$\\bullet$Consider a unit circle where an equilateral triangle is inscribed as \
    shown in Figure 5. \\\ \ \\\ \
    $\\bullet$ Suppose a random line is to be drawn across it, \
    determine the probability that the cord is less than the length of the \
    the side of equilateral triangle. \\\ ")
Cf(title="Random Variable Models")
#End Slide 18





#Begin Slide 19
theta=linspace(0,2*np.pi,100)
x=np.cos(theta);y=np.sin(theta)
lx=[cos(np.pi/2),
    cos(np.pi/2+2*np.pi/3),
    cos(np.pi/2+4*np.pi/3),
    cos(np.pi/2)]
ly=[sin(np.pi/2),
    sin(np.pi/2+2*np.pi/3),
    sin(np.pi/2+4*np.pi/3),
    sin(np.pi/2)]

r1x=[0,cos(np.pi/2+np.pi/3)]
r1y=[0,sin(np.pi/2+np.pi/3)]

r2x=[0,cos(np.pi/2+np.pi)]
r2y=[0,sin(np.pi/2+np.pi)]


r3x=[0,cos(np.pi/2+5*np.pi/3)]
r3y=[0,sin(np.pi/2+5*np.pi/3)]


figure(num=5)
#subplot(2,1,1)
subplots_adjust(hspace=1)
#subplot(row,column,plot number)
ax=gca();cla()
#axis([0,20,-0.05,0.15])
ax.set_title("The Unit Circle ")
ax.set_ylabel("y")
ax.set_xlabel("x")
#plot(domain array,range array,"color",lw=2)

plot(x,y,color="b")
plot(lx,ly)
plot(r1x,r1y,color="g")
plot(r2x,r2y,color="g")
plot(r3x,r3y,color="g")
plot(x/2,y/2,color="r")

savefig('Fig05')
If("Fig05",width=1,height=.7,caption="5. Equilateral Triangle Inscribe in \
    Unit Circle")
Cf(title="Random Lines Across a Circle")
#End Slide 19




#Begin Slide 20
At( "There are a number of answer depending \
   on how the random lines are drawn. \\\ \
   1. The line drawn from any two points at the circumference, gives the \
   probability of $\\frac{1}{3}$. \\\ \
   2. The line drawn perpendicular to radius from a any point along radius gives the \
   probability of $\\frac{1}{2}$ \\\ \
   3. The line drawn tangent to any concentric circle gives the probabiity \
   $\\frac{1}{4}$. \\\ \
   4. From the length of the cord i.e. $0$ to $2$, the probability is \
   $\\frac{\\sqrt{3}}{2}$. \\\ \ \\\ \
   The question is that which of the four probability numbers make sense? \
   In all these methods, does rotation of line matters?")

Cf(title="Matter of Method")
#End Slide 20


#Begin Slide 21

At("$\\bullet$The random variable in matter of two points at the circumference is the \
   arc of the circle. \\\ \ \\\ \
   $\\bullet$The random variable for line drawn perpendiculare to the radius is the \
   distance of the point where line intersects with radius from the center of the circule. \
   \\\ \ \\\ \
   $\\bullet$The random variable for the line tangent to the concentric circle is the \
   area of the concentric circle. \\\ \ \\\ \
   $\\bullet$The random variable for the length of the cord is the cord itself. \\\ \
   -All the lines segmented by perimeter of the circle are cords. Why is it that \
   are the probabilities of the lines above are different from the last?")

Cf(title="Matter of Random Variables")
#End Slide 21



#Begin Slide 22

At("Given a set of wirebonders bonding a particular producted, must all the set up \
    be identical exactly? \\\ \ \\\ \
    Generally no however the ranges of parameters must be identical. It means \
    each machine is different and the parameters are used to nullify the \
    differences. \\\ \ \\\ \
    The question is that what are the variables to be considered random? \
    These variables are not readily observable and measurable. These manifest \
    at region of ignorance where it is bounded by upper and lower control \
    limits of SPC charts")


Cf(title="Sample Problems")
#End Slide 22



#Begin Slide 22

At("There are a number of innovation opportunities that may be derived. \\\ \ \\\ \
    $\\bullet$ Make the intermittent or not readily observable phenomenon \
    consistently observable \\\ \ \\\ \
    $\\bullet$ What is made consistently observable may not be readily measurable. \
    Therefore make it readily measurable. \\\ \ \\\ \
    $\\bullet$ The region of ignorance in SPC charts provides the leading clues \
    for such phenomenon.")


Cf(title="Conclusion")
#End Slide 22

#Begin Slide 23

At("Maraming Salamat Po.")

Cf(title="End of Presentation")
#End Slide 23


Pb(Filename="MCBeamer.tex")
