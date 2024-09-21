BUILD_DIR=./_build

INDEX=$(BUILD_DIR)/index.json

ARCHIVES := $(wildcard packages/**/**/*.tgz)
PACKAGES := $(addprefix $(BUILD_DIR)/,$(ARCHIVES:.tgz=))

default: all

all: unpack index validate

unpack: $(PACKAGES)

index: $(INDEX)

$(INDEX):
	@./index_build.py $@

$(BUILD_DIR)/packages/%: packages/%.tgz | $(BUILD_DIR)
	@mkdir -p $(dir $@); \
	DIR=$$(tar tzf $< | sed -e 's@/.*@@' | uniq); \
	tar -xzf $< -C $(dir $@); \
	cp -Rp $(dir $@)$${DIR} $@; \
	rm -rf $(dir $@)$${DIR}

$(BUILD_DIR):
	@mkdir -p $@

validate: $(INDEX)
	@./index_validate.py $^

clean:
	rm -rf $(BUILD_DIR)

.PHONY: default all unpack index validate clean
