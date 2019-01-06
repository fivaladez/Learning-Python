#EJ30_P2 Exceptions

#try:
    #Runs first
    # < code >
#except:
    #Runs if exception pccurs in try block
    # < code >
#else:
    # Executes if try block *succeeds*
    # < code >
#finally:
    # This code #always* Executes
    # < code >

# Example
import logging
import time
import os

# Create logger
logging.basicConfig(filename = os.getcwd() + os.sep + "problems_EJ30.log",
level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at "path" and measyre time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    # FileNotFoundError is not defined in Pthon 2
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path,time=dt))

data = read_file_timed( os.getcwd() + os.sep + "audio_file.wav" )# 45 MB file
