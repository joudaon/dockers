# baget

BaGet (pronounced "baguette") is a lightweight NuGet and symbol server. It is open source, cross-platform, and cloud ready!

## TOC

- [baget](#baget)
  - [TOC](#toc)
  - [Uploading nuget package](#uploading-nuget-package)
  - [Useful links](#useful-links)

## Uploading nuget package

```powershell
&> dotnet nuget push -s http://<ip>:<port>/v3/index.json -k apitoken <nugetpackage>
&> dotnet nuget push -s http://localhost:8085/v3/index.json -k 1111 *.nupkg
```

## Useful links
- [BaGet github](https://github.com/loic-sharma/BaGet)
- [Create your own NuGet server and package feed](https://medium.com/@onurvatan/net-core-custom-nuget-server-baget-on-docker-b763a3c7a276)
- [BaGet](https://loic-sharma.github.io/BaGet/#running-baget-on-docker)
- [BaGet docker-hub](https://hub.docker.com/r/loicsharma/baget)
