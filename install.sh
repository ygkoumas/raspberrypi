#!/bin/bash
chmod 755 __main__.py
cp __main__.py /etc/init.d/shutdown-button.py
update-rc.d shutdown-button.py defaults
