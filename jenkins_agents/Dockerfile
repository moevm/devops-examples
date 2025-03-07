FROM jenkins/jenkins:lts

USER root
RUN apt update && apt install -y vim ranger mc && echo ' \
alias ls="ls --color=auto"\n \
PS1="\e[33m$PS1\e[0m" ' >> /etc/bash.bashrc
USER jenkins
