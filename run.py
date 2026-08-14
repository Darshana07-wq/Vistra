import multiprocessing
import subprocess 
# from subprocess import STARTUPINFO, STARTF_FORCEOFFFEEDBACK
from main import start
# from .context import reduction, get_spawning_popen, set_spawning_popen

# Function to run Vistra
def startVistra():
        # Display a message that Vistra is starting
        print("Vistra is starting up.")
        # from main import start
        start()

# Function to listen for a specific wake word
def listenHotword():
        # Display a message that the wake word listener is active
        print("Listening for the wake word.")
        from engine.features import hotword
        hotword()
startVistra()
# subprocess.call([r'device.bat'])
listenHotword()
    # Start both processes
# if __name__ == '__main__':
#         process=[]
#         p1 = multiprocessing.Process(target=startJarvis)
#         p2 = multiprocessing.Process(target=listenHotword)
#         process.append(p1)
#         process.append(p2)
#         p1.start()
#         p2.start()
#         # p1.join()

        # if p2.is_alive():
        #     p2.terminate()
        #     p2.join()

        # print("system stop")