# custom_jenkins

## Set up environment

Create `jenkins_home` folder on master node.

```sh
$ sudo mkdir master/jenkins_home
$ sudo chmod 777 master/jenkins_home
```

Update `env` variables as desired.

Deploy the environment.

```sh
$ docker-compose up -d
```

## Clean up environment

Stop and remove docker containers.

```sh
$ docker-compose down
```

Remove `jenkins_home` folder.

```sh
$ sudo rm -rf master/jenkins_home ssh-slave/home
```

## Connecting slaves (ssh-slave)

- In the Jenkins Master UI, go to: Manage Jenkins / Nodes / Add new node
- Add your host (hostname = jenkins-ssh-slave) with credentials: user-root / password jenkins
