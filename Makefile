BUILD_DIR=./_build

default: init

init: | $(BUILD_DIR)
	@echo "Initializing ..."

$(BUILD_DIR):
	mkdir -p $@

verify:
	return 0

clean:
	rm -rf $(BUILD_DIR)

.PHONY: default init verify clean
