import turtle as tut, tkinter as tk,tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox, END
        
def ugcsct():
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

def ugcomt():
    
    ugcomp=tk.Toplevel()
    ugcomp.title("Communications")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Communications Program Are Listed Below .',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugpoliscit():
    ugcomp=tk.Toplevel()
    ugcomp.title("Government / Political Science")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Government / Political Science Program Are Listed Below .',font=("Courier",12),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugbust():
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Business")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Business Program Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugecot():   
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Economics")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Economics Program Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugengt():
        
    ugcomp=tk.Toplevel()
    ugcomp.title("English Language and Literature")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For English Language and Literature Program Are Listed Below .',font=("Courier",11),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugpsyt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Psychology")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Psychology Program Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugnurst():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Nursing")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Nursing Program Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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

def ugchemt():
                
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Chemical Engineering")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Chemical Engineering Program Are Listed Below .',font=("Courier",12),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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
    
def ugbiot():
        
    ugcomp=tk.Toplevel()
    ugcomp.title("Biology")
    ugcomp.configure(bg="#CCE2CB")
    ugcomp.geometry("900x550")
    namelab=tk.Label(ugcomp,text='Top 20 Universities In The World For Biology Program Are Listed Below .',font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=20)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
    namelab.place(x=20,y=51)
    namelab=tk.Label(ugcomp,text='RANK\t    LOCATION\t\t\t   UNIVERSITIES',font=("Courier",13),bg="#CCE2CB")
    namelab.place(x=20,y=70)
    namelab=tk.Label(ugcomp,text=str('-'*72),font=("Courier",14),bg="#CCE2CB")
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
