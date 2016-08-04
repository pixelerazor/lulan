#!/bin/bash

cp /var/www/html/lulan/000-default.conf /etc/apache2/sites-available/000-default.conf
chmod 644 /etc/apache2/sites-available/000-default.conf
chown root:root /etc/apache2/sites-available/000-default.conf
