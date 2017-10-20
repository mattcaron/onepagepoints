FACTIONS = Tao Robot_Legions High_Elf_Fleets

TEX := $(foreach d,$(FACTIONS),$(wildcard $(d)/*.tex))
TEMPLATE := $(wildcard template/*.sty)
PDF := $(TEX:.tex=.pdf)
OUT_PDF := $(addprefix out/,$(notdir $(PDF)))
PYTHONS := $(wildcard *.py)

CLEAN := $(foreach d,$(FACTIONS),$(wildcard $(d)/*.csv) $(wildcard $(d)/*.pdf))

define add_dep =
$(1): $(2)
endef

define copy_out =
$(1): $(2)
	@cp $$< $$@
endef

all: $(OUT_PDF)

clean: $(CLEAN)
	@echo Removing $(CLEAN)
	@rm -f $(CLEAN)
	@rm -rf out

indent:
	@python3 indentjson.py $(FACTIONS)

out:
	@mkdir out

# pdf dependency is the tex file, all faction json files, all python scripts, and latex templates
%.pdf : %.tex $(PYTHONS) $(TEMPLATE) | out
	@rm -f $(@D)/*.csv
	@python3 onepagebatch.py $(@D)
	@cd $(@D) && xelatex -interaction=batchmode -halt-on-error $(notdir $<)

# copy all pdf to out/ directory
$(foreach f,$(PDF),$(eval $(call copy_out,$(addprefix out/,$(notdir $(f))),$(f))))

# add dependency to all json found in faction directory
$(foreach d,$(FACTIONS),$(eval $(call add_dep,$(d)/$(d).pdf,$(wildcard $(d)/*.json))))
