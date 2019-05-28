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
Symposium="$29^{th}$ ASEMEP National Technical Symposium"
title="An Introduction to Process Variability Simulation"
author_data=[["Celso Bation Co ",
              "Research and Development Office",
              "Technological Institute of the Philippines",
              "Quezon City, Philippines",
              "celso.co@tip.edu.ph"]]

thanks_data=[["Technological Institute of the Philippines"]]
#End To be filled by the user


thanks=""
for i in thanks_data:
    thanks+="\\IEEEcompsocthanksitem "+str(i[0])+"\n"

authors=""
for i in range(len(author_data)):
    temp=author_data[i][0]+"\\\ \n " +author_data[i][1]+"\\\ "+\
         author_data[i][2]+"\\\ "+author_data[i][3]+"\\\ "+author_data[i][4]+"\\\ "
    authors+=temp
authors+="\ \n"

#\\documentclass[10pt,a4paper]{article}\n\

PyArt=PyArticle(Headers=\
"\\documentclass[10pt,journal,compsoc]{IEEEtran}\
 \\ifCLASSOPTIONcompsoc\n\
 \\usepackage[nocompress]{cite}\n\
 \\else\n\
  \\usepackage{cite}\
 \\fi\n\
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
 \\begin{document} \n\
 \\title{"+title+"}\
 \\author{"+authors+"\
 \\IEEEcompsocitemizethanks{"+thanks+"}\
 \\thanks{Manuscript received March 18, 2019}}\n\
 \\maketitle\n\
 \markboth{"+Symposium+"}%\n\
    {Shell \MakeLowercase{\textit{et al.}}: Bare Advanced Demo of \
    IEEEtran.cls for IEEE Computer Society Journals}")

          
             
#Shortcut Handlers 

At=PyArt.Append_Text            #Append Frame variable
Ae=PyArt.Append_Expression      #Short cut for Atf(Ae(s,n='',c-''))
Ce=PyArt.Append_Equation        #Short cut for At(Ae(Eq(left,right),n="",c=""))
Pb=PyArt.Build                        #Build Latex File
Lx=PyArt.Adjust_Latex                 #Convert text to Latex with adjustment
If=PyArt.Insert_Figure                       #Insert figure
eQ=PyArt.eQ                           #Equation List
Se=PyArt.Split_Expression             #Split the varialbe into n segments for display




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
 
 #End to be filled by user

At("\\begin{abstract}"+Abstract+"\\end{abstract}")  


#Begin to be filled by user

#Keywords
Keywords=\
   "variability, Normal Distribution, Gausian, Man, Machine, Method, Material, \
    4Ms."
#End to be filled by user

At("\\begin{IEEEkeywords}"+Keywords+"\\end{IEEEkeywords}")



#1 Introduction
At("\\section{Introduction}")

#Begin to be filled by user
 
from ccoLatex import *  #This is the library for Python-Tex coding.
from sympy.stats import Normal, density, E, std, cdf, skewness
from sympy import Symbol, simplify, pprint, factor, together, factor_terms, symbols

f, x, sigma, mu, fx = symbols("f x \\sigma \\mu f(x)")

At("The Monte Carlo Simulation requires the generation of random variable of \
    which statistical distribution follows a certain distribution.  In this \
    case, the normal or Gaussian distribution is used based on the assertion that a \
    stable process must obey central tendency theorem. \\\ \\\ \
    The Gaussian distribution function\\cite{20} is stated as follows.")

Ce(fx,1/(sigma*sqrt(2*pi))*exp(-(x-mu)**2/(2*sigma**2)).simplify())  #1

At("where :	\\\ \
$\\mu$    : Real number or a list representing the mean or the mean vector \\\ \
$\\sigma$ : Real number or a positive definite square matrix, \\\ "+
Lx(Gt(sigma**2, 0))+" the variance \\\ \
Returns: A Random Symbol. \\\ \\\ ")  

z, zi, zf, y, d, f1, f2, f3, p, X = symbols("z z_i z_f y density f1 f2 f3 p X")
f2x, f1z, f1x, f2z, f3z = symbols("f(x) f{_1}(z) f{_1}(x) f{_2}(z) f{_3}(z)")
from sympy.stats import Normal, density, E, std, cdf, skewness
from sympy import Symbol, simplify, pprint, factor, together, factor_terms


X = Normal("x", mu, sigma)
sf1=simplify(density(X))
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

At("Let "+Lx(Eq(mu,0))+" and "+Lx(Eq(sigma,1))+" then  "+Lx(f2)+
   " from "+Lx(Eq(zi,-oo))+" to "+Lx(Eq(zf,+oo))+" we have normal probability \
   distribution as follows.")
Ce(Eq(f2z,Integral(f1z,(z,-oo,oo))),
   sf2z.subs(zi,-oo).subs(zf,oo).subs(sigma,1).subs(mu,0))  #5

At("The " +Lx(f3z)+ " from "+Lx(Eq(zi,-1))+" to "+ Lx(Eq(zf,+1))+" implies \
   lower limit at "+Lx(-sigma )+" and upper limit "+Lx(+sigma)+". ")
Ce(Eq(Integral(f1z,(z,-1,1)),
      sf2z.subs(zi,-1).subs(zf,1).subs(sigma,1).subs(mu,0)),
      sf2z.subs(zi,-1).subs(zf,1).subs(sigma,1).subs(mu,0).evalf())  #6
At("At $\\pm $"+Lx(3*sigma)+", ")
Ce(Eq(Integral(f1z,(z,-3,3)),
      sf2z.subs(zi,-3).subs(zf,3).subs(sigma,1).subs(mu,0)),
      sf2z.subs(zi,-3).subs(zf,3).subs(sigma,1).subs(mu,0).evalf())  #7
At("Finally at $\\pm $"+Lx(6*sigma)+", ")
Ce(Eq(Integral(f1z,(z,-6,6)),
      sf2z.subs(zi,-6).subs(zf,6).subs(sigma,1).subs(mu,0)),
      sf2z.subs(zi,-6).subs(zf,6).subs(sigma,1).subs(mu,0).evalf())  #8
At("The defect per million DPM\\cite{21} of (6), (7), and (8) are given as follows.")
dpm, rd = symbols("DPM Rods")
Ce(dpm,(1-eQ[6].rhs)*1e6)    #9
Ce(dpm,(1-eQ[7].rhs)*1e6)    #10
Ce(dpm,(1-eQ[8].rhs)*1e6)    #11

#2 Review of Related Literature

At("\\section{Review of Related Literature } \
   The context of this tutorial on process variability is the statistical \
   process control (SPC)\\cite{23}. It is asserted that the stable process follows \
   the central limit theorem\\cite{22}. Hence, by making the upper control limit \
   and lower control limit of approaches a distant of $6 \\sigma$  from the mean \
   $\\mu$, the process is made extremely stable nd predictable. The discussion \
   would focus on the relationship of variables in processes to account for \
   relative impact of assignable causes\\cite{24}.\\\ \\\ ")

nrodmu=10
nrodsigma=1

#3 Simulation

At("\\section{Simulation} \
    Given a case where a 10m rod is to be cut into two halves where \
    the statistiscs of random variables are those of machine, man, material \
    and method, it is desired to find out how these affect the yield of the \
    process. The objective of the analysis to improve the accuracy that is \
    the distance of average from the desired mean and the precision that is \
    standard deviation or variance. \\\ \\\ " )

count=10000
At("\\subsection{Material}  A set of values of $z$ can be generated \
    randomly by the sympy function \\\ $Normal(\\mu, \\sigma)$. Given  "+
    Lx(Eq(mu,nrodmu))+" and "+ Lx(Eq(sigma,nrodsigma))+" then for "+str(count)+
    " pieces we have \\\ \\\ ")


nN=[]
dm=linspace(0,count,count)

# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2

nrod = random.normal(nrodmu,nrodsigma,count)


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
print("count = ", h[0],"  bin = ", h[1])
savefig('Fig01')
At("The histogram of (15) is shown in Figure 1.")
If("Fig01",width=1,height=.25,caption="1. Histogram Rods Variation")

At("Question: \\\ Given the specification of $\\pm 1$, how many are good and what is the \
   yield? \\\ ")


GoodRod=[]

for i in nrod:
    if Ge(i,9) and Le(i,11):
        GoodRod.append(i)

ct = symbols("Cut_{event}")
nGoodRod=len(GoodRod)
nYield=nGoodRod/count
ncutmu=.5;ncutsigma=.1

At("Answer number of good rods = "+str(nGoodRod)+", yield = "
   +str(round(nYield*100,4))+"\%. Note that everytime the program is run these \
   values changes. The solution was an algorithm to check dimension of each \
   rod and count those that are within tolerance. Solving it using (4) gives \
   a unique answer unlike the results from the algorithm above. Why?  "+
   " \\subsection{Equipment} \
   Now consider that these rods are to be cut into \
   halves. The cutter has "+Lx(Eq(mu,ncutmu))+" and "+
    Lx(Eq(sigma,ncutsigma))+" then for "+str(nGoodRod)+" pieces we have ")

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
At("The histogram of (19) is shown in Figure 2.")
If("Fig02",width=1,height=.25,caption="Histogram of Cutter Variation")

At("\\subsection{Method} \
   There two methods to cut the rod. One method is the cutter is place at  a \
   distance of half the rod size exactly 5. Then the rod is referenced at the \
   point of origin and cut is made.  The other method is to place the rod \
   at its center for cutter engagement. The formulas for the two methods are \
   different. \\\ \\\ Question: Determine the formula for each and justify it.")

At("\\\ Answers: \\\  1. The cutter with variation, i.e., $0.5 \\pm .1$  is \
   multiplied by the perfect dimension of rod that is 10. Why perfect 10? \
   Then the answer is substracted from a rod with variation. The two answers \
   are the cut products. \
   \\\ 2. The rod with variation, i.e., $ 10 \\pm 1$ is multiplied by the \
   cutter with variation, i.e., $0.5 \\pm .1$. The answer is substracted from \
   the rod with variation. The two cuts are products. \\\ ")


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
If("Fig03",width=1,height=.25,caption="Histogram of Cut Rods")


At("Question: \\\ Assuming that the cut specification is $5 \\pm .5$, determine the number \
   of good cut and the yield for each method \\\ ")

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

At("Answer: \\\ 1. The number of good cut for method 1 is "+Lx(len(cm1))+" while for method 2 "+
    Lx(len(cm2)) + " respectively. \\\ ")
nOPsigma=.1; nOPmu=.4
nOP = random.normal(nOPmu,nOPsigma,len(GoodRod))
At("2. The yield for method 1 is "+Lx(ym1)+"\% while for method 2 is " + 
   Lx(ym2)+"\% respectively. Why is it method 2 has higher yield? \\\ \\\ \
   \\subsection{Operator} \
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
If("Fig04",width=1,height=.25,caption="Histogram of Cut Rods with \
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

At("The yield with operator's handling errors for method 1 is "+Lx(yOPm1)+
   "\% while for method 2 is " + Lx(yOPm2)+"\% respectively.")

#4 Discussion

At("\\section{Discussion}"+
   "\\subsection{Tolerance Variation}"+
   "The yield numbers were exagerated for theoretical discussion. The four \
   variables are material, equipment or machine, method, and operator or man. \
   Hences, such sources of variations are known as 4M. \\\ \\\ \
   In real world, the overall yied is the only one observed and reported. It \
   problematict to account the yield loss for each source. However, the so-called \
   fool proofing refers to elimination of operator's mishandling. Tyically the \
   solution is jig and fixture. In this case, the positional fixture with \
   alignment jig could eliminate the operator's error. \\\ \\\ \
   The variation in machine could increase overtime. Hence, regular caligration \
   is necessary. To improve the variability, the continuous improvement \
   probram is the typical solution. \\\ \\\ \
   The material variation can be mitigated at a cost by simple requirement f0r \
   tighter tolerances. However, the most difficult variation to estimate is \
   the method. The difficulty was chosing the appropriate equation to define \
   the variability in a method. For instance, either of the two methods has \
   rejects of oversize.  It is possible to introduct rework or reprocess to \
   cut the oversize for yield recovery purposes. What are the appropriate \
   equations and the corresponding algorithm that can be concocted for each \
   method? If the target reference remains the mean, there is a chance that the \
   outcome is undersize. Should it the reference be at maximum tolerance? \
   In other words, the method for rework may not be the same as the standard \
   process. "+
   "\\subsection{Other Type of Variations}")


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
If("Fig05",width=1,height=.3,caption="Equilateral Triangle Inscribe in \
    Unit Circle")

At("Consider a unit circle where an equilateral triangle is inscribed as \
   shown in Figure 5. Suppose a random line is to be drawn across it, \
   determine the probability that the cord is less than the length of the \
   the side of equilateral triangle. There are a number of answer depending \
   on how the random lines are drawn. \\\ \
   1. The line drawn from any two points at the circumference, gives the \
   probability of $\\frac{1}{3}$. \\\ \
   2. The line drawn perpendicular to radius from a any point along radius gives the \
   probability of $\\frac{1}{2}$ \\\ \
   3. The line drawn tangent to any concentric circle gives the probabiity \
   $\\frac{1}{4}$. \\\ \
   4. From the length of the cord i.e. $0$ to $2$, the probability is \
   $\\frac{\\sqrt{3}}{2}$. \\\ \\\ \
   The question is that which of the four probability numbers make sense? ")

#5 Conclusion
At("\\section{Conclusion}"+
   "The variation of process variables can simulated by pseudo random generator. \
    The formula or equation associated with the algorithm must be ensured \
    realistically. From theoretical perspective the variance of every variable \
    can be determined but in real world operation, the net variance is the \
    only one that can be measured. Hence, the defect modes may be difficult \
    to itemize. \\\ \\\ \
    As discussed, the application of random variable depends on certain \
    perspective of variation. For instance, a short cord drawn near the center \
    of the circuit is not a line crossing the circle although it is random. \
    It hsd to be moved from the center to have its end points touch the \
    circumference. \\\ \\\ \
    Finally, the accuracy must be the difference between the average and the \
    specified mean must be approaching zero. The precission or repeatability \
    must be such that the tolerance is equal to a number of sixmas. ")

#6 Recommendation
At("\\section{Recommendation}"+
   "The Monte Carlo Simulation is useful for prediction of process yield. \
    Due care should be excercised in formulation of equation and algorthm. \
    The mathematics must be articulate the real world. There exists ample \
    room for creativity in defect modes itemization. The design of experiments \
    were used to optimize parameters. The Monte Carlo Simulation may help \
    to reduce number of experiments.")
    
show()

#7.0 References
At("\\bibliographystyle{plain} \n \\bibliography{MCIEEE}")

#9.0 About the Author
At("\\section*{About the Authors}")

#Begin to be filled by user

ABT=[
     {'ID'     :'cco.png',
      'Author' :'Celso Bation Co',
      'Account':'He earned his diploma as Electronic Technician from International \
       Correspondence Schools of University of Pennsylvania in 1972. He obtained \
       his degree of Bachelor of Science in Electronics and Communication \
       Engineering (ECE) from the University of Sto Tomas in 1977, Master  \
       and Doctoral degrees in ECE from De La Salle University in 1996 and \
       2007 respectively. \\\ '+
       'He is currently the research director of Technological Institute of the \
       Philippines and an advocate of strong linkages among academes, industries \
       and government institutions.'}]

def AbtItem(var):
    l=len(var)
    About=""
    for i in range(l):
        temp="\\begin{IEEEbiography}[{\\includegraphics[width=.75in,height=1in,clip, \
              keepaspectratio]{"+var[i]['ID']+"}}]{"+var[i]['Author']+"} "+\
              var[i]['Account']+"\\end{IEEEbiography}\ "
        About+=temp+"\ \\newline\n"      
    return About

At(AbtItem(ABT))


Pb(Filename="MCIEEE.tex")
