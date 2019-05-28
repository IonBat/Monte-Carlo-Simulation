# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Library

from ccoLatex import *  #This is the library for Python-Tex coding.


from Figure import *


from sympy import Union, Intersection
        
#initialize the PyLx as class PyLatex

#Begin To be filled up by the user


title="Scratch Pad Fuzzy Set"
author="student"


HDRS="\\documentclass[10pt,a4paper]{article}\n\
\\newtheorem{theorem}{Theorem} \n\
\\newtheorem{lemma}{Lemma} \n\
\\newtheorem{proposition}{Proposition} \n\
\\newtheorem{proof}{Proof} \n\
\\newtheorem{definition}{Definition}\n\
\\usepackage[latin1]{inputenc}\n\
\\usepackage[T1]{fontenc}\n\
\\usepackage{amsmath}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{makeidx}\n\
\\usepackage{graphicx}\n\
\\usepackage{float}\n\
\\usepackage{ifpdf}\n\
\\ifpdf\n\
\\usepackage[breaklinks,hidelinks]{hyperref}\n\
\\else \n\
\\usepackage{url}\n\
\\fi\n\
\\author{"+author+"}\n\
\\title{"+title+"}\n\
\\begin{document}\n\
\\maketitle\n\n"

PyArt=PyArticle(Headers=HDRS)
                     
#Shortcut Handlers 

At=PyArt.Append_Text            #Append Frame variable
Ae=PyArt.Append_Expression      #Short cut for Atf(Ae(s,n='',c-''))
Ce=PyArt.Append_Equation        #Short cut for At(Ae(Eq(left,right),n="",c=""))
Pb=PyArt.Build                  #Build Latex File
Lx=PyArt.Adjust_Latex           #Convert text to Latex with adjustment
If=PyArt.Insert_Figure          #Insert figure
eQ=PyArt.eQ                     #Equation List
Se=PyArt.Split_Expression       #Split the varialbe into n segments for display

from ccoLatex import *  #This is the library for Python-Tex coding.

from sympy.stats import Normal, density, E, std, cdf, skewness
from sympy import Symbol, simplify, pprint, factor, together, factor_terms, symbols

f, x, sigma, mu = symbols("f x \\sigma \\mu")

At("sympy.stats.Normal(name, mean, std) \\\ \
Create a continuous random variable with a Normal distribution. \\\ \
The density of the Normal distribution is given by \
")

Ce(f(x),1/(sigma*sqrt(2*pi))*exp(-(x-mu)**2/(2*sigma**2)).simplify())  #1


At("Parameters:	\\\ \
mu    : Real number or a list representing the mean or the mean vector \\\ \
sigma : Real number or a positive definite sqaure matrix, \\\ "+
Lx(Gt(sigma**2, 0))+" the variance \\\ \
Returns: A Random Symbol.  \\\ \\\ \
References  \\\ \
$[R575]$	\\url{http://en.wikipedia.org/wiki/Normal_distribution}  \\\ \
$[R576]$	\\url{http://mathworld.wolfram.com/NormalDistributionFunction.html}")  

z, zi, zf, y, d, f1, f2, f3, p, X = symbols("z z_i z_f y density f1 f2 f3 p X")
from sympy.stats import Normal, density, E, std, cdf, skewness
from sympy import Symbol, simplify, pprint, factor, together, factor_terms


X = Normal("x", mu, sigma)
sf1=simplify(density(X))
At("The sympy function ")
Ce(f1,sf1)  #2
At("declares the Normal Distribution ")
sf2=sf1(z)
At("The following function specifies the random variable $z$")
Ce(Eq(f2,f1(z)),sf2)  #3
sf3=sf2.integrate((z,zi,zf))
Ce(Eq(f3,f2(z).integrate((z,zi,zf))),sf3)  #4
At("Let "+Lx(Eq(mu,0))+" and "+Lx(Eq(sigma,1))+" then ")
Ce(Eq(f3,f2(z).integrate((z,-oo,oo))),
   sf3.subs(zi,-oo).subs(zf,oo).subs(sigma,1).subs(mu,0))  #5

Ce(Eq(f2(z).integrate((z,-1,1)),
      sf3.subs(zi,-1).subs(zf,1).subs(sigma,1).subs(mu,0)),
      sf3.subs(zi,-1).subs(zf,1).subs(sigma,1).subs(mu,0).evalf())  #6

Ce(Eq(f2(z).integrate((z,-3,3)),
      sf3.subs(zi,-3).subs(zf,3).subs(sigma,1).subs(mu,0)),
      sf3.subs(zi,-3).subs(zf,3).subs(sigma,1).subs(mu,0).evalf())  #7

Ce(Eq(f2(z).integrate((z,-6,6)),
      sf3.subs(zi,-6).subs(zf,6).subs(sigma,1).subs(mu,0)),
      sf3.subs(zi,-6).subs(zf,6).subs(sigma,1).subs(mu,0).evalf())  #8

dpm, rd = symbols("DPM Rods")
Ce(dpm,(1-eQ[6].rhs)*1e6)    #9
Ce(dpm,(1-eQ[7].rhs)*1e6)    #10
Ce(dpm,(1-eQ[8].rhs)*1e6)    #11

nmu=5
nsigma=.5

At("A set of values of $z$ can be generated randomly by the sympy function \\\ \
    $Normal(\\mu, \\sigma)$. Given  "+Lx(Eq(mu,nmu))+" and "+
    Lx(Eq(sigma,nsigma))+" then ")
X=Normal("x", nmu, nsigma)

s1X=simplify(density(X))
s2X=s1X(z)
s3X=s2X.integrate((z,zi,zf))
Ce(f1,s1X)   #12
Ce(f2,s2X)   #13
Ae(latex(Eq(f3,f2(z).integrate((z,zi,zf))))+" = \\\ "+latex(s3X))   #14
count=10000
At("\\section{Material}  A set of values of $z$ can be generated \
    randomly by the sympy function \\\ $Normal(\\mu, \\sigma)$. Given  "+
    Lx(Eq(mu,nmu))+" and "+ Lx(Eq(sigma,nsigma))+" then for "+str(count)+
    " pieces we have \\\ \\\ ")


nN=[]
dm=linspace(0,count,count)

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
nmu, nsigma = 10, 0.5
nrod = random.normal(nmu,nsigma,10000)


Ae(latex(rd)+" = random.normal(nmu, nsigma, count) = "+str(nrod))   #15

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
print("count = ", h[0],"  bin = ", h[1])
savefig('Fig01')
At("The histogram of (15) is shown in Figure 1.")
If("Fig01",width=1,height=.25,caption="Histogram Rods Variation")

At("Given the specification of $\\pm 1$, how many are good and what is the \
   yield? ")


GoodRod=[]

for i in nrod:
    if Ge(i,9) and Le(i,11):
        GoodRod.append(i)

ct = symbols("Cut_{event}")
nsigma=.05; nmu=.5
nct = random.normal(nmu,nsigma,len(GoodRod))

nGoodRod=len(GoodRod)
nYield=nGoodRod/count

At("Answer number of good rods = "+str(nGoodRod)+", yield = "
   +str(round(nYield*100,4))+"\%. Note that everytime the program is run these \
   values changes. The solution used is to use an algorithm to check each \
   rod and count those that are within tolerance. Try solving it using (14) \
   and compare the results. \\\ \\\ \\section{Equipment} \
   Now consider that these rods are to be cut into \
   halves. The cutter has "+Lx(Eq(mu,nmu))+" and "+
    Lx(Eq(sigma,nsigma))+" then for "+str(nGoodRod)+" pieces we have \\\ \\\ ")


Y=Normal("y", nmu, nsigma)
s1Y=simplify(density(Y))
s2Y=s1Y(z)
s3Y=s2Y.integrate(z)
Ce(f1,s1Y)   #16
Ce(f2,s2Y)   #17
Ae(latex(Eq(f3,f2(z).integrate((z,zi,zf))))+" = \\\ "+latex(s3Y))   #18

Ae(latex(ct)+" = random.normal(nmu, nsigma, len(GoodRod)) = "+ str(nct)) #19


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
h2 =hist(GoodRod, bins=25) # matplotlib version (plot)
savefig('Fig02')
At("The histogram of (19) is shown in Figure 2.")
If("Fig02",width=1,height=.25,caption="Histogram of Cutter Variation")

At("\\section{Method} \
   There two methods to cut the rod. One method is the cutter is place at  a \
   distance of half the rod size exactly 5. Then the rod is referenced at the \
   point of origin and cut is made.  The other method is to place the rod \
   at its center for cutter engagement. The formulas for the two methods are \
   different. Determine the formula for each and justify it.")

At("\\\ \\\ Answers: \\\ 1. The cutter with variation, i.e., $5 \\pm .25$  is \
   multiplied by the perfect dimension of rod that is 10. Then the answer is \
   substracted from rod with variation. The two answer are the cut products. \
   \\\ 2. The rod with variation, i.e., $ 10 \\pm 1$ is multiplied by the \
   cutter with variation, i.e., $5 \\pm .25$. The answer is substracted from \
   the rod with variation. The cut producst are the two answers. \\\ \\\ \
   Determine the average and standard deviation of cut rods for each method \
   and compare them. What is your observation?")


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
If("Fig03",width=1,height=.5,caption="Histogram of Cut Rods")


At("Assuming that the cut specification is $5 \\pm .5$, determine the number \
   of good cut and the yield for each method")

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

At("The number of good cut for method 1 is "+Lx(len(cm1))+" while for method 2 "+
    Lx(len(cm2)) + " respectively.  ")
nOPsigma=.1; nOPmu=.4
nOP = random.normal(nOPmu,nOPsigma,len(GoodRod))
At("The yield for method 1 is "+Lx(ym1)+"\% while for method 2 is " + 
   Lx(ym2)+"\% respectively. Why is it method 2 has higher yield? \\\ \\\ \
   \\section{Operator} \
   Assume and operator makes the loading with error of "+Lx(Eq(mu,nOPmu))+" and "+
   Lx(Eq(sigma,nOPsigma))+". ")
    

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
At("The histograms with operator handling for Method 1 and 2 are shown in \
    Figure 4.")
If("Fig04",width=1,height=.5,caption="Histogram of Cut Rods with \
   Operator's Handling")




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

At("The yield for method 1 is "+Lx(yOPm1)+"\% while for method 2 is " + 
   Lx(yOPm2)+"\% respectively.")

show()



'''
Examples

Run code block in SymPy Live
>>> from sympy.stats import Normal, density, E, std, cdf, skewness
>>> from sympy import Symbol, simplify, pprint, factor, together, factor_terms
Run code block in SymPy Live
>>> mu = Symbol("mu")
>>> sigma = Symbol("sigma", positive=True)
>>> z = Symbol("z")
>>> y = Symbol("y")
>>> X = Normal("x", mu, sigma)
Run code block in SymPy Live
>>> density(X)(z)
sqrt(2)*exp(-(-mu + z)**2/(2*sigma**2))/(2*sqrt(pi)*sigma)
Run code block in SymPy Live
>>> C = simplify(cdf(X))(z) # it needs a little more help...
>>> pprint(C, use_unicode=False)
   /  ___          \
   |\/ 2 *(-mu + z)|
erf|---------------|
   \    2*sigma    /   1
-------------------- + -
         2             2
Run code block in SymPy Live
>>> simplify(skewness(X))
0
Run code block in SymPy Live
>>> X = Normal("x", 0, 1) # Mean 0, standard deviation 1
>>> density(X)(z)
sqrt(2)*exp(-z**2/2)/(2*sqrt(pi))
Run code block in SymPy Live
>>> E(2*X + 1)
1
Run code block in SymPy Live
>>> simplify(std(2*X + 1))
2
Run code block in SymPy Live
>>> m = Normal('X', [1, 2], [[2, 1], [1, 2]])
>>> from sympy.stats.joint_rv import marginal_distribution
>>> pprint(density(m)(y, z))
       /  y   1\ /2*y   z\   /  z    \ /  y   2*z    \
       |- - + -|*|--- - -| + |- - + 1|*|- - + --- - 1|
  ___  \  2   2/ \ 3    3/   \  2    / \  3    3     /
\/ 3 *e
------------------------------------------------------
                         6*pi
Run code block in SymPy Live
>>> marginal_distribution(m, m[0])(1)
 1/(2*sqrt(pi))
 
'''
Pb(Filename="MC01.tex")
