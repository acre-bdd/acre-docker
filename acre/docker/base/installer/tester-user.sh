[ -z $1 ] || export USER_ID=$1
USER_ID=${USER_ID:-9001}
echo USER_ID is $USER_ID
adduser --uid $USER_ID --disabled-password --gecos '' tester
addgroup sudo
adduser tester sudo
echo '%sudo ALL=(ALL) NOPASSWD: ALL' >/etc/sudoers
