# sonatype-nexus3
 
## TOC
 
- [sonatype-nexus3](#sonatype-nexus3)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)
    - [Persistent Data](#persistent-data)
  - [Repository information](#repository-information)
    - [Docker](#docker)
    - [File upload](#file-upload)
 
## Useful links
 
- [docker hub - sonatype/nexus3](https://hub.docker.com/r/sonatype/nexus3/)
- [github - sonatype/nexus3](https://github.com/sonatype/docker-nexus3)
- [Repository Manager 3](https://help.sonatype.com/repomanager3)
- [OSS vs PRO](https://www.sonatype.com/nexus-repository-oss-vs.-pro-features)
 
## Information
 
### Persistent Data
There are two general approaches to handling persistent storage requirements with Docker. See Managing Data in Containers for additional information.
 
Use a docker volume. Since docker volumes are persistent, a volume can be created specifically for this purpose. This is the recommended approach.
 
```sh
$ docker volume create --name nexus-data
$ docker run -d -p 8081:8081 --name nexus -v nexus-data:/nexus-data sonatype/nexus3
```
 
Mount a host directory as the volume. This is not portable, as it relies on the directory existing with correct permissions on the host. However it can be useful in certain situations where this volume needs to be assigned to certain specific underlying storage.
 
```sh
$ mkdir /some/dir/nexus-data && chown -R 200 /some/dir/nexus-data
$ docker run -d -p 8081:8081 --name nexus -v /some/dir/nexus-data:/nexus-data sonatype/nexus3
```
 
## Repository information
 
### Docker
 
To make Docker repository work, please follow these steps:
 
1. On Nexus web interface, set an HTTP connector in "Repository Connectors". A port must be set (5000 for example).
2. On docker-compose.yml file, expose the above port.
3. Update "/etc/docker/daemon.json" file and set our repository as insecure registry.
    ```json
    {
    "insecure-registries": [
        "http://<nexus-server-ip>:5000"
        ]
    }
    ```
4. Login into the docker repository:
  
    ```sh
    $> docker login -u <username> http://<nexus-server-ip>:5000
    ```

5. Pushing image

    ```sh
    $> docker pull hello-world
    $> docker tag hello-world:latest <nexusip>:5000/repository/docker-master/hello-world:latest
    $> docker push <nexusip>:5000/repository/docker-master/hello-world:latest
    ``` 

### File upload

Files can be uploaded from command line this way:

```sh
$> curl --fail -u admin:Password1234! --upload-file test.txt 'http://172.28.103.82:8081/repository/myrepository/'
```