# jfrog-artifactory-oss

## TOC

- [jfrog-artifactory-oss](#jfrog-artifactory-oss)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Installing Artifactory with Docker](https://www.jfrog.com/confluence/display/RTF/Installing+with+Docker)
- [Artifactory Docker Compose Examples](https://github.com/jfrog/artifactory-docker-examples/tree/master/docker-compose/artifactory)
- [Artifactory docker versions](https://bintray.com/jfrog/reg2/jfrog%3Aartifactory-oss)
- [Artifactory versions](https://bintray.com/jfrog/product/JFrog-Artifactory-Oss/view)

## Information

Before starting run the prepareHostEnv.sh script as root. This will create the required folers.

```sh
$> ./prepareHostEnv.sh -t oss -d ./data
```

How do I login to Artifactory for the first time? What are the default admin username and password?
Artifactory comes with a pre-configured default "admin" account. Username: admin, Password: password.

