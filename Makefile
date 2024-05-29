BUILD_DIR=./_build

INDEX=$(BUILD_DIR)/index.txt

ARCHIVES := $(wildcard packages/**/*.tgz)
PACKAGES := $(addprefix $(BUILD_DIR)/,$(ARCHIVES:.tgz=))

default: all

all: $(PACKAGES) | $(BUILD_DIR)

$(BUILD_DIR)/packages/%: packages/%.tgz | $(BUILD_DIR)
	@mkdir -p $(dir $@); \
	DIR=$$(tar tzf $< | sed -e 's@/.*@@' | uniq); \
	tar -xzf $< -C $(dir $@); \
	cp -Rp $(dir $@)$${DIR} $@; \
	rm -rf $(dir $@)$${DIR}; \
	echo $@ >> $(INDEX)

$(BUILD_DIR):
	@mkdir -p $@

verify:
	return 0

clean:
	rm -rf $(BUILD_DIR)

.PHONY: default init verify clean
