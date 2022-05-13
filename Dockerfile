FROM python:3.9-slim-buster

RUN apt-get update -qq -y && apt-get install -qq -y unzip

WORKDIR /.singer_pex/
COPY dist/singer_bins/singer_pex_bundle.zip /.singer_pex/
RUN unzip ./singer_pex_bundle.zip && rm singer_pex_bundle.zip
