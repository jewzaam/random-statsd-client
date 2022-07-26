SHELL := /usr/bin/env bash

IMAGE_REGISTRY ?= quay.io
IMAGE_REPOSITORY ?= nmalik

# Accommodate docker or podman
CONTAINER_ENGINE=$(shell command -v podman 2>/dev/null || command -v docker 2>/dev/null)

CURRENT_COMMIT=$(shell git rev-parse --short=7 HEAD)
IMAGE_TAG=$(CURRENT_COMMIT)
IMAGE_NAME=random-statsd-client
IMAGE_URI=$(IMAGE_REGISTRY)/$(IMAGE_REPOSITORY)/$(IMAGE_NAME):$(IMAGE_TAG)
IMAGE_URI_LATEST=$(IMAGE_REGISTRY)/$(IMAGE_REPOSITORY)/$(IMAGE_NAME):latest


.PHONY: image-build
image-build:
	$(CONTAINER_ENGINE) build . -f build/Dockerfile -t $(IMAGE_URI)

.PHONY: image-test
image-test:
	$(CONTAINER_ENGINE) run -it --rm $(IMAGE_URI)

.PHONY: image-push
image-push:
	$(CONTAINER_ENGINE) tag $(IMAGE_URI) $(IMAGE_URI_LATEST)
	$(CONTAINER_ENGINE) push $(IMAGE_URI)
	$(CONTAINER_ENGINE) push $(IMAGE_URI_LATEST)
