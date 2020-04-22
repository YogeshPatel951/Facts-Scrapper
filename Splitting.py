import pandas as pd
a=pd.read_csv('OneMillionFacts.csv')
cnt=0
end=0
start=0
while(1):
    end=end+100000
    last=a.shape[0]
    
    if(end<last):
        b=a[start:end]
        b.to_csv(str(cnt)+'.csv')
        print(cnt)
        cnt=cnt+1
        start=end
        
        
    else:
        end=last
        b=a[start:end]
        b.to_csv(str(cnt)+'.csv')
        print(cnt)
        cnt=cnt+1
        start=end
        break
    
        
        
