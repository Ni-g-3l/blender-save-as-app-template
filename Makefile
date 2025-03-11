EXTENSION_VERSION = $(shell cat $(CURDIR)/extension_save_as_app_template/blender_manifest.toml | sed -n 's/.*version = "\([^"]*\)".*/\1/p' | tail -n 1)

env:
	@echo "------------------- INSTALL DEV ENV ------------------- "
	mkdir $(CURDIR)/.build -p
	blender --command extension repo-add --name extension_save_as_app_template --directory $(CURDIR)/.build --clear-all extension_save_as_app_template
	ln $(CURDIR)/extension_save_as_app_template $(CURDIR)/.build/extension_save_as_app_template -s
	@echo "------------------------------------------------------- "

run:
	@echo "--------------------- RUN BLENDER --------------------- "
	@blender

deploy:release
	@echo "------------------- DEPLOY EXTENSION -------------------- "
	@echo Deploying ${EXTENSION_VERSION} version
	@git push --tags
	@gh release create ${EXTENSION_VERSION} $(CURDIR)/dist/extension_save_as_app_template-${EXTENSION_VERSION}.zip --generate-notes --latest 
	@echo "------------------------------------------------------- "

release:build clean
	@echo "------------------- RELEASE EXTENSION ------------------- "
	@echo Releasing ${EXTENSION_VERSION} version
	@git tag ${EXTENSION_VERSION} || echo "Tag already exists."
	@echo "------------------------------------------------------- "

build: clean
	@echo "-------------------- BUILD EXTENSION -------------------- "
	mkdir -p $(CURDIR)/dist
	blender --command extension build --source-dir $(CURDIR)/dummy_extension --output-dir $(CURDIR)/dist/ --verbose
	@echo "------------------------------------------------------- "

clean:
	@echo "-------------------- CLEAN EXTENSION -------------------- "
	find $(CURDIR) -name \*.py[ocd] -delete
	find $(CURDIR) -name __pycache__ -delete
	@echo "------------------------------------------------------- "

test:
	@echo "---------------------- RUN TESTS ---------------------- "
	python3 -m unittest discover tests
	@echo "------------------------------------------------------- "
