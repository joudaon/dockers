# Elastic APM Agent example

- [Elastic APM Agent example](#elastic-apm-agent-example)
  - [How to deploy](#how-to-deploy)
  - [Checking APM Agent on Kibana UI](#checking-apm-agent-on-kibana-ui)
  - [Useful linnks](#useful-linnks)

## How to deploy

```sh
# Start container
$> docker-compose up -d
```

## Checking APM Agent on Kibana UI

First of all we need to play with applications so visit either:
- Python flask application: `http://localhost:5000`
- Apache Tomcat java application: `http://localhost:8080/demo`

Then, go to Kibana UI:

`http://localhost:5601/app/apm`

We should see here the application metrics.

## Useful linnks

- [Demo Java Web App](https://github.com/tongueroo/demo-java)
- [APM Agents](https://www.elastic.co/guide/en/apm/agent/index.html)