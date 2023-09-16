#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
	#Install Nginx if not installed
	sudo apt -y update
	sudo apt -y install nginx
	sudo ufw allow 'Nginx HTTP'
	sudo service nginx start
fi

# create /data/ folder
if [[ ! -d "/data/" ]]; then
	sudo mkdir /data/
fi

# create /data/web_static/ folder
if [[ ! -d "/data/web_static/" ]]; then
	sudo mkdir -p /data/web_static/
fi

# create /data/web_static/releases/
if [[ ! -d "/data/web_static/releases/" ]]; then
	suod mkdir -p /data/web_static/releases/
fi

# create /data/web_static/shared/
if [[ ! -d "/data/web_static/shared/" ]]; then
	sudo mkdir -p /data/web_static/shared/
fi

# create /data/web_static/releases/test/
if [[ ! -d "/data/web_static/releases/test/" ]]; then
	sudo mkdir -p /data/web_static/releases/test/
fi

# create a fake html file
echo "Welcome Mr Fabian!" | sudo tee /data/web_static/releases/test/index.html

# create a symlink
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Ownership of file
sudo chown -R ubuntu:ubuntu /data
sudo chown -R ubuntu:ubuntu /data/*

# using alias
sudo sed -i '53i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# restarting nginx
sudo service nginx restart
