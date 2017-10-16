FACTIONS = Tao Robot_Legions

TEX := $(foreach d,$(FACTIONS),$(wildcard $(d)/*.tex))
PDF := $(TEX:.tex=.pdf)

CLEAN := $(foreach d,$(FACTIONS),$(wildcard $(d)/*.csv) $(wildcard $(d)/*.pdf))

define add_dep =
$(1): $(2)
endef

all: $(PDF)

clean: $(CLEAN)
	@echo Removing $(CLEAN)
	@rm -f $(CLEAN)

%.pdf : %.tex
	@rm -f $(@D)/*.csv
	@python3 onepagebatch.py $(@D)
	@cd $(@D) && xelatex -interaction=batchmode -halt-on-error $(notdir $<)

# add dependency to all json found in faction directory
$(foreach d,$(FACTIONS),$(eval $(call add_dep,$(d)/$(d).pdf,$(wildcard $(d)/*.json))))
