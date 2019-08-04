# Jenkins

## Useful links

- [Continuous Integration with Jenkins and Docker](https://code-maze.com/ci-jenkins-docker/)
- [docker-series](https://github.com/CodeMazeBlog/docker-series/tree/docker-series-continuous-integration-jenkins-end/jenkins-docker)
- [Official Jenkins Docker image](https://github.com/jenkinsci/docker/blob/master/README.md)
- [jenkins official docker image](https://hub.docker.com/r/jenkins/jenkins)
- [jenkins docker-compose example](https://github.com/istresearch/jenkins/blob/master/docker-compose.yml)
- [docker-compose Jenkins with persistent data](https://codeandunicorns.com/docker-compose-jenkins-persistent-data/)
- [jenkins-base](https://github.com/fabric8io/jenkins-base)


## Information:
To mount volume special permissions need to be added:

NOTE: Avoid using a bind mount from a folder on the host machine into /var/jenkins_home, as this might result in file permission issues (the user used inside the container might not have rights to the folder on the host machine). If you really need to bind mount jenkins_home, ensure that the directory on the host is accessible by the jenkins user inside the container (jenkins user - uid 1000) or use -u some_other_user parameter with docker run.

docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
this will run Jenkins in detached mode with port forwarding and volume added. You can access logs with command 'docker logs CONTAINER_ID' in order to check first login token. ID of container will be returned from output of command above.

```sh
$ sudo mkdir jenkins_home
$ sudo chmod 777 jenkins_home/
```
