FROM ubuntu:22.04

RUN apt update
RUN apt install -y python-is-python3
RUN apt install -y inkscape

RUN apt install -y pdftk

COPY build.sh /
COPY cv_page1_plain.svg /
COPY cv_page2_plain.svg /
COPY preprocess.py /

ENTRYPOINT ["/bin/sh", "build_github.sh"]



