%.build:
	@if [ -d $* ]; then \
		echo "Building Docker image $(USER)/centos$*:"; \
		docker build -t $(USER)/centos$* ./$*; \
	else \
		echo "Error: No such directory exists: $*!"; \
	fi
