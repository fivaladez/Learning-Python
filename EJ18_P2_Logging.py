#EJ18_P2    Logging - Record progress and problem

#Purpose: Record progress and problems
#Levels: NotSet(0), Debug(10), Info(20), Warnin(30), Error(40), Critical(50)
import logging
import math
import os

#Levels -> CAPITAL CONSTANS
#Classes -> Starts with Capital Letter
#Methods(functions) -> start with lower case letters
#dir(logging)

# Comments are a good place for a log message

# Create and configure a logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = os.getcwd() + "lumberjack.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "w")
logger = logging.getLogger()#Root logger

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

#Example
def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0},{1},{2})".format(a,b,c))

    # Compute the discriminant
    logger.debug(" # Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug(" # Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug(" # Return the roots")
    return (root1, root2)

roots = quadratic_formula(1,0,-4)
print roots

print logger.level
