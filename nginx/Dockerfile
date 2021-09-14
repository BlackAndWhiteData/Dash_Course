FROM nginx:latest

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx

CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]