#!/bin/sh

set -eou pipefail

#
PROJECT_NAME="news-archive"

# pypy
rm -fr .venv
mise exec uv@latest -- uv venv --python pypy3

# systemd
mkdir -p ~/.config/systemd/user || true
cp daemon/"${PROJECT_NAME}"-daemon.service ~/.config/systemd/user/"${PROJECT_NAME}"-daemon.service
cp web/"${PROJECT_NAME}"-web.service ~/.config/systemd/user/"${PROJECT_NAME}"-web.service
systemctl --user daemon-reload
systemctl --user enable "${PROJECT_NAME}"-daemon.service
systemctl --user enable "${PROJECT_NAME}"-web.service
systemctl --user restart "${PROJECT_NAME}"-daemon.service
systemctl --user restart "${PROJECT_NAME}"-web.service
