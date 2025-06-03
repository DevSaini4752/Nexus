#Modules
import sys
from time import sleep as delay

# -----Animation for user interaction and entertainment-----#

def type_write(text, wait=0.002):
    """This function will make the text appear
    to be typed by someone at that moment. This
    is just to entertain user :)"""

    # Explanation

    """Explanation -
    - Loop will give char by char
    - sys.stdout = print() they are same but here
    I have used sys.stdout to customize it

    - sys.stdout.write() - this is more controlled as 
    it is different from others because it don't add 
    a line on it's own this provide us a controlled 
    way to print something

    - sys.stdout.flush() - this forces the content to 
    stdout (print) as python may wait for full msg and 
    wait for it to be typed but here we want a typing 
    effect so we are using it

    - delay - give break between every letter
    - At end print gives a next line """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        delay(wait)
    print()  # To leave a line
