#
.DEFAULT_GOAL:=	test
.PHONY:		deploy test

#
# Targets
deploy::
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:news-archive/
	ssh ${SSH_USER}@${SSH_HOST} 'cd news-archive && scripts/deploy.sh'

test::
	@true

-include GNUmakefile.local
