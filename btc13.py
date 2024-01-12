#đọc file
def read(filename):
    with open(filename,"r") as f:
        a=f.read()
        print("nội dung file:\n",a)
        f.close()

def  report(filename):
     with open(filename,"r") as f:
         a=f.readlines()
         print("line=",len(a))
         d=[]
         for i in f:
           b=int(ord(i))
           if (b>=97 and b<=122) or (b>=65 and b<=90):
            d.append(i)
         print("words=",len(d))
         b=[]
         for i in f:
             b.append(i)
         print("char=",len(b))
         f.close()
         
def write(filename,content):
     with open(filename,"w") as f: 
          f.write(content)
          f.close()

def write_append(filename,content):
    while True:     
         with open(filename,"a") as f:
             f.write(content,"\n")
             f.close()
         a=int(input("tiếp tục nhập\n1:có   0:không\nnhập lựa chọn:"))
         if a==1:
            continue
         if a==0:
            break

def read_csv(filename):
    import csv
    with open(filename) as f:
        for i in csv.reader(f):
            print(i)
        f.close()    

def write_csv(filename,content):
    import csv
    with open(filename,"w") as f:
        csv.writer(f).writerow(content)
    f.close()    