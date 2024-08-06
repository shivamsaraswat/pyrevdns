# Build: docker build -t pyrevdns:latest .
# Run: docker run -it --rm pyrevdns -h

# Base Image
FROM cgr.dev/chainguard/python:latest-dev@sha256:ede036bd6cac024a9ab1c6fca3a324f4dbcfe82f67f5c3b7bf1fbf2ef9f8f0e3

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
