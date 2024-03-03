def hackerrankInString(s):
    h='hackerrank'
    c=0
    for i in s:
        if i==h[c]:
            c+=1
        if c==len(h):# for making sure that when at some point of time c will fulfil condition and also exceed length 
            return 'YES' # it should not resturn no .  
            
            
    if c==len(h):
        return 'YES'
    else:
        return 'NO'
    
