#
.DEFAULT_GOAL:=	help
.PHONY:		deploy help lint test

#
# Targets
deploy::	# Deploy
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:news-archive/
	ssh ${SSH_USER}@${SSH_HOST} 'cd news-archive && scripts/deploy.sh'

help::		# Show this help
	@grep -E '^[a-zA-Z_-]+::' GNUmakefile | sort | awk -F'[:#]' '{print $$1 ":\t" $$NF}'

lint::		# Run linter
	uv run --python pypy3 ruff check

test::		# Run test cases
	@true

-include GNUmakefile.local
