import turtle as tut, tkinter as tk,tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox, END

def gfint():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Finance")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Finance Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t     LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},
2:{'Massachusetts Institute of Technology[MIT]':'United States'},
3:{'Stanford University':'United States'},
4:{'The London School of Economics and Political Science[LSE]':'United Kingdom'},
5:{'University of Oxford':'United Kingdom'},
6:{'University of Cambridge':'United Kingdom'},
7:{'University of Pennsylvania':'United States'},
8:{'University of California[UCB]':'United States'},
9:{'University of Chicago':'United States'},
10:{'New York University[NYU]':'United States'},
11:{'London Business School':'United Kingdom'},
12:{'Columbia University':'United States'},
13:{'national University of Singapore[NUS]':'Singapore'},
14:{'Yale University':'United States'},
15:{'The University of New South Wales[UNSW Sydney]':'Australia'},
16:{'The University of Melbourne':'Australia'},
17:{'Bocconi University':'Italy'},
18:{'University of California,Los Angeles[UCLA]':'United States'},
19:{'HEC Paris School of Management':'France'},
20:{'Peking University':'China[Mainland]'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gcsct():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Computer Science")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Computer Science Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t     LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Carnegie Mellon University':'United States'},
2:{'University of California,Berkeley[UCB]':'United States'},
3:{'University of Oxford':'United Kingdom'},
4:{'University of Cambridge':'United Kingdom'},
5:{'Harvard University':'United States'},
6:{'EPFL':'Switzerland'},
7:{'ETH Zurich-Swiss Federal Institute of Technology':'Switzerland'},
8:{'University of Toronto':'Canada'},
9:{'Princeton University':'United States'},
10:{'Tsinghua University':'China[Mainland]'},
11:{'Imperial College London':'United Kingdom'},
12:{'University of California,Los Angeles[UCLA]':'United States'},
13:{'Nanyang Technology UNiversity,Singapore[NTU]':'Singapore'},
14:{'UCL':'United Kingdom'},
15:{'Cornell University':'United States'},
16:{'New York University[NYU]':'United States'},
17:{'Peking University':'China[Mainland]'},
18:{'University of Edinburgh':'United Kingdom'}, 
19:{'University of Waterloo':'Canada'},
20:{'University of British Columbia':'Canada'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gmarkt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Marketing")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Marketing Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t     LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'HEC Paris':'France'},
2:{'Imperial College':'United Kingdom'},
3:{'Columbia':'United States'},
4:{'Manchester[Alliance]':'United Kingdom'},
5:{'EMLyon':'France'},
6:{'ESCP Europe Business School':'London and Paris'},
7:{'ESADE':'Spain'},
8:{'Warwick Business School':'United Kingdom'},
9:{'EDHEC':'France'},
10:{'WU Vienna':'Austria'},
11:{'University of Edinburgh Business School':'United Kingdom'},
12:{'Vlerick Business School':'Belgium'},
13:{'SKEMA Business School':'France'},
14:{'USC[Marshall]':'United States'},
15:{'Texas[Mccombs]':'United States'},
16:{'Cranfield':'United Kingdom'},
17:{'Trinity BUsiness School':'Ireland'},
18:{'UCD[Smurfit]':'Ireland'},
19:{'Erasmus[RSM]':'Netherlands'},
20:{'IESEG':'France'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gbusit():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("business")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Business Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},
2:{'INSEAD':'France'},
3:{'London Business School':'United Kingdom'},
4:{'Massachusetts Institute of Technology(MIT)':'United States'},
5:{'Stanford University':'United States'},
6:{'University of Pennsylvania':'United States'},
7:{'Bocconi University':'Italy'},
8:{'University of Cambridge':'United Kingdom'},
9:{'HEC Paris School of Management':'France'},
10:{'The London School of Economics and Political Science(LSE)':'United Kingdom'},
11:{'University of Oxford':'United Kingdom'},
12:{'University of California,Berkeley(UCB)':'United States'},
13:{'National University of Singapore(NUS)':'Singapore'},
14:{'Northwestern University':'United States'},
15:{'Copenhagen Business School':'Denmark'},
16:{'The Hong Kong University of Science and Technology':'Hong Kong SAR'},
17:{'Erasmus University Rotterdam':'Netherlands'},
18:{'Columbia University':'United States'},
19:{'Yale University':'United States'},
20:{'New York University(NYU)':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gmatht():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Mathematics")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Mathematics Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Princeton University':'United States'},
2:{'ETH Zurich-Swiss Federal Institute of Technology':'Switzerland'},
3:{'New York University[NYU]':'United States'},
4:{'Imperial College London':'United Kingdom'},
5:{'Columbia University':'United States'},
6:{'National University of Singapore[NUS]':'Singapore'},
7:{'Universite PSL':'France'},
8:{'University of Toronto':'Canada'},
9:{'University of Chicago':'United States'},
10:{'California Institute of Technology[Caltech]':'United States'},
11:{'University of Michigan-Ann Arbor':'United States'},
12:{'University of Warwick':'United Kingdom'},
13:{'Tsinghua University':'China[Mainland]'},
14:{'Yale University':'United States'},
15:{'Peking University':'China[Mainland]'},
16:{'University of British Columbia':'Canada'},
17:{'EPFL':'Switzerland'},
18:{'The University of Tokyo':'Japan'},
19:{'Ecole Polytechnique':'France'},
20:{'The UNiversity of Melbourne ':'Australia'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def ginfot():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Information System")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Information System Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'University of Arizona':'Tucson'},
2:{'UA - Eller College of Management':'Tucson'},
3:{'The University of Texas at Austin':'Austin'},
4:{'Georgia State University':'Atlanta'},
5:{'Florida State University':'Tallahassee'},
6:{'The University of Texas at Dallas':'Richardson'},
7:{'Syracuse University':'Syracuse'},
8:{'Tsinghua University':'Beijing'},
9:{'Heinz College of Information System':'Pittsburgh'},
10:{'University of Oxford':'Oxford'},
11:{'Indiana University Bloomington':'Bloomington'},
12:{'Robert H. Smith School of Business':'College Park'},
13:{'University of Melbourne':'Melbourne'},
14:{'NYU Stern School of Business':'New York'},
15:{'McCombs School of Business':'Austin'},
16:{'Southern N.. Hampshire University':'Manchester'},
17:{'University of Southern California':'Los Angeles'},
18:{'Krannert School of Management':'West Lafay'},
19:{'Missouri University of Science and Technology':'Rolla'},
20:{'Mays Business School':'College Stations'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gphyt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Physics")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Physics Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Massachusetts Institute of Technology (MIT)':'United States'},
2:{'Harvard University':'United States'},
3:{'Stanford University':'United States'},
4:{'University of Cambridge':'United Kingdom'},
5:{'University of California, Berkeley (UCB)':'United States'},
6:{'University of Oxford':'United Kingdom'},
7:{'California Institute of Technology (Caltech)':'United States'},
8:{'Princeton University':'United States'},
9:{'ETH Zurich (Swiss Federal Institute of Technology)':'Switzerland'},
10:{'The University of Tokyo':'Japan'},
11:{'Imperial College London':'United Kingdom'},
12:{'EPFL':'Switzerland'},
13:{'University of California, Los Angeles (UCLA)':'United States'},
14:{'Columbia University':'United States'},
15:{'Yale University':'United States'},
16:{'Technical University of Munich':'Germany'},
17:{'University of Chicago':'United States'},
18:{'Tsinghua University':'China'},
19:{'Perking University of Science and Technology':'China'},
20:{'Ludwig - Maximilians - Universitat Munchen':'Germany'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gacct():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Accountancy")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Accountancy Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},  
2:{'Massachusetts Institute of Technology (MIT)':'United States'},   
3:{'Stanford University':'United States'},
4:{'The London School of Economics and Political Science (LSE)':'United Kingdom'},  
5:{'University of Oxford':'United Kingdom'},
6:{'University of Cambridge':'United Kingdom'},
7:{'University of Pennsylvania':'United States'},   
8:{'University of California,Berkeley(UCB)':'United States'}, 
9:{'University of Chicago':'United States'},
11:{'London Business School':'United Kingdom'},  
12:{'Columbia University':'United States'},
13:{'National University of Singapore (NUS)':'Singapore'},
14:{'Yale University':'United States'},
15:{'The University of New South Wales(UNSW Sydney)':'Australia'},  
16:{'The University of Melbourne':'Australia'},
17:{'Bocconi University':'Italy'},
18:{'University of California,Los Angeles(UCLA)':'United States'}, 
19:{'HEC Paris School of Management':'France'},
20:{'The Hong Kong University of Science and Technology':'Hong Kong SAR'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gstatt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Statistics")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Statistics Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'University of Oxford':'United Kingdom'},
2:{'California Institute of Technology':'United States'},
4:{'University of Cambridge':'United Kingdom'},
5:{'Stanford University':'United States'},
6:{'Massachusetts Institute of Technology':'United States'},
7:{'Princeton University':'United States'},
8:{'Harvard University':'United States'},
9:{'Yale University':'United States'},
10:{'The University of Chicago':'United States'},
11:{'Imperial College London':'United Kingdom'},
12:{'University of Pennsylvania':'United States'},
13:{'Johns Hopkins University':'United States'},
14:{'Duke University':'United States'},
15:{'ETH Zurich':'Switzerland'},
16:{'UCL':'United Kingdom'},
17:{'Columbia University':'United States'},
18:{'University of California,Los Angeles':'United States'},
19:{'University of Toronto':'Canada'},
20:{'Cornell University':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def gentt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Entrepreneurship")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Entrepreneurship Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Babson College':'Babson Park, MA'},
2:{'Stanford University':'Stanford, CA'},
3:{'Massachusetts Institute of Technology':'Cambridge, MA'},
4:{'University of California':'Berkeley, CA'},
5:{'Harvard University':'Boston, MA'},
6:{'University of Pennsylvania':'Philadelphia, PA'},
7:{'University of Michigan':'Ann Arbor, MI'},
8:{'Indiana University':'Bloomington, IN'},
9:{'University of Texas':'Austin, TX'},
10:{'Saint Louis University':'St. Louis, MO'},
11:{'Rice University':'Houston, TX'},
12:{'Loyola Marymount University':'Los Angeles, CA'},
13:{'University of Utah':'Salt Lake City, UT'},
14:{'Baylor University':'Waco, TX'},
15:{'Columbia University':'New York, NY'},
16:{'Cornell University':'Ithaca, NY'},
17:{'Georgetown University':'Washington, DC'},
18:{'Loyola University New Orleans':'New Orleans, LA'},
19:{'New York University':'New York, NY'},
20:{'Northwestern University':'Evanston, IL'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)
