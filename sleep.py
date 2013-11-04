
# name : abosloh
# email : cinema48@gmail.com

# sleep the programe 1,2,3,... seconds
def sleep(sec):
    
    t = int(time()) # get initial time as seconds
    # when the real time greater than initial time + parameter seconds
    # break while and exit from function
    while True:
        if time()>t+1:
            break
        
