import sys
import utils.utils as u
from classes.my_document import MyDocument


class DocumentManager(object):
    def __init__(self, argv):
        self.argv = argv
        self.check_arguments()

    def check_arguments(self):
        if len(self.argv) < 2:
            # print("\n\nNo date argument specified.\n")
            # sys.exit()
            date_string = u.next_saturday()

        else:
            date_string = self.argv[1]

        if len(date_string) > 6:
            date_string2 = date_string[0:6]
        else:
            date_string2 = date_string

        if not u.validate_date_code(date_string2):
            print("\n\nSpecify a valid date argument.\n")
            sys.exit()

        document = MyDocument(date_string)
        document.mark_links_with_image()

    def go(self):
        a = 1
