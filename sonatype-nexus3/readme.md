# sonatype-nexus3
 
## TOC
 
- [sonatype-nexus3](#sonatype-nexus3)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)
    - [Persistent Data](#persistent-data)
 
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
