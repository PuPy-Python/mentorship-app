FROM python:3.6.6

# install OS-level dependencies
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  apt-transport-https \
  python-dev \
  python-pip \
  postgresql-client

# install pip
RUN pip install pipenv

# nvm environment variables
RUN mkdir /root/.nvm
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 8.9.4

# install nvm
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION

# set paths
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install yarn -y
