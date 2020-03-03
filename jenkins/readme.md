# Jenkins

## Useful links

- [Continuous Integration with Jenkins and Docker](https://code-maze.com/ci-jenkins-docker/)
- [docker-series](https://github.com/CodeMazeBlog/docker-series/tree/docker-series-continuous-integration-jenkins-end/jenkins-docker)
- [Official Jenkins Docker image](https://github.com/jenkinsci/docker/blob/master/README.md)
- [jenkins official docker image](https://hub.docker.com/r/jenkins/jenkins)
- [jenkins docker-compose example](https://github.com/istresearch/jenkins/blob/master/docker-compose.yml)
- [docker-compose Jenkins with persistent data](https://codeandunicorns.com/docker-compose-jenkins-persistent-data/)
- [jenkins-base](https://github.com/fabric8io/jenkins-base)
- [github - Official Jenkins Docker image](https://github.com/jenkinsci/docker/blob/master/README.md)
- [How to run and upgrade Jenkins using the official Docker image](https://batmat.net/2018/09/07/how-to-run-and-upgrade-jenkins-using-the-official-docker-image/)
- [New Jenkins Container And Update Jenkins (Docker)](https://medium.com/@jimkang/how-to-start-a-new-jenkins-container-and-update-jenkins-with-docker-cf628aa495e9)
- [Continuous Integration with Jenkins and Docker](https://code-maze.com/ci-jenkins-docker/)
- [docker-jenkins](https://github.com/foxylion/docker-jenkins)
- [jenkins-bootstrap-shared](https://github.com/samrocketman/jenkins-bootstrap-shared/tree/master/scripts)
- [Jenkins Docker image](https://github.com/thbkrkr/jks)
- [Groovy Hook Script and Jenkins Configuration as Code](http://tdongsi.github.io/blog/2017/12/30/groovy-hook-script-and-jenkins-configuration-as-code/)

## Information:
To mount volume special permissions need to be added:

NOTE: Avoid using a bind mount from a folder on the host machine into /var/jenkins_home, as this might result in file permission issues (the user used inside the container might not have rights to the folder on the host machine). If you really need to bind mount jenkins_home, ensure that the directory on the host is accessible by the jenkins user inside the container (jenkins user - uid 1000) or use -u some_other_user parameter with docker run.

docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
this will run Jenkins in detached mode with port forwarding and volume added. You can access logs with command 'docker logs CONTAINER_ID' in order to check first login token. ID of container will be returned from output of command above.

```sh
$ sudo mkdir jenkins_home
$ sudo chmod 777 jenkins_home/
```

## Getting installed plugins

In Jenkins "Script Console" type the following:

```groovy
Jenkins.instance.pluginManager.plugins.each{
  plugin -> 
    println ("${plugin.getDisplayName()} (${plugin.getShortName()}): ${plugin.getVersion()}")
}
```

