code=""
last=0
ttrue=True
while ttrue:
    lines=input("get text?")
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
            sp1=sp[:n1]
            s1=",".join(sp1)
            
            s2="    "*c
            s1=s2+"#"+s1+"\n"
            nn=code.find(s1)
            if nn<0:
                
                s3=code[:m]
                s4=s1+s2+"if value=="+sp[c]+":\nvalues="+sp[c]+"\n"
                n4=len(s4)
                s3=s3+s1+s2+"if value=="+sp[c]+":\nvalues="+sp[c]+"\n"
                s3=s3+code[m:]
                code=s3
                m=m+n4
            else:
                m=nn+len(s1)+1

        print(code)
            
            
        
         
    
