# tomllib is only avaible since py3.11
try:
    import tomllib as toml
# for <3.11 we use the 'toml' library
# available on PyPI
except ModuleNotFoundError:
    import toml

import os
import argparse

import qrcode
import qrcode.image.svg
from qrcode.compat.etree import ET

def create_qr(data, 
        fpath="github_qr.gif", 
        error_correction=qrcode.ERROR_CORRECT_M,
        full_svg=False,
        fill_color="black",
        back_color="white",
        box_size=7,
        border=0):
    
    factory = qrcode.image.svg.SvgPathImage

    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
        image_factory=factory
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    if full_svg:
        img.save(fpath)
        return
    ET.ElementTree(img.path).write(fpath, xml_declaration=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', 
                        type=str,
                        default=None,
                        help='path to the config file ("config.toml" by default)')
    
    args = parser.parse_args()
    github_url = os.environ.get("GITHUB_URL")
    qr_file = os.environ.get("QR_FILE")
    if args.config:
        config = toml.load(args.config)
        github_url = config.get("github_url")
        qr_file = config.get("qr_file")
    assert github_url, ("A Github URL must be supplied either in the "
                        "GITHUB_URL environment variable or the "
                        "'github_url' setting in the config file."
                       )
    assert qr_file, ("Name of the output file must be supplied either "
                     "in the QR_FILE environment variable or the "
                     "'qr_file' setting in the config file."
                    )

    
    create_qr(github_url, qr_file, full_svg=False)