# Use an official PHP image with Apache

# Pull a suitable php image
FROM php:7.4-apache

# Install required PHP extensions: PDO, MySQL, and other dependencies
RUN docker-php-ext-install pdo pdo_mysql 

# Set working directory inside the container
WORKDIR /var/www/html

# Copy all application files into the container
COPY . /var/www/html

# Set environment variables for database connection
ENV DB_HOST="localhost"
ENV DB_NAME="image_catalog"
ENV DB_USER="appmod-phpapp-user"
ENV DB_PASS="strongstrongpassword"


# Configure Apache to listen on port 8080. Use sed command to change the default listening port.
ENV APACHE_LISTEN_PORT=8080
RUN sed -ri -e 's/Listen 80/Listen ${APACHE_LISTEN_PORT}/' /etc/apache2/ports.conf \
    -e 's/Listen 80/Listen ${APACHE_LISTEN_PORT}/' /etc/apache2/sites-available/000-default.conf

#Expose to port 8080
EXPOSE 8080

# Start Apache in the foreground
CMD ["apache2-foreground"]
