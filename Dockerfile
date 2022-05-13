FROM python:3.9-slim-buster as pex-bundle-build

# Build deps
RUN apt-get update -qq -y && \
    apt-get install -qq -y \
    curl \
    build-essential \
    git \
    zip

ARG PANTS_PANTSD=false
ARG PANTS_WATCH_FILESYSTEM=false

WORKDIR /build

# Bootstrap pants separately
COPY pants .
COPY pants.toml .
RUN ./pants --version

# Build the bundle
COPY . .
RUN ./pants package singer_bins:singer_pex_bundle


# Get a fresh image and copy in the artifacts
FROM python:3.9-slim-buster

RUN apt-get update -qq -y && apt-get install -qq -y unzip

WORKDIR /.singer_pex/

COPY --from=pex-bundle-build /build/dist/singer_bins/singer_pex_bundle.zip /.singer_pex/

RUN unzip ./singer_pex_bundle.zip && \
    rm singer_pex_bundle.zip && \
    mkdir bin && \
    ls | \
    grep singer_bins. | \
    while read line; \
        do \
            executable_name=${line#"singer_bins."} && \
            cp $line/bin.pex bin/$executable_name && \
            rm -r $line; \
        done

WORKDIR /

ENV PATH="/.singer_pex/bin:${PATH}"
