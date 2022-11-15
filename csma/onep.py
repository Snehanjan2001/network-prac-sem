#always checks for the data if flowing
import threading
import time

frameTime=3
interFrameTime=1

totalFrames =0
numFrames =5

def log(lock, totalFramesWillBeSent):
    global totalFrames
    tmp = 0
    used = 0
    while totalFrames < totalFramesWillBeSent:
        if lock.locked():
            used += 1
        tmp += 1
    print(f"Channel utilization -> {used/tmp}")


class CSMA(threading.Thread):
    def __init__(self,lock,index):
        super().__init__()
        self.lock=lock
        self.index=index

    def run(self):
        global numFrames
        global totalFrames
        count=1

        while count <= numFrames:
            #Attempting to send the numFrames
            print(f"Attempting to send Frame{count} to Node {self.index}")

            # go away if the node is locked
            while self.lock.locked:
                pass

            #Acquire lock
            self.lock.acquire()
            time.sleep(frameTime)
            totalFrames += 1
            print(f"[Successful] Frame {count} | Node {self.index}")
            # Release lock
            self.lock.release()
            # Sleep for interframe time
            time.sleep(interFrameTime)
            count+=1

if __name__=='__main__':
    numberNodes = int(input("Enter number of nodes: "))
    numFrames = int(input("Enter number of frames will be sent by frame : "))

    lock = threading.Lock() # Lock object
    nodes = [CSMA(lock,i+1) for i in range(0,numberNodes)] # List of nodes
    # Create log thread
    logThread = threading.Thread(target=log, args=[lock, numberNodes*numFrames])
    logThread.start()
    # Start all threads
    for node in nodes:
        node.start()    
    # Wait for all threads to finish
    for node in nodes:
        node.join()
    # Wait for log thread to finish
    logThread.join()