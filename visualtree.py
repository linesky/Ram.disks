code=""
last=0
ttrue=True
files=input("file data name? ")
try:
    f1=open(files,"r")
    code=f1.read()
    f1.close()
except:
    aa=0
while ttrue:
    lines=input("out? ")
    lines=lines.strip()
    if lines=="":
        ttrue=False
    else:
        sp=lines.split(",")
        s1=""
        m=0
        for c in range(len(sp)):
            sp1=[]
            n1=c
            sp1=sp[:n1+1]
            s1=",".join(sp1)
            
            s2="    "*c
            ss2="    "*(c+1)
            s1=s2+"#"+s1+"\n"
            s4=s1+s2+"if value=="+sp[c]+":\n"+ss2+"values="+sp[c]+"\n"
            n4=len(s4)
            nn=code.find(s1)
            if nn<0:
                
                s3=code[:m]
                
                
                s3=s3+s4
                s3=s3+code[m:]
                code=s3
                m=m+n4
            else:
                m=nn+n4+1

        print(code)
try:
    f1=open(files,"w")
    f1.write(code)
    f1.close()
except:
    print("error on write file")
            
            
        
         
    
