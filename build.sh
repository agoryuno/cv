#!/bin/bash

export GITHUB_URL="https://github.com/agoryuno/cv/tree/tech_variant"
export QR_FILE="qr_code.xml"

python make_qr.py

python preprocess.py cv_page1_plain.svg --github=$GITHUB_URL
python preprocess.py cv_page2_plain.svg --github=$GITHUB_URL

inkscape $PWD/cv_page1_plain_out.svg --export-pdf=goryunov_page1.pdf
inkscape $PWD/cv_page2_plain_out.svg --export-pdf=goryunov_page2.pdf

pdftk goryunov_page1.pdf goryunov_page2.pdf cat output goryunov_cv.pdf

rm cv_page1_plain_out.svg
rm cv_page2_plain_out.svg
rm goryunov_page1.pdf
rm goryunov_page2.pdf
rm $QR_FILE
