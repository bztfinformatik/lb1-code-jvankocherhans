FROM httpd:2.4

MAINTAINER s3rp3nt kocherhansjvan@gmail.com

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

RUN mkdir -p /usr/local/apache2/conf/sites/

EXPOSE 80
EXPOSE 443

CMD ["httpd", "-D", "FOREGROUND"]