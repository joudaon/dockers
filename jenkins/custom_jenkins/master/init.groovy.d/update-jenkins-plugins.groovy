#!/usr/bin/env groovy

println "--> Updating jenkins plugins"

jenkins.model.Jenkins.getInstance().getUpdateCenter().getSites().each { site ->
  site.updateDirectlyNow(hudson.model.DownloadService.signatureCheck)
}

hudson.model.DownloadService.Downloadable.all().each { downloadable ->
  downloadable.updateNow();
}

def plugins = jenkins.model.Jenkins.instance.pluginManager.activePlugins.findAll {
  it -> it.hasUpdate()
}.collect {
  it -> it.getShortName()
}

println "Plugins to upgrade: ${plugins}"
long count = 0

jenkins.model.Jenkins.instance.pluginManager.install(plugins, false).each { f ->
  f.get()
  println "${++count}/${plugins.size()}.."
}

if(plugins.size() != 0 && count == plugins.size()) {
  jenkins.model.Jenkins.instance.safeRestart()
}