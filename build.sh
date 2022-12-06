#!/bin/bash

inkscape cv_page1_plain.svg --export-pdf=goryunov_page1.pdf
inkscape cv_page2_plain.svg --export-pdf=goryunov_page2.pdf

pdftk goryunov_page1.pdf goryunov_page2.pdf cat output goryunov_cv_tech.pdf