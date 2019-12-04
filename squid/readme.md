# squid

Squid is a caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. Squid has extensive access controls and makes a great server accelerator.

## TOC

- [squid](#squid)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [squid official site](http://www.squid-cache.org/)
- [Docker hub: squid](https://hub.docker.com/r/sameersbn/squid)
- [Github: squid](https://github.com/sameersbn/docker-squid)
- [How To Setup and Configure a Proxy Server – Squid Proxy](https://devopscube.com/setup-and-configure-proxy-server/)
- [How to Setup “Squid Proxy” Server on Ubuntu and Debian](https://www.tecmint.com/install-squid-in-ubuntu/)
- [Configuring Squid Proxy Server with Restricted Access and Setting Up Clients to Use Proxy – Part 5](https://www.tecmint.com/configure-squid-server-in-linux/)
- [ERR_ACCESS_DENIED: No access by default](https://github.com/sameersbn/docker-squid/issues/59)
- [squid logs](https://wiki.squid-cache.org/SquidFaq/SquidLogs)
- [How Squid ACLs work](https://workaround.org/squid-acls/)

## Information

```sh
# Test if the proxy server is working using a simple curl request
$> curl -x http://<squid-proxy-server-IP>:3128  -L http://google.com
```
