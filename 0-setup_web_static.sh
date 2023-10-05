#!/usr/bin/env bash
# Sets up web servers for the deployment of `web_static`

# Install NGINX if not already installed
sudo apt update
sudo apt install -y nginx

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file to test the configuration
echo "
<html>
  <head></head>
  <body>
     Holberton School!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symlink `/data/web_static/current` linked to `/data/web_static/releases/test/`
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/ to `ubuntu` user and group, recursively
sudo chown -R ubuntu:ubuntu /data/

# Set up the server to server `hbnb_static`
printf %s "server {
       listen 80 default_server;
       listen [::]:80 default_server;

       add_header X-Served-By $HOSTNAME;

       root /var/www/html;
       index index.html;

       location /hbnb_static/ {
           alias /data/web_static/current/;
       }

       location /redirect_me {
           return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
       }

       error_page 404 /err_404.html;
       location /err_404.html {
           root /var/www/html;
	   internal;
       }
}" | sudo tee /etc/nginx/sites-available/default

# Reload the configuration
sudo service nginx restart
