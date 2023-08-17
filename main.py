import turtle as tut, tkinter as tk,tkinter.font as font
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox

def agpa():
    def calc():
        a,b,c,d,e=name.get(),namet.get(),col.get(),colt.get(),sat.get()
        f=(int(a)+int(b)+int(c)+int(d)+int(e))/5
        gpa=(f/100)*4
        messagebox.showinfo("GPA", "Your GPA on 4.0 scale is :\n"+str(gpa))
    ugcomp=tk.Toplevel()
    ugcomp.title("Calculate GPA")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("700x270")
    namelab=tk.Label(ugcomp,text='Calculate your GPA for college :',font=("Courier",13,'bold'),bg="#CCE2CB")
    namelab.place(x=140,y=20)
    namelab=tk.Label(ugcomp,text='Enter Percentage of Subject 1 (out of 100):',font=("Courier",12),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    name=tk.Entry(ugcomp)
    name.place(x=480,y=70)
    namelabt=tk.Label(ugcomp,text='Enter Percentage of Subject 2 (out of 100):',font=("Courier",12),bg="#CCE2CB")
    namelabt.place(x=20,y=100)
    namet=tk.Entry(ugcomp)
    namet.place(x=480,y=100)
    collab=tk.Label(ugcomp,text='Enter Percentage of Subject 3 (out of 100):',font=("Courier",12),bg="#CCE2CB")
    collab.place(x=20,y=130)
    col=tk.Entry(ugcomp)
    col.place(x=480,y=130)
    collabt=tk.Label(ugcomp,text='Enter Percentage of Subject 4 (out of 100):',font=("Courier",12),bg="#CCE2CB")
    collabt.place(x=20,y=160)
    colt=tk.Entry(ugcomp)
    colt.place(x=480,y=160)
    satlab=tk.Label(ugcomp,text='Enter Percentage of Subject 5 (out of 100):',font=("Courier",12),bg="#CCE2CB")
    satlab.place(x=20,y=190)
    sat=tk.Entry(ugcomp)
    sat.place(x=485,y=190)
    cont = tk.Button(ugcomp, text="Calculate", font=("Courier",10), bg="#FFFFFF",command=calc)
    cont.place(x=20, y=230)
    ugcomp.mainloop()

def inp():
    def apply():
        a=sat.get()
        b=act.get()
        def les():
            messagebox.showinfo("Can not apply", "We are really sorry to inform you\nthat your SAT and ACT scores are not upto the mark")
        def ok():
            messagebox.showinfo("Congratulations", "We are really pleased to inform you\nthat your application has been sent to the college.")
        def er():
            messagebox.showinfo("Error", "Error !\nYou have left a field empty.")
        
        if a=='' or b=='' or name.get()=='' or namet.get()=='' or col.get()=='' or colt.get()=='':
            er()
        elif int(a)<1100 or int(b)<25:
            les()
        else:
            ok()
    ugcomp=tk.Toplevel()
    ugcomp.title("Apply for colleges")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("600x320")
    namelab=tk.Label(ugcomp,text='Apply for Your College Here',font=("Courier",13,'bold'),bg="#FCDFFF")
    namelab.place(x=140,y=20)
    namelabt=tk.Label(ugcomp,text='Enter Your First Name :',font=("Courier",12),bg="#FCDFFF")
    namelabt.place(x=20,y=50)
    name=tk.Entry(ugcomp)
    name.place(x=270,y=50)
    namelaba=tk.Label(ugcomp,text='Enter Your Last Name :',font=("Courier",12),bg="#FCDFFF")
    namelaba.place(x=20,y=80)
    namet=tk.Entry(ugcomp)
    namet.place(x=250,y=80)
    collab=tk.Label(ugcomp,text='Enter College you want to apply :',font=("Courier",12),bg="#FCDFFF")
    collab.place(x=20,y=110)
    col=tk.Entry(ugcomp)
    col.place(x=400,y=110)
    collabt=tk.Label(ugcomp,text='Enter the Course you want to apply for :',font=("Courier",12),bg="#FCDFFF")
    collabt.place(x=20,y=140)
    colt=tk.Entry(ugcomp)
    colt.place(x=450,y=140)
    satlab=tk.Label(ugcomp,text='Enter your SAT Score :',font=("Courier",12),bg="#FCDFFF")
    satlab.place(x=20,y=170)
    sat=tk.Entry(ugcomp)
    sat.place(x=245,y=170)
    actlab=tk.Label(ugcomp,text='Enter your ACT Score :',font=("Courier",12),bg="#FCDFFF")
    actlab.place(x=20,y=200)
    act=tk.Entry(ugcomp)
    act.place(x=245,y=200)
    actlab=tk.Label(ugcomp,text='Enter your GPA Score (4.0 points):',font=("Courier",12),bg="#FCDFFF")
    actlab.place(x=20,y=230)
    act=tk.Entry(ugcomp)
    act.place(x=370,y=230)
    cont = tk.Button(ugcomp, text="Apply", font=("Courier",10), bg="#FFFFFF",command=apply)
    cont.place(x=20, y=270)
    ugcomp.mainloop()

def pbiot():        
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Biology")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Biology Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pphyt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Physics")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Physics Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pchemt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Chemistry")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Chemistry Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pcsct():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Computer Science")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Computer Science Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pphist():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Phisiology")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Phisiology Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pmant():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Management")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Management Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pmatht():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Mathematics")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Mathematics Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in list(k.items()):
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

def pecot():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Economics")
    ugcomp.configure(bg="#FBF6D9")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Economics Programs Are Listed Below .',font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FBF6D9")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
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
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FBF6D9")
        vv.place(x=40,y=90+f)
        for a,b in list(k.items()):
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FBF6D9")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FBF6D9")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FBF6D9")
    namelab.place(x=20,y=510)

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

def ugcsct():
    ugcomp=tk.Toplevel()
    ugcomp.title("Computer Science")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Computer Science Programs Are Listed Below .',font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Massachusetts Institute of Technology (MIT)':'United States'},
    2:{'Stanford University':'United States'},
    3:{'Carnegie Mellon University':'United States'},
    4:{'University of California, Berkeley (UCB)':'United States'},
    5:{'University of Oxford':'United Kingdom'},
    6:{'University of Cambridge':'United Kingdom'},
    7:{'Harvard University':'United States'},
    8:{'EPFL':'Switzerland'},
    9:{'ETH Zurich - Swiss Federal Institute of Technology':'Switzerland'},	
    10:{'University of Toronto':'Canada\t'},		
    11:{'Princeton University':'United States'},		
    12:{'National University of Singapore (NUS)':'Singapore'},	
    13:{'Tsinghua University':'China\t'},
    14:{'Imperial College London':'United Kingdom'},		
    15:{'University of California, Los Angeles (UCLA)':'United States'},
    16:{'Nanyang Technological University, Singapore (NTU)':'Singapore'},
    17:{'UCL':'United Kingdom'},
    18:{'University of Washington':'United States'},
    19:{'Columbia University':'United States'},
    20:{'Cornell University':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugcomt():
    
    ugcomp=tk.Toplevel()
    ugcomp.title("Communications")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Communications Program Are Listed Below .',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'University of Amsterdam':'Netherlands'},
            2:{'University of Southern California':'United States'},
            3:{'Stanford University':'United Kingdom'},
            4:{'University of Texas at Austin':'United States'},
            5:{'University of Pennsylvania':'United States'},
            6:{'Nanyang Technology University,Singapore[NTU]':'Singapore'},
            7:{'University of California,Berkeley[UCB]':'United States'},
            8:{'New York University[NYU]':'United States'},
            9:{'University of Wisconsin-Madison':'United States'},
            10:{'National University of Singapore[NUS]':'Singapore'},
            11:{'University of California,Los Angeles[UCLA]':'United States'},
            12:{'COlumbia University':'United States'},
            13:{'The Chinese University of Hong Kong[CUHK]':'Hong Kong SAR'},
            14:{'Michigan State University':'United States'},
            15:{'Queensland University of Technology[QUT]':'Australia'},
            16:{'University of Zurich':'Switzerland'},
            17:{'Northwestern University':'United States'},
            18:{'University of Michigan-Ann Arbor':'United States'},
            19:{'The University of Sydney':'Australia'},
            20:{'University of California,Santa Barbara[UCSB]':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugpoliscit():
    ugcomp=tk.Toplevel()
    ugcomp.title("Government / Political Science")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Government / Political Science Program Are Listed Below .',font=("Courier",12),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},
            2:{'Sciences Po':'France\t'},
            3:{'University of Kingdom':'United Kingdom'},
            4:{'The London School of Economics and Political Science[LSE]':'United Kingdom'},
            5:{'University of Cambridge':'United Kingdom'},
            6:{'Stanford University':'United States'},
            7:{'The Australian National University':'Australia'},
            8:{'Yale University':'United States'},
            9:{'University of California,Berkeley[UCB]':'United States'},
            10:{'Columbia University':'United States'},
            11:{'Georgetown University':'United States'},
            12:{'National University of Singapore[NUS]':'Singaore\t'},
            13:{'Uiversity of California,San Diego[UCSD]':'United States'},
            14:{'Kings College London':'United Kingdom'},
            15:{'University of California,Los Angeles[UCLA]':'United States'},
            16:{'University of Chicago':'United States'},
            17:{'SOAS University of London':'United Kingdom'},
            18:{'Freie Universitaet Berlin':'Germany\t'},
            19:{'University of Toronto':'Canada\t'},
            20:{'The University of Tokyo':'Japan\t'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugbust():
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Business")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Business Program Are Listed Below .',font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},
            2:{'INSEAD':'France\t'},
            3:{'London Business School':'United KIngdom'},
            4:{'Massachusetts Institute of Technology':'United States'},
            5:{'University of Pennsylvania':'United States'},
            6:{'Bocconi University':'Italy\t'},
            7:{'University of Cambridge':'United Kingdom'},
            8:{'HEC Paris School of Management':'France\t'},
            9:{'University of Oxford':'United Kingdom'},
            10:{'University of California,Berkeley[UCB]':'United States'},
            11:{'National University of Singapore[NUS]':'Singapore'},
            12:{'Northwestern University':'United States'},
            13:{'Copenhagen Business School':'Denmark\t'},
            14:{'The HongKong University of Science and Technology':'HongKong SAR'},
            15:{'Erasmus University Rotterdam':'NEtherlands'},
            16:{'Columbia University':'United States'},
            17:{'Yale University':'United States'},
            18:{'New York University':'United States'},
            19:{'Universitat Ramon Llull':'Spain\t'},
            20:{'University of Chicago':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugecot():   
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Economics")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Economics Program Are Listed Below .',font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'Cambridge (U.S.)'},
    2:{'Massachusetts Institute of Technology':'Cambridge (U.S.)'},
    3:{'University of California':'Berkeley (U.S.)'},
    4:{'Stanford University':'Stanford (U.S.)'},
    5:{'University of Pennsylvania':'Philadelphia (U.S.)'},
    6:{'University of Chicago':'Chicago (U.S.)'},
    7:{'London School of Economics and Political Science':'London (U.K.)'},
    8:{'Columbia University':'New York City (U.S.)'},
    9:{'New York University':'New York City (U.S.)'},
    10:{'University of Michigan':'Ann Arbor (U.S.)'},
    11:{'Erasmus University Rotterdam':'Netherlands'},
    12:{'Yale University':'New Haven (U.S.)'},
    13:{'Northwestern University':'Evanston (U.S.)'},
    14:{'University of Oxford':'Oxford (U.K.)'},
    15:{'National University of Singapore':'Singapore'},
    16:{'Princeton University':'Princeton (U.S.)'},
    17:{'University of Cambridge':'Cambridge (U.K.)'},
    18:{'Bocconi University':'Italy'},
    19:{'Duke University':'Durham (North Carolina, U.S.)'},
    20:{'Tilburg University':'Netherlands'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugengt():
        
    ugcomp=tk.Toplevel()
    ugcomp.title("English Language and Literature")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For English Language and Literature Program Are Listed Below .',font=("Courier",11),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'University of Oxford':'United Kingdom'},     
    2:{'University of Cambridge':'United Kingdom'},      
    3:{'Harvard University':'United States'}, 
    4:{'University of California':'Berkeley (U.S.)'},
    5:{'Stanford University':'United States'},
    6:{'Yale University':'United States'},  
    7:{'Princeton University':'United States'},       
    8:{'University of California,Los Angeles(UCLA)':'United States'},       
    9:{'The University of Edinburgh':'United Kingdom'},
    10:{'University of Toronto':'Canada'},
    11:{'Columbia University':'United States'},       
    12:{'University of Chicago':'United States'},       
    13:{'UCL':'United Kingdom'},
    14:{'Kings College London':'United Kingdom'},      
    15:{'New York University (NYU)':'United States'},       
    16:{'Duke University':'United States'},
    17:{'University of British Columbia':'Canada'},      
    18:{'The University of Melbourne':'Australia'},      
    19:{'Cornell University':'United States'}, 
    20:{'The University of Sydney':'Australia'},      
    20:{'University of Pennsylvania':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugpsyt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Psychology")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Psychology Program Are Listed Below .',font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},      
    2:{'Stanford University':'United States'},
    3:{'University of Cambridge':'United Kingdom'},      
    4:{'University of Oxford':'United Kingdom'},   
    5:{'University of California,Berkeley(UCB)':'United States'},       
    6:{'University of California,Los Angeles(UCLA)':'United States'},       
    7:{'UCL':'United Kingdom'},
    8:{'Yale University':'United States'},       
    9:{'Massachusetts Institute of Technology (MIT)':'United States'},       
    10:{'University of Michigan':'Ann Arbor,United States'},
    11:{'New York University (NYU)':'United States'},
    12:{'Columbia University':'United States'},
    13:{'University of British Columbia':'Canada'},      
    14:{'University of Pennsylvania':'United States'},       
    15:{'University of Amsterdam':'Netherlands'},
    16:{'University of Chicago':'United States'},      
    17:{'Princeton University':'United States'},     
    18:{'The University of Melbourne':'Australia'},       
    19:{'University of Toronto':'Canada'},
    20:{'Kings College London':'United Kingdom'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugnurst():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Nursing")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Nursing Program Are Listed Below .',font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'University of Pennsylvania':'United States'},
            2:{'King\'s College London':'United Kingdom'},
            3:{'University of Manchester':'United Kingdom'},
            4:{'Johns Hopkings University':'United States'},
            5:{'University of Southampton':'United Kingdom'},
            6:{'University of California':'United Sates'},
            7:{'University of Toronto':'Canada\t'},
            8:{'University of Washington':'United States'},
            9:{'Yale University':'United States'},	
            10:{'University of Technology Sydney':'Australia'},		
            11:{'University of North Carolina , Chapel Hill':'United States'},		
            12:{'University of Michigan':'United States'},	
            13:{'Duke University':'United States'},
            14:{'Karolinska Institutet':'Sweden\t'},		
            15:{'McMaster University':'Canada\t'},
            16:{'The University of Sydney':'Australia'},
            17:{'Monash University':'Australia'},
            18:{'University of Pittsburgh':'United States'},
            19:{'National University of Singapore (NUS)':'Singapore'},
            20:{'Columbia University':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugchemt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Chemical Engineering")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Chemical Engineering Program Are Listed Below .',font=("Courier",12),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Massachusetts Institute of Technology':'United States'},
            2:{'Stanford University':'United States'},
            3:{'University of Cambridge':'United Kingdom'},
            4:{'University of California , Berkeley (UCB)':'United States'},
            5:{'ETH Zurich':'Switzerland'},
            6:{'University of Oxford':'United Kingdom'},
            7:{'California Institute of Technology (Caltech)':'United States'},
            8:{'EPFL':'Switzerland'},
            9:{'National University of Singapore (NUS)':'Singapore'},	
            10:{'Imperial College London':'United Kingdom'},		
            11:{'Nanyang Technological University (NTU)':'Singapore'},		
            12:{'Tsinghua University':'China\t'},	
            13:{'Delft University of Technology':'Netherlands'},
            14:{'The University of Tokyo':'Japan\t'},		
            15:{'Princeton University':'United States'},
            16:{'University of California (UCLA)':'United States'},
            17:{'Yale University':'United States'},
            18:{'UCL':'United Kingdom'},
            19:{'Kyoto University':'Japan\t'},
            20:{'University of Texas':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)
    
def ugbiot():
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Biology")
    ugcomp.configure(bg="#FCDFFF")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Biology Program Are Listed Below .',font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#FCDFFF")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=90.25)
    csc={'':{'':''},
    1:{'Harvard University':'United States'},
            2:{'Massachusetts Institute of Technology':'United States'},
            3:{'Stanford University':'United States'},
            4:{'University of Cambridge':'United Kingdom'},
            5:{'University of California , Berkeley':'United States'},
            6:{'University of California , San Francisco':'United States'},
            7:{'University of Oxford':'United Kingdom'},
            8:{'University of California , San Diego':'United States'},
            9:{'Johns Hopkins University':'United States'},	
            10:{'University of Toronto':'Canada\t'},		
            11:{'Cornell University':'United States'},		
            12:{'University College London':'United Kingdom'},	
            13:{'University of Michigan , Ann Arbor':'United States'},
            14:{'Columbia University':'United States'},		
            15:{'Swiss Federal Institute of Technology Zurich':'Switzerland'},
            16:{'University of Copenhagen':'Denmark\t'},
            17:{'University of Washington':'United States'},
            18:{'University of California , Los Angeles':'United States'},
            19:{'University of Pennsylvania':'United States'},
            20:{'Yale University':'United States'}}
    f=z=w=0
    for v,k in csc.items():
        vv=tk.Label(ugcomp,text=str(v),font=("Courier",10),bg="#FCDFFF")
        vv.place(x=40,y=90+f)
        for a,b in k.items():
            aa=tk.Label(ugcomp,text=a,font=("Courier",10),bg="#FCDFFF")
            aa.place(x=400,y=90+z)
            bb=tk.Label(ugcomp,text=b,font=("Courier",10),bg="#FCDFFF")
            bb.place(x=150,y=90+w)
            z+=20
            w+=20
        f+=20

    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#FCDFFF")
    namelab.place(x=20,y=510)

def ugdegrees():
    def contact_us():
        messagebox.showinfo("Contact Details ", "Email us at: collegehelp@helpus.com \nCall us at: 12345678")
    lugdeg=tk.Tk()
    lugdeg.title("UNDERGRADUATE DEGREE")
    lugdeg.configure(bg="#D4F0F0")
    lugdeg.geometry("650x500")
    text=tk.Label(lugdeg,text="Choose Program :",font=("Courier",18,"bold"),bg="#D4F0F0")
    text.place(x=200,y=20)
    ugcsc = tk.Button(lugdeg, text="Computer Science", font=10, bg="#FFFFFF",command=ugcsct)
    ugcsc.place(x=20,y=80)
    ugcom=tk.Button(lugdeg,text="Communications",font=10,bg="#FFFFFF",command=ugcomt)
    ugcom.place(x=370,y=80)
    ugpolisci = tk.Button(lugdeg, text="Government / Political Science", font=10, bg="#FFFFFF",command=ugpoliscit)
    ugpolisci.place(x=320, y=140)
    update = tk.Button(lugdeg, text="Buisness", font=10, bg="#FFFFFF",command=ugbust)
    update.place(x=60, y=140)
    ugeco = tk.Button(lugdeg, text="Economics", font=10, bg="#FFFFFF",command=ugecot)
    ugeco.place(x=50,y=200)
    ugeng = tk.Button(lugdeg, text="English Language / Literature", font=10, bg="#FFFFFF",command=ugengt)
    ugeng.place(x=320,y=200)
    ugpsy = tk.Button(lugdeg, text="Psychology", font=10, bg="#FFFFFF",command=ugpsyt)
    ugpsy.place(x=50,y=260)
    ugnurs = tk.Button(lugdeg, text="Nursing", font=10, bg="#FFFFFF",command=ugnurst)
    ugnurs.place(x=405,y=260)
    ugchem = tk.Button(lugdeg, text="Chemical Engineering", font=10, bg="#FFFFFF",command=ugchemt)
    ugchem.place(x=350,y=320)
    ugbio = tk.Button(lugdeg, text="Biology", font=10, bg="#FFFFFF",command=ugbiot)
    ugbio.place(x=70,y=320)
    cont = tk.Button(lugdeg, text="Contact Us For More Info", font=10, bg="#FFFFFF",command=contact_us)
    cont.place(x=180, y=400)
    lugdeg.mainloop()

def gdegrees():
    def contact_us():
        messagebox.showinfo("Contact Details ", "Email us at: collegehelp@helpus.com \nCall us at: 12345678")
    lgdeg=tk.Tk()
    lgdeg.title("GRADUATE DEGREE")
    lgdeg.configure(bg="#D4F0F0")
    lgdeg.geometry("650x500")
    text=tk.Label(lgdeg,text="Choose Program :",font=("Courier",18,"bold"),bg="#D4F0F0")
    text.place(x=200,y=20)
    gcsc = tk.Button(lgdeg, text="Finance", font=10, bg="#FFFFFF",command=gfint)
    gcsc.place(x=110,y=80)
    gcom=tk.Button(lgdeg,text="Computer Science",font=10,bg="#FFFFFF",command=gcsct)
    gcom.place(x=370,y=80)
    gpolisci = tk.Button(lgdeg, text="Marketing", font=10, bg="#FFFFFF",command=gmarkt)
    gpolisci.place(x=400, y=140)
    pdate = tk.Button(lgdeg, text="Mathematics", font=10, bg="#FFFFFF",command=gmatht)
    pdate.place(x=90, y=140)
    geco = tk.Button(lgdeg, text="Business", font=10, bg="#FFFFFF",command=gbusit)
    geco.place(x=100,y=200)
    geng = tk.Button(lgdeg, text="Information System", font=10, bg="#FFFFFF",command=ginfot)
    geng.place(x=370,y=200)
    gpsy = tk.Button(lgdeg, text="Physics", font=10, bg="#FFFFFF",command=gphyt)
    gpsy.place(x=110,y=260)
    gnurs = tk.Button(lgdeg, text="Accountancy", font=10, bg="#FFFFFF",command=gacct)
    gnurs.place(x=405,y=260)
    gchem = tk.Button(lgdeg, text="Statistics", font=10, bg="#FFFFFF",command=gstatt)
    gchem.place(x=420,y=320)
    gbio = tk.Button(lgdeg, text="Entrepreneurship", font=10, bg="#FFFFFF",command=gentt)
    gbio.place(x=70,y=320)
    cont = tk.Button(lgdeg, text="Contact Us For More Info", font=10, bg="#FFFFFF",command=contact_us)
    cont.place(x=180, y=400)
    lgdeg.mainloop()

def phddegrees():
    def contact_us():
        messagebox.showinfo("Contact Details ", "Email us at: collegehelp@helpus.com \nCall us at: 12345678")
    pdeg=tk.Tk()
    pdeg.title("Ph.D. DEGREE")
    pdeg.configure(bg="#D4F0F0")
    pdeg.geometry("650x400")
    ptext=tk.Label(pdeg,text="Choose Program :",font=("Courier",18,"bold"),bg="#D4F0F0")
    ptext.place(x=200,y=20)
    pcsc = tk.Button(pdeg, text="Biology", font=10, bg="#FFFFFF",command=pbiot)
    pcsc.place(x=100,y=80)
    pcom=tk.Button(pdeg,text="Physics",font=10,bg="#FFFFFF",command=pphyt)
    pcom.place(x=450,y=80)
    ppolisci = tk.Button(pdeg, text="Chemistry", font=10, bg="#FFFFFF",command=pchemt)
    ppolisci.place(x=438, y=140)
    ppdate = tk.Button(pdeg, text="Computer Science", font=10, bg="#FFFFFF",command=pcsct)
    ppdate.place(x=60, y=140)
    peco = tk.Button(pdeg, text="Phisiology", font=10, bg="#FFFFFF",command=pphist)
    peco.place(x=90,y=200)
    peng = tk.Button(pdeg, text="Management", font=10, bg="#FFFFFF",command=pmant)
    peng.place(x=425,y=200)
    ugpsy = tk.Button(pdeg, text="Mathematics", font=10, bg="#FFFFFF",command=pmatht)
    ugpsy.place(x=75,y=260)
    ugnurs = tk.Button(pdeg, text="Economics", font=10, bg="#FFFFFF",command=pecot)
    ugnurs.place(x=430,y=260)
    cont = tk.Button(pdeg, text="Contact Us For More Info", font=10, bg="#FFFFFF",command=contact_us)
    cont.place(x=180, y=320)
    pdeg.mainloop()

def mainsc():
    mainscreen = tk.Tk()
    mainscreen.configure(bg="#FFD2BC")
    mainscreen.geometry("600x500")
    mainscreen.title("College Search")
    text=tk.Label(mainscreen,text="Choose Which Degree You Want To Search About :",font=("courier",15,"bold"),bg="#FFD2BC")
    text.place(x=30,y=150)
    ug=tk.Button(mainscreen,text="Undergraduate",font=10,bg="#FFFFEB",command=ugdegrees)
    ug.place(x=60,y=225)
    g=tk.Button(mainscreen,text="Graduate",font=10,bg="#FFFFEB",command=gdegrees)
    g.place(x=270,y=225)
    phd=tk.Button(mainscreen,text="Ph.D.",font=10,bg="#FFFFEB",command=phddegrees)
    phd.place(x=440,y=225)
    phd=tk.Button(mainscreen,text="Apply for College",font=10,bg="#FFFFEB",command=inp)
    phd.place(x=70,y=300)
    phd=tk.Button(mainscreen,text="Calculate GPA",font=10,bg="#FFFFEB",command=agpa)
    phd.place(x=350,y=300)
    mainscreen.mainloop()


mainsc()
