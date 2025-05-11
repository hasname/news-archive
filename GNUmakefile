#
.DEFAULT_GOAL:=	help
.PHONY:		db deploy help lint test

#
# Targets
db::		# Upgrade (or initialize if not existed) database
	uv run --python pypy3 alembic upgrade head

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
