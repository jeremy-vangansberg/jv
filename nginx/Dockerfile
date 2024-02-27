FROM nginx:latest
RUN apt-get update && apt-get install -y procps
RUN mkdir -p /home/app/staticfiles
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY staticfiles/ /home/app/