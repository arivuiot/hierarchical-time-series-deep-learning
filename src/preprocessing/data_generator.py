import numpy as np, pandas as pd
np.random.seed(42)
def generate():
 rows=[]
 for r in range(2):
  for s in range(5):
   for k in range(5):
    base=100+r*20+s*5
    series=base+np.cumsum(np.random.normal(0,3,150))
    for t,v in enumerate(series): rows.append([r,s,k,t,max(v,1)])
 return pd.DataFrame(rows,columns=['region','store','sku','time','sales'])
if __name__=='__main__': generate().to_csv('data/hierarchical_sales.csv',index=False)
