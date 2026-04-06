#!/bin/bash

echo "Make sure you have sudo when you run this setup!!!!"

# ensure www-data has the right perms to run in /var/www/html/
sudo usermod -aG gpio,i2c,spi,dialout www-data

#echo "Setting up vitual environment..."
#rm -rf venv
#python3 -m venv --system-site-packages venv
#source venv/bin/activate
#pip install adafruit-circuitpython-tcs34725

sudo rm -rf /var/www/html/MarbleMachine
sudo mkdir -p /var/www/html/MarbleMachine
sudo rsync -av --delete $(pwd) /var/www/html/

# set sane web perms
echo "Ensuring Proper Web Permissions"
sudo chown -R www-data:www-data /var/www/html/MarbleMachine
sudo find /var/www/html/MarbleMachine -type d -exec chmod 755 {} \;
sudo find /var/www/html/MarbleMachine -type f -exec chmod 644 {} \;

echo "Configuring Apache Web Server..."
sudo sed -i -E 's#^[[:space:]]*DocumentRoot[[:space:]]+/var/www/html[[:space:]]*$#DocumentRoot /var/www/html/MarbleMachine#' /etc/apache2/sites-available/000-default.conf
sudo apache2ctl configtest && sudo systemctl restart apache2
