#
.DEFAULT_GOAL:=	help
.PHONY:		db deploy help lint syntax test

#
# Targets
db::		# Upgrade (or initialize if not existed) database
	uv run --python pypy3 alembic upgrade head

deploy:: syntax lint	# Deploy
	rsync -Favz --delete-after ./ ${SSH_USER}@${SSH_HOST}:news-archive/
	ssh ${SSH_USER}@${SSH_HOST} 'cd news-archive && scripts/deploy.sh'

help::		# Show this help
	@grep -E '^[a-zA-Z_-]+::' GNUmakefile | sort | awk -F'[:#]' '{print $$1 ":\t" $$NF}'

lint::		# Run linter
	uv run --python pypy3 ruff check

syntax::	# Check syntax
	uv run --python pypy3 -m py_compile daemon/*.py web/*.py

test::		# Run test cases
	@true

-include GNUmakefile.local
