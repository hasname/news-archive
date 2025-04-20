#!/bin/sh

set -eou pipefail

#
PROJECT_NAME="news-archive"

# pypy
rm -fr .venv
mise exec uv@latest -- uv venv --python pypy3

# systemd
mkdir -p ~/.config/systemd/user || true
cp "${PROJECT_NAME}".service ~/.config/systemd/user/"${PROJECT_NAME}".service
systemctl --user daemon-reload
systemctl --user enable "${PROJECT_NAME}".service
systemctl --user restart "${PROJECT_NAME}".service
