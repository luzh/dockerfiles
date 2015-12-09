WORK_IMAGE = python2.7-imaging

# Build a "python" image that contains the most relevant tools for work.
python: dockerfile
	docker build -t python .

# Adding a user is mainly for using the X11 socket on the local host for GUI.
dockerfile:
	@echo "FROM $(USER)/$(WORK_IMAGE)" > Dockerfile
	@echo "RUN useradd --shell /bin/bash --create-home $(USER) \\" >> Dockerfile
	@echo " && usermod --uid $(shell id -u $(USER)) $(USER) \\" >> Dockerfile
	@echo " && groupmod --gid $(shell id -g $(USER)) $(USER)" >> Dockerfile
	@echo "USER $(USER)" >> Dockerfile
	@echo "--- Dockerfile Created ---"
	@cat Dockerfile

%.build:
	@if [ -d $* ]; then \
		echo "Building Docker image $(USER)/python2.7-$*:"; \
		docker build -t $(USER)/python2.7-$* ./$*; \
	else \
		echo "Error: No such directory exists: $*!"; \
	fi

%.test:
	@if [ -d $* ]; then \
		echo "Testing Docker image $(USER)/python2.7-$*:"; \
		if [[ $* == imaging || $* == wxpython ]]; then \
			if [ -z "$(DISPLAY)" ]; then \
				echo "Error: DISPLAY is not set, needed by python2.7-imaging and python2.7-wxpython!"; \
			else \
				xhost +si:localuser:root; \
				docker run --rm -e DISPLAY=$(DISPLAY) -v /tmp/.X11-unix:/tmp/.X11-unix -v $(PWD):$(PWD) -w $(PWD) $(USER)/python2.7-$* $(PWD)/$*/imagetest.py; \
				xhost -si:localuser:root; \
			fi \
		else \
			docker run --rm -v $(PWD):$(PWD) -w $(PWD) $(USER)/python2.7-$* $(PWD)/$*/imagetest.py; \
		fi \
	else \
		echo "Error: No such directory exists: $*!"; \
	fi
