# Imagine you need to deploy a new web server for a PHP application. Normally, this involves several manual steps: launching a virtual server, connecting to it via SSH, and then running a series of commands to install and configure the necessary software.

# The scripts below are designed to be that to-do list, transforming a brand-new, generic Linux instance into a fully functional LAMP-stack web server (Linux, Apache, PHP - MySQL would be the next step) without any manual intervention.

#!/bin/bash

yum update -y
amazon-linux-extras install -y php8.2
yum install -y httpd

systemctl start httpd
systemctl enable httpd

usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;

echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php