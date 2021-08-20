import os

def changepath(path,n):
    #path is string type so do a right find and get \ symbol's position
    for i in range(n):
            
        pos1 = path.rfind('\\')
        #print('Position -',pos1) # its working . its finding the last \ symbol

        newstr= path[pos1:]
      


        path2 = path
        path = path.replace(newstr,' ' )
        
        path  = path.rstrip() # working . removing only the trailing spaces 
       
    # change dir

    #cur_path = os.getcwd()
    #print('curr path -',cur_path)
    # NOTE = THIS WORKS PROPELY ONLY WHEN THE DIR IS NOT TRIED TO BE CHANGED TO THE ROOT OR THE HARDISK HOME. EX = G:HOME\SDSSD IS CHANGED TO G:. THEN IT WILL NOT WORK.
    return ('path changed')


changepath(path,n)

