import os
import argparse
from jinja2 import Environment, FileSystemLoader

def main(infile, outfile=None, template_path=""):

    env = Environment(loader=FileSystemLoader(template_path))

    template = env.get_template(infile)
    out_str = template.render()

    if not outfile:
        fname, ext = os.path.splitext(infile)
        outfile = f"{fname}_out{ext}"
    
    with open(outfile, "w") as f:
        f.write(out_str)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess XML files for Inkscape.')
    parser.add_argument('files', type=str, nargs="+",
                        help=("The input and output file names. If output file isn't"
                              "provided then it is assumed to be <input_name>_out.<extension>"))

    args = parser.parse_args()
    main(*args.files)