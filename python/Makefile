all: init proto-gen build

init:
	@echo "Pull External Protofiles"
	git submodule init
	git submodule update --remote

#@echo "Install dependencies"
#npm i

# do not format. we uses just auto-generated ones.
#format: 
#	npm run format

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

proto-gen: 
	@echo "Generating Protobuf files"
	./scripts/proto-gen.sh

build: 
	poetry build

publish:
	poetry publish

.PHONY: all proto-gen format init build publish
