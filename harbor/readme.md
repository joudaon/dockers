# Harbor

## What is Harbor?

Harbor is an open source cloud native registry that stores, signs, and scans container images for vulnerabilities.

Harbor solves common challenges by delivering trust, compliance, performance, and interoperability. It fills a gap for organizations and applications that cannot use a public or cloud-based registry, or want a consistent experience across clouds.

Harbor extends the open source Docker Distribution by adding the functionalities usually required by users such as security, identity and management. Having a registry closer to the build and run environment can improve the image transfer efficiency. Harbor supports replication of images between registries, and also offers advanced security features such as user management, access control and activity auditing.

## Useful links

- [Installation and Configuration Guide](https://github.com/goharbor/harbor/blob/master/docs/installation_guide.md)

## Steps

1. Download online or offline installer from https://github.com/goharbor/harbor/releases

2. Extract the packages

    ```sh
    $ tar xvf harbor-offline-installer-<version>.tgz
    $ tar xvf harbor-online-installer-<version>.tgz
    ```

3. Configure 'harbor.yml'

    Key values:

    | key | value | description  |
    | ----| ----- | ------------ |
    | hostname | 0.0.0.0 | The IP address or hostname to access admin UI and registry service. |
    | harbor_admin_password | Password1234! | The initial password of Harbor admin. |
    | password | Password1234! | The password for the root user of Harbor DB. Change this before any production use. |
    | data_volume | ./data | By default, registry data is persisted in the host's /data/ directory. This data remains unchanged even when Harbor's containers are removed and/or recreated, you can edit the data_volume in harbor.yml file to change this directory.
    | location | ./log/harbor |  Harbor uses rsyslog to collect the logs of each container. By default, these log files are stored in the directory /var/log/harbor/ on the target host for troubleshooting, also you can change the log directory in harbor.yml. |

4. Start Harbor using the install.sh script

    ```sh
    $ sudo ./install.sh
    ```

5. If everything worked properly, you should be able to open a browser to visit the admin portal at http://reg.yourdomain.com (change reg.yourdomain.com to the hostname configured in your harbor.yml). Note that the default administrator username/password are admin/Harbor12345.