import csv
import webbrowser
print("""

 _    _ __  __  _____           _     
| |  | |  \/  |/ ____|         | |    
| |__| | \  / | |  __ _ __ __ _| |__  
|  __  | |\/| | | |_ | '__/ _` | '_ \ 
| |  | | |  | | |__| | | | (_| | |_) |
|_|  |_|_|  |_|\_____|_|  \__,_|_.__/ 
                        By Tibin Sunny


                                      
                                      """)
f=open("connected.html","w")
f.write("<center>Designed By Tibin Sunny</Center>")
i=0
a=2
array_arrange=0
stat_code = []
name=raw_input("Enter path to CSV file :")
newpath = r"hmgrab"+name 
if not os.path.exists(newpath):
    os.makedirs(newpath)
with open(name,'rt')as f:
  data = csv.reader(f)
  for row in data:
        if(row[2]==""):
            continue
        else:
            print(row[0])
            k=row[2]
            k=newpath+"/"+k+".txt"
            f=open(k,"a")
            f.write(row[0])
            f.write("\n")
            if row[2] not in stat_code:
                  stat_code.append(row[2])
flag=len(stat_code)
for j in range(flag):
      array_arrange=j
      name=stat_code[array_arrange]
      name_ext=name+".txt"
      f1=open(name_ext,"r")
      f=open(newpath+"/connected.html","a")
    #  f.write("<h1>Data from:"+name_ext+"</h1>")
      f.write("<table border=1>"+name_ext)
      for x in f1:
          f.write("<tr><td><a href="+x+">"+x+"</a><br></td></tr>")
      f.write("")
f.write("</table>")
webbrowser.open("connected.html")

     

