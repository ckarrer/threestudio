# Reference:
# https://github.com/cvpaperchallenge/Ascender
# https://github.com/nerfstudio-project/nerfstudio

FROM nvidia/cuda:12.4.0-devel-ubuntu22.04

ARG USER_NAME=dreamer
ARG GROUP_NAME=dreamers
ARG UID=1000
ARG GID=1000

# Set compute capability for nerfacc and tiny-cuda-nn
# See https://developer.nvidia.com/cuda-gpus and limit number to speed-up build
ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0 7.5 8.0 8.6 8.9 9.0+PTX"
ENV TCNN_CUDA_ARCHITECTURES=90;89;86;80;75;70;61;60
# Speed-up build for RTX 30xx
# ENV TORCH_CUDA_ARCH_LIST="8.6"
# ENV TCNN_CUDA_ARCHITECTURES=86
# Speed-up build for RTX 40xx
# ENV TORCH_CUDA_ARCH_LIST="8.9"
# ENV TCNN_CUDA_ARCHITECTURES=89

ENV CUDA_HOME=/usr/local/cuda
ENV PATH=${CUDA_HOME}/bin:/home/${USER_NAME}/.local/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}
ENV LIBRARY_PATH=${CUDA_HOME}/lib64/stubs:${LIBRARY_PATH}

# apt install by root user
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libegl1-mesa-dev \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    python-is-python3 \
    python3.10-dev \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Change user to non-root user
RUN groupadd -g ${GID} ${GROUP_NAME} \
    && useradd -ms /bin/sh -u ${UID} -g ${GID} ${USER_NAME}
USER ${USER_NAME}

RUN python -m pip install pip==23.0.1
RUN pip install setuptools==69.5.1 ninja
RUN pip install torch==2.4.0+cu124 torchvision==0.19.0+cu124 --index-url https://download.pytorch.org/whl/cu124
# Install nerfacc and tiny-cuda-nn before installing requirements.txt
# because these two installations are time consuming and error prone
RUN pip install git+https://github.com/KAIR-BAIR/nerfacc.git@v0.5.2
RUN pip install git+https://github.com/NVlabs/tiny-cuda-nn.git#subdirectory=bindings/torch

COPY requirements.txt /tmp
RUN cd /tmp && pip install -r requirements.txt
RUN pip install -U fastapi pydantic

# Install extensions
WORKDIR /home/${USER_NAME}/threestudio/custom

## 3dgs extension
RUN git clone https://github.com/DSaurus/threestudio-3dgs.git
RUN cd threestudio-3dgs
RUN git clone --recursive https://github.com/ashawkey/diff-gaussian-rasterization
RUN git clone https://github.com/DSaurus/simple-knn.git
RUN pip install ./diff-gaussian-rasterization
RUN pip install ./simple-knn
RUN pip install pymeshlab
RUN pip install plyfile

WORKDIR /home/${USER_NAME}/threestudio
