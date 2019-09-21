
- [Key Features](#key-features)
- [Keeping up to date](#keeping-up-to-date)
- [Installation](#installation)
- [Upgrading](#upgrading)
- [Other repositories](#other-repositories)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)
- [Useful links](#useful-links)

## Steps

1. Download install-lt from (here)[http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz]
2. tar -xzvf install-tl-unx.tar.gz
3. ./install-tl-20190507/install-tl then (ret meand the return key) press D ret 1 ret ~/sharelatex_texlive/2019 ret R ret I ret
4. wait for the installation to finish, depends on your internet connection how long it takes.
5. the docker-compose.yml, under volumes:, i use - ~/sharelatex_texlive:/usr/local/texlive and inside environment: I added: PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/texlive/2019/bin/x86_64-linux/
6. docker-compose down && docker-compose up -d inside my sharelatex dir where the docker-compose.yml file is.
7. docker exec sharelatex lualatex --version to check if it uses the correct version.

## Useful links

- [Host Your Own LaTeX Server](https://medium.com/@shuangzizuobh2/host-your-own-latex-server-a-docker-example-2787531bf93b)
- [Overleaf - A web-based collaborative LaTeX editor](https://github.com/overleaf/overleaf)
- [docker image](https://github.com/overleaf/docker-image)
- [Update TexLive to 2018](https://github.com/overleaf/overleaf/issues/601)
