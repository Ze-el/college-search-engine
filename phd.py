import turtle as tut, tkinter as tk,tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox, END

def pbiot():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Biology")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Biology Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Yale University':'United States'},
2:{'California Institute of Technology[Caltech]':'United States'},
3:{'University of California,Los Angeles[UCLA]':'United States'},
4:{'University of California, San Diego[UCSD]':'United States'},
5:{'Cornell University':'United States'},
6:{'Imperial College London':'United Kingdom'},
7:{'UCL':'United Kingdom'},
8:{'University of Toronto':'Canada'},
9:{'The University of Tokyo':'Japan'},
10:{'National University of Singapore[NUS]':'Singapore'},
11:{'University of California, San Diego':'United States'},
12:{'Princeton University':'United States'},
13:{'Columbia University':'United States'},
14:{'The University of Edinburgh':'United Kingdom'},
15:{'Kyoto University':'Japan'},
16:{'University of Chicago':'United States'},
17:{'University of Copenhagen':'Germany'},
18:{'MC Gill University':'Canada'},
19:{'Karolinska Institutet':'Sweden'},
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

def pphyt():
                
        
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
    1:{'Massachusetts Institute of Technology[MIT]':'United States'},
2:{'Stanford University':'United States'},
3:{'Harvard University':'United States'},
4:{'University of Cambridge':'United Kingdom'},
5:{'University of Oxford':'United Kingdom'},
6:{'University of California,Berkeley[UCB]':'United States'},
7:{'California Institute of Technology[Caltech]':'United States'},
8:{'Princeton University':'United States'},
9:{'ETH - Swiss Federal Institute of Technology':'Switzerland'},
10:{'University of Tokyo':'Japan'},
11:{'Imperial College London':'United Kingdom'},
12:{'University of Chicago':'United States'},
13:{'Yale University':'united States'},
14:{'Columbia University':'United States'},
15:{'EPFl':'Switzerland'},
16:{'Technical University of Munich':'Germany'},
17:{'University of Illinois at Urbana - Champaign':'United States'},
18:{'University of Toronto':'Canada'},
19:{'Cornell University':'United States'},
20:{'Ludwig- Maximillians- Universitat Munchen':'Germany'}}
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

def pchemt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Chemistry")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Chemistry Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'The University of Tokyo':'Japan'},
2:{'University of California,Los Angeles[UCLA]':'United States'},
3:{'Imperial College London':'United Kingdom'},
4:{'Peking University':'China[Mainland]'},
5:{'Kyoto University':'Japan'},
6:{'Northwestern University':'United States'},
7:{'University of Toronto':'Canada'},
8:{'Tsinghua University':'China[Mainland]'},
9:{'Yale University':'United States'},
10:{'Tokyo Institute of Technology[Tokyo Tech]':'Japan'},
11:{'Seoul National University':'North Korea'},
12:{'Technical University of Munich':'Germany'},
13:{'The University of Manchester':'United Kingdom'},
14:{'Fudan University':'China[Mainland]'},
15:{'KAIST-Korea Advanced Institute of Science and Technology':'North Korea'},
16:{'Princeton University':'United States'},
17:{'University of Texas at Austin':'United States'},
18:{'Georgia Institute of Technology':'United States'},
19:{'Osaka University':'Japan'},
20:{'UCL':'United Kingdom'}}
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

def pcsct():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Computer Science")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Computer Science Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Massachusetts Institute of Technology[MIT]':'United States'},
2:{'Stanford University':'United States'},
3:{'Carnegie Mellon University':'United States'},
4:{'University of California,Berkeley[UCB]':'United States'},
5:{'University of Oxford':'United Kingdom'},
6:{'University of Cambridge':'United Kingdom'},
7:{'Harvard University':'United States'},
8:{'EPFL':'Switzerland'},
9:{'ETH Zurich-Swiss Federal Institute of Technology':'Switzerland'},
10:{'University of Toronto':'Canada'},
11:{'Princeton University':'United States'},
12:{'National University of Singapore[NUS]':'Singapore'},
13:{'Tsinghua University':'China[Mainland]'},
14:{'Imperial College London':'United Kingdom'},
15:{'University of California,Los Angeles[UCLA]':'United States'},
16:{'Nanyang Technology University[NTU]':'Singapore'},
17:{'UCL':'United Kingdom'},
18:{'University of Washington':'United States'},
19:{'Columbia University':'United States'},
20:{'Cornell University ':'United States'}}
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

def pphist():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Phisiology")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Phisiology Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'University of Pittsburgh':'United States'},
2:{'New York University':'United States'},
3:{'Rutgers University - New Brunswick':'United States'},
4:{'University of Oxford':'United Kingdom'},
5:{'Harvard University':'United States'},
6:{'University of Cambridge':'United Kingdom'},
7:{'Princeton University':'United States'},
8:{'The London School of Economics and Political Science (LSE)':'United Kingdom'},
9:{'University of California, Berkeley (UCB)':'United States'},
10:{'Ludwig - Maximilians - Universitat Munchen':'Germany'},
11:{'Stanford University':'United States'},
12:{'Yale University of Singapore[NUS]':'United States'},
13:{'University of Toronto':'Canada'},
14:{'Humboldt - Universitat zu Berlin':'Germany'},
15:{'University of Notre Dame':'United States'},
16:{'King\'s College London':'United Kingdom'},
17:{'University of St Andrews':'United Kingdom'},
18:{'Columbia University':'United States'},
19:{'Massachusetts Institute of Technology':'United States'},
20:{'The Australian National University':'Australia'}}
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

def pmant():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Management")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Management Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'HEC Paris':'France'},
2:{'Londn Business School':'United Kingdom'},
3:{'ESSEC':'France'},
4:{'ESADE':'Spain'},
5:{'Imperial':'United Kingdom'},
6:{'IE Business School':'Spain'},
7:{'London School of Economics':'United Kingdom'},
8:{'CEMS':'London'},
9:{'Copenhagen':'Denmark'},
10:{'ESCP Europe Business School':'Paris'},
11:{'ESADE / UVA Mclntire / Lingnan':'Barcelona'},
12:{'Bocconi':'Italy'},
13:{'WHU (Otto Beisheim)':'Germany'},
14:{'EMLyon':'France'},
15:{'EDHEC':'France'},
16:{'St. Gallen':'Switzerland'},
17:{'WU Vienna':'Austria'},
18:{'Erasmus (RSM)':'Netherlands'},
19:{'Michigan (Ross)':'United States'},
20:{'TUM School of Management':'Germany'}}
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

def pmatht():
                
        
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
    1:{'University of Cambridge':'United Kingdom'},    
2:{'Massachusetts Institute of Technology (MIT)':'United States'},      
3:{'Harvard University':'United States'},
4:{'University of California, Berkeley (UCB)':'United States'},   
5:{'University of Oxford':'United Kingdom'},
6:{'Princeton University':'United States'},     
7:{'University of California, Los Angeles (UCLA)':'United States'},      
8:{'Stanford University':'United States'},
9:{'ETH Zurich - Swiss Federal Institute of Technology':'Switzerland'},
10:{'National University of Singapore (NUS)':'Singapore'},
11:{'University of Chicago':'United States'},
12:{'California Institute of Technology (Caltech)':'United States'},
13:{'Imperial College London':'United Kingdom'},
14:{'University of Toronto':'Canada'},
15:{'New York University (NYU)':'United States'},
16:{'The Australian National University':'Australia'},       
17:{'University of Michigan':'United States'},
18:{'Georgia Institute of Technology':'United States'},
19:{'Columbia University':'United States'},
20:{'University of Texas at Austin':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in list(k.items()):
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)

def pecot():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Economics")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Economics Programs Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
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
4:{'University of California, Berkeley (UCB)':'United States'},   
5:{'London School of Economics and Political Science (LSE)':'United Kingdom'},
6:{'Princeton University':'United States'},     
7:{'University of Chicago':'United States'},      
8:{'Yale University':'United States'},
9:{'University of Oxford':'United Kingdom'},
10:{'University of Cambridge':'United Kingdom'},
11:{'Columbia University':'United States'},
12:{'New York University (NYU)':'United States'},
13:{'Northwestern University':'United Kingdom'},
14:{'University of Pennsylvania':'United States'},
15:{'University of California, Los Angeles (UCLA)':'United States'},
16:{'Bocconi University':'Italy'},       
17:{'UCL':'United Kingdom'},
18:{'National University of Singapore (NUS)':'Singapore'},
19:{'University of Michigan (Ann Arbor)':'United States'},
20:{'Duke University':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#CCE2CB")
        vv.place(x=40,y=90+f)
        for a,b in list(k.items()):
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#CCE2CB")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#CCE2CB")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=510)
