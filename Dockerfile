# copied from https://www.cloudways.com/blog/docker-php-application/

FROM php:7.4-apache

# Install the MySQL extension
RUN docker-php-ext-install mysqli
#        /usr/local/bin/docker-php-ext-install -j5 gd mbstring mysqli pdo pdo_mysql shmop
RUN docker-php-ext-install -j5 mysqli pdo pdo_mysql

# Create a directory for your application code
WORKDIR /var/www/html

# Copy the application code into the container
COPY ./ /var/www/html

# == riccardo note ==
# Cloud Run says: "We recommend that you listen on $PORT instead of this specific number."
# But if I change 80 to 8080 Apache won't just pick it up from here, I need to specify in a non-standard apache config
# =>  Too much hussle.

# Expose port 80 for web traffic
EXPOSE 80

# added per Clod Run
# https://stackoverflow.com/questions/59324794/google-cloud-run-port
ENV PORT 80
