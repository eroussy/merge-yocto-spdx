# Copyright (C) 2021, RTE (http://www.rte-france.com)
# SPDX-License-Identifier: Apache-2.0

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        locales \
        python3 \
        python3-pip \
    && sed -i "s/# en_US\.UTF-8 UTF-8/en_US\.UTF-8 UTF-8/" /etc/locale.gen \
    && locale-gen \
    && dpkg-reconfigure locales \
    && pip install "spdx-tools==0.8.0a2" \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/*

COPY merge_spdx.py /usr/bin/merge
