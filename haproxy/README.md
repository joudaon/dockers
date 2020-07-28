# HAProxy

HAProxy is a free, open source high availability solution, providing load balancing and proxying for TCP and HTTP-based applications by spreading requests across multiple servers. It is written in C and has a reputation for being fast and efficient (in terms of processor and memory usage).

In this example we are going to create two identical Apache servers and one HAProxy container. When we want to access our website, we will be calling HAProxy, not the Apache servers. HAProxy will divert traffic to Apache servers in "round-robin" fashion.

## Flow

1. Request goes to HAProxy container.
2. HAProxy container calls either Apache container 1 or 2.
3. Response is served by Apache container 1 or 2.

## Testing load balacing via curl

```sh
$> for i in {1..10}; do curl 192.168.0.33:80 && echo ;  done

Serving from Apache Server 1
Serving from Apache Server 2
Serving from Apache Server 1
Serving from Apache Server 2
```

## Useful links

- [haproxy - docker hub](https://hub.docker.com/_/haproxy)
- [Creating a single HAProxy and two Apache containers with Docker compose](http://www.inanzzz.com/index.php/post/w14j/creating-a-single-haproxy-and-two-apache-containers-with-docker-compose)