#!/usr/bin/env groovy

import jenkins.model.JenkinsLocationConfiguration

println "--> Setting up jenkins root url"

jlc = JenkinsLocationConfiguration.get()
jlc.setUrl("http://localhost/") 
println(jlc.getUrl())
jlc.save()
