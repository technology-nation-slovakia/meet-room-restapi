# console log module
from app import app
import datetime

# terminal colors for logs
class termcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def console_log(text, style):
    # if not app.debug:
    #     return
    current_time = datetime.datetime.utcnow().strftime("[%d/%m/%Y %H:%M:%S] ")

    print(current_time, end='')

    if style == 'note':
        print(termcolor.OKBLUE, end="")
    elif style == 'info':
        print(termcolor.OKGREEN + 'INFO ', end="")
    elif style == 'warning':
        print(termcolor.WARNING + 'WARNING ', end="")
    elif style == 'fail':
        print(termcolor.FAIL + 'FAILED ', end="")

    print(text, termcolor.ENDC)

def sql_log(text, style):
    if app.config['SQL_DEBUG']:
        console_log(text, style)
