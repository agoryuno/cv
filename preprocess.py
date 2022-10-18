"""
Inkscape's understanding of XML is rather limited.
For instance, it doesn't know anything about DTD entities.
Therefore, we pass the XML source through Python's standard
ElementTree parser, which assembles the final XML document
and subsitutes all the entity values, so that Inkscape doesn't
have any problems converting it to PDF.
"""

import os
import argparse
from xml.etree import ElementTree as et


def main(infile, outfile=None):
    p = et.parse(infile)

    if not outfile:
        fname, ext = os.path.splitext(infile)
        outfile = f"{fname}_out{ext}"
    
    with open(outfile, "w") as f:
        p.write(f, encoding="unicode")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess XML files for Inkscape.')
    parser.add_argument('files', type=str, nargs="+",
                        help=("The input and output file names. If output file isn't"
                              "provided then it is assumed to be <input_name>_out.<extension>"))

    args = parser.parse_args()
    main(*args.files)