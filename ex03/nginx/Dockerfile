FROM nginx

RUN rm -f /etc/nginx/conf.d/default.conf
COPY /conf/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
