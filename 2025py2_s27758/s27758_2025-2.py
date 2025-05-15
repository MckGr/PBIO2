from Bio import Entrez,SeqIO
import matplotlib.pyplot as plt,pandas as p,socket
def f(e,k,t,a,b,n):
 Entrez.email,Entrez.api_key=e,k
 try:r=Entrez.read(Entrez.esearch(db="nucleotide",term=f"txid{t}[Organism]",retmax=n,usehistory="y"))
 except:return[]
 i=r["IdList"]
 if not i:return[]
 try:h=Entrez.efetch(db="nucleotide",id=",".join(i),rettype="gb",retmode="text")
 except:return[]
 return[r for r in SeqIO.parse(h,"gb")if a<=len(r.seq)<=b]
def s(d,o):
 df=p.DataFrame([{"a":r.id,"l":len(r.seq),"d":r.description}for r in d])
 df.to_csv(o,index=0)
 return df
def g(df,f):
 df=df.sort_values("l",ascending=0)
 plt.figure(figsize=(10,5))
 plt.plot(df["a"],df["l"],marker="o")
 plt.xticks(rotation=90)
 plt.tight_layout()
 plt.savefig(f)
 plt.close()
if __name__=="__main__":
 e=input("Email: ");k=input("API Key: ");t=input("TaxID: ")
 a,b,n=[int(input(x+": "))for x in("Min","Max","Num")]
 d=f(e,k,t,a,b,n)
 if d:
  c=f"r_{t}.csv";m=f"r_{t}.png"
  df=s(d,c);g(df,m)
  print("CSV:",c,"Plot:",m)
 else:print("Brak wyników.")
