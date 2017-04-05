FROM python:3.6

RUN apt update \
    && apt install build-essential \
             chrpath \
             libssl-dev \
             libxft-dev \
             libfreetype6 \
             libfreetype6-dev \
             libfontconfig1 \
             libfontconfig1-dev -y \
    && cd ~ \
    && export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" \
    && wget https://github.com/Medium/phantomjs/releases/download/v2.1.1/$PHANTOM_JS.tar.bz2 \
    && tar xvjf $PHANTOM_JS.tar.bz2 \
    && mv $PHANTOM_JS /usr/local/share \
    && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \
    && phantomjs --version \
    && apt-get clean \
    && pip install urllib3==1.13.1 \
                selenium==3.0.2

ENV APPLICATION_ROOT /app/
RUN mkdir $APPLICATION_ROOT
ADD . $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT
