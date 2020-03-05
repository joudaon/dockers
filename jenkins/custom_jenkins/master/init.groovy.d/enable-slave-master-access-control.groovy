#!/usr/bin/env groovy

import jenkins.security.s2m.AdminWhitelistRule
import jenkins.model.Jenkins

println "--> Enabling slave master access control"

Jenkins.instance.getInjector().getInstance(AdminWhitelistRule.class)
.setMasterKillSwitch(false)

Jenkins.instance.save()