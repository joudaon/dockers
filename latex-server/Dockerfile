FROM sharelatex/sharelatex:latest

RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \
        mkdir /install-tl-unx; tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1
RUN echo "selected_scheme scheme-full" >> /install-tl-unx/texlive.profile; \
        /install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile; \
        rm -r /install-tl-unx; rm install-tl-unx.tar.gz
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/texlive/2019/bin/x86_64-linux/
WORKDIR /usr/local/texlive/2019/bin/x86_64-linux
RUN ./tlmgr install latexmk ; \
    ./tlmgr install texcount
RUN rm -rf /usr/local/texlive/2017
