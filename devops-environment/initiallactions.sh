echo "--> configuring jenkins"
mkdir -p storeddata/jenkins_home
chmod -R 777 storeddata/jenkins_home/
echo "--> configuring nexus"
mkdir -p storeddata/nexus-data && chown -R 200 storeddata/nexus-data
echo "--> configuring sonarqube"
mkdir -p storeddata/sonarqube/sonarqube_conf storeddata/sonarqube/sonarqube_data storeddata/sonarqube/sonarqube_extensions storeddata/sonarqube/sonarqube_bundled-plugins storeddata/postgresql/postgresql storeddata/postgresql/postgresql_data
chmod -R 777 storeddata/sonarqube/sonarqube_conf storeddata/sonarqube/sonarqube_data storeddata/sonarqube/sonarqube_extensions storeddata/sonarqube/sonarqube_bundled-plugins storeddata/postgresql/postgresql storeddata/postgresql/postgresql_data
