# Build: docker build -t pyrevdns:latest .
# Run: docker run -it --rm pyrevdns -h

# Base Image
FROM cgr.dev/chainguard/python:latest-dev@sha256:7805dfaa784da1919f3479c497d03f4e6d6b2c5bf28a8968edf679b08a29c32c

# Maintainer
LABEL maintainer="Shivam Saraswat <thecybersapien@protonmail.com>"
LABEL description="PYrevDNS is a simple tool for performing reverse DNS lookups on IP addresses."

# Set Work Directory
WORKDIR /usr/src/app
# Copy Project
COPY . .

# Install Project Dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Start with console arguments passed to docker run
ENTRYPOINT ["python3", "pyrevdns"]
