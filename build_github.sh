#!/bin/bash

python preprocess.py cv_page1_plain.svg
python preprocess.py cv_page2_plain.svg

inkscape cv_page1_plain_out.svg --export-pdf=goryunov_page1.pdf
inkscape cv_page2_plain_out.svg --export-pdf=goryunov_page2.pdf

pdftk goryunov_page1.pdf goryunov_page2.pdf cat output $GITHUB_WORKSPACE/goryunov_cv.pdf