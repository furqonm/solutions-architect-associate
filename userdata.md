# 🚀 Automated LAMP Stack Deployment

This repository provides an automated bootstrap script to transform a fresh Amazon Linux instance into a fully functional **LAMP-stack** web server (Linux, Apache, PHP).

Normally, deploying a web server involves manual SSH sessions and repetitive command execution. These scripts eliminate manual intervention by acting as a programmatic "to-do list" for your server's initial launch.

## 🛠️ The Deployment Script

The following bash script handles the system updates, software installation, service management, and permission hardening.

```bash
#!/bin/bash

# 1. Update the system and install software
yum update -y
amazon-linux-extras install -y php8.2
yum install -y httpd

# 2. Manage Apache service
systemctl start httpd
systemctl enable httpd

# 3. Configure permissions for the web directory
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 :{} \;

# 4. Create a test landing page
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php

```

---

## 🔍 How It Works

### **Phase 1: Installation**

The script first synchronizes the package manager (`yum update`) to ensure security patches are current. It then pulls **PHP 8.2** via the Amazon Linux Extras repository and installs the **Apache (httpd)** web server.

### **Phase 2: Service Management**

It triggers the `systemctl` daemon to start the web server immediately and ensures that Apache automatically restarts if the server ever reboots.

### **Phase 3: Permission Hardening**

To allow the `ec2-user` to upload files without needing `sudo` every time, the script:

* Adds the user to the `apache` group.
* Sets the **SGID (Set Group ID)** bit (`chmod 2775`), ensuring new files created in the directory inherit the correct group permissions automatically.

### **Phase 4: Verification**

Finally, it generates a `phpinfo.php` file. Once the script finishes, you can navigate to `http://your-server-ip/phpinfo.php` to verify that the PHP engine is communicating correctly with Apache.
