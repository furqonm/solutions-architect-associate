Berikut ini adalah user data untuk EC2 dengan AMI Amazon Linux, Centos, atau Redhat.

```
#!/bin/bash
yum update -y
amazon-linux-extras install -y php7.2
yum install -y httpd
systemctl start httpd
systemctl enable httpd
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
```
