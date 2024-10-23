FROM ubuntu:20.04
# Set the timezone non-interactively
ENV TZ=America/New_York
ARG DEBIAN_FRONTEND=noninteractive

# Set the desired timezone (e.g., "America/New_York")
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Install Node.js
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get install -y python3 python3-pip python3-dev

# Install Lighthouse
RUN npm install -g lighthouse

RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

RUN mkdir -p /var/run/dbus
RUN dbus-daemon --config-file=/usr/share/dbus-1/system.conf --print-address
RUN apt-get clean
# Check if Chromium is installed
RUN if command -v google-chrome-stable > /dev/null; then echo "Chromium is installed"; else echo "Chromium is not installed"; fi

CMD ["lighthouse", "--help"]