from classes.environment_variable import EnvironmentVariable
from datetime import datetime
from qrcode.constants import ERROR_CORRECT_L
import os
import qrcode
import sys


class QrMaker(object):
    def __init__(self, url):
        self.box_size = EnvironmentVariable('box_size', 'int', permit_omission=False).value
        self.url = url
        # self.check_arguments()
        self.create_folders()
        self.get_filename()

    def check_arguments(self):
        if len(sys.argv) < 2:
            print("Please supply a URL as an argument")
            sys.exit()
        else:
            url_argument = sys.argv[1]
            if "https" not in url_argument and "www" not in url_argument:
                print("Please supply a valid URL as an argument")
                sys.exit()
            else:
                self.create_folders()
                self.url = sys.argv[1]
                self.get_filename()

    def get_filename(self):
        now = datetime.now()
        url_safe = self.url.replace("https://", "")
        url_safe = url_safe.replace("/", "-").lower()
        date_string = now.strftime("%Y%m%d")
        filename = "qr-{date_string}-{url}.png".format(
            url=url_safe,
            date_string=date_string
        )

        self.filename = os.path.join(self.qr_code_path, filename)

    def create_folders(self):
        self.resources_path = os.path.join(os.getcwd(), "resources")
        self.qr_code_path = os.path.join(self.resources_path, "qr_codes")
        os.makedirs(self.resources_path, exist_ok=True)
        os.makedirs(self.qr_code_path, exist_ok=True)

    def make_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=self.box_size,
            border=0,
        )
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.filename)  # type: ignore[arg-type]
