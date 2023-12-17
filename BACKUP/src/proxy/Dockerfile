FROM httpd:2.4

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

RUN mkdir -p /usr/local/apache2/conf/sites/

EXPOSE 80
EXPOSE 8081

CMD ["httpd", "-D", "FOREGROUND"]