"""
This file provides a library of music exception types that are used throughout the project to better report errors to the user.

Exception Types:

TabException - general exception type for the project used to report general errors in the tab that cannot be reported more specifically
MeasureException - caused by the construction of a Measure whose length is not <= 1
TabFileException - error caused by incorrect input tab file
TabIOException - error caused by file reading/writing in tab program.
TabConfigurationException - exception caused by incorrect program configuration file
StaffException - caused by illegal StaffString object construction
StaffOutOfBoundsException - caused by accessing a StaffString index that is out of bounds
LoggingException - caused by failure of logging operations.

Some of these exceptions are used in try-except clauses that handle a more generic Python exception (e.g. ValueError, IOError) and then raise one of these exception types
to better inform the user.

author: Chami Lamelas
date: Summer 2019
"""

README_LINK = "https://github.com/LiquidsShadow/Music_Tab_Project/blob/master/README.md"

class TabException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

class MeasureException(TabException):
    def __init__(self, op, reason):
        super().__init__("Operation on Measure failed: {0}. Reason: {1}.".format(op, reason))

class TabFileException(TabException):
    DEFAULT_LINE = -1

    def __init__(self, issue, reason, line=DEFAULT_LINE):
        errorMsg = "Issue with the tab file: \"{0}\". Reason: {1}.".format(issue, reason)
        if line != TabFileException.DEFAULT_LINE:
            errorMsg += " Approximate line number: {0}.".format(line)
        super().__init__(errorMsg + " Please review the input file and the guidelines outlined in the program README here {0}".format(README_LINK))

class TabIOException(TabException):
    def __init__(self, issue, reason):
        super().__init__("I/O Error with \"{0}\". Reason: {1}.".format(issue, reason))

class TabConfigurationException(TabException):
    # first line in the file is line 1. Line=0 means source of problem couldn't be identified.
    def __init__(self, reason="not specified", line=0):
        super().__init__("Program configuration failed. Error on line {0}. Reason: {1}. To reset the config. file see the README at {2}.".format(line, reason, README_LINK))

class StaffException(TabException):
    def __init__(self, op, reason, str):
        super().__init__("Staff operation cannot be performed: \"{0}\", Reason: {1}. str={2}".format(op, reason, str))

class StaffOutOfBoundsException(TabException):
    def __init__(self, reason, viol):
        super().__init__("Bounds Violation, reason: {0} ({1})".format(reason, viol))

class LoggingException(Exception):
    def __init__(self, op, reason):
        self.msg = "Log operation \"{0}\" failed. Reason: {1}".format(op, reason)
    def __str__(self):
        return str(self.msg)

"""
TODO 
"""
def handleTraceback(tracebackStr):
    pass
