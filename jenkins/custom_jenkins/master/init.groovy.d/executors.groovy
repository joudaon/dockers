#!/usr/bin/env groovy

import jenkins.model.*

println "--> Updating executors"

Jenkins.instance.setNumExecutors(1)