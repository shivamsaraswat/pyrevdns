# Build: docker build -t pyrevdns:latest .
# Run: docker run -it --rm pyrevdns -h

# Base Image
FROM cgr.dev/chainguard/python:latest-dev@sha256:39d3b461ec14222f7eadb6cf5c64153291c03aca514e09b307b77aa60d0f0a3b

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
