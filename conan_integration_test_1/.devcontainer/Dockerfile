# Use a specific Ubuntu version as the base
ARG IMAGE_NAME
ARG IMAGE_VERSION
FROM ${IMAGE_NAME}:${IMAGE_VERSION}

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install sudo and other required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends sudo && \
    rm -rf /var/lib/apt/lists/*

# Create a generic user with sudo privileges
#RUN useradd -m devuser && \
#    echo "devuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set up devuser and ensure file permissions
#RUN adduser --disabled-password --gecos "" devuser \
#    && usermod -aG sudo devuser \
#    && chown -R devuser:devuser /workspace


# Update package lists and install essential development tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    gdb \
    clangd \
    clang-tidy \
    python3 \
    python3-pip \
    python3-venv\
    git \
    curl \
    wget \
    unzip \
    protobuf-compiler \
    libprotobuf-dev \
    nodejs \
    npm \
    ninja-build \
    ssh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install additional Python packages if needed
RUN python3 -m venv /opt/venv
#RUN /opt/venv/bin/pip install --no-cache-dir conan
#RUN /opt/venv/bin/pip install --no-cache-dir numpy scipy matplotlib

# Set the default working directory
#WORKDIR /workspace

# Set the default command to bash
CMD ["/bin/bash"]


