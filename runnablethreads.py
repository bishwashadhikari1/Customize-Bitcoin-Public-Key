import threading

from combinations import combinations, trywallet

def runthreads():
    # function leveraging thread to run tasks simultaneously

    keywords = combinations() # retrieves and stores list of possible keywords to satisfy requirement


    # basically threads 
    
    t1 = threading.Thread(target=trywallet, args=[keywords])

    t2 = threading.Thread(target=trywallet, args=[keywords])

    t3 = threading.Thread(target=trywallet, args=[keywords])

    t4 = threading.Thread(target=trywallet, args=[keywords])

    t5 = threading.Thread(target=trywallet, args=[keywords])

    t6 = threading.Thread(target=trywallet, args=[keywords])

    t7 = threading.Thread(target=trywallet, args=[keywords])

    t8 = threading.Thread(target=trywallet, args=[keywords])

    t1.start()

    t2.start()

    t3.start()

    t4.start()

    t5.start()

    t6.start()

    t7.start()

    t8.start()