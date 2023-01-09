# tomllib is only avaible since py3.11
try:
    import tomllib as toml
# for <3.11 we use the 'toml' library
# available on PyPI
except ModuleNotFoundError:
    import toml

import argparse

import qrcode
import qrcode.image.svg

def create_qr(data, fpath="github_qr.gif"):
    factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(data, image_factory=factory)
    img.save(fpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', 
                        type=str,
                        default="config.toml",
                        help='path to the config file ("config.toml" by default)')
    
    args = parser.parse_args()

    config = toml.load(args.config)
    create_qr(config["github_url"], "qr_code.svg")