FROM alpine:latest as builder
WORKDIR /app
COPY index.html .
RUN sed -i 's/Hello/Goodbye/g' index.html

FROM nginx
EXPOSE 80
COPY --from=builder /app/index.html /usr/share/nginx/html
