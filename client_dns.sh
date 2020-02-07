#!/usr/bin/env bash

systemctl disable systemd-resolved.service
systemctl stop systemd-resolved.service
rm /etc/resolv.conf
cp resolv.conf /etc/resolv.conf