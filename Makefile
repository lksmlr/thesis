THESIS=thesis

.SUFFIXES:
.SUFFIXES: .bib .pdf .tex
.PHONY: clean

run: $(THESIS).pdf

deploy:
	pdflatex -shell-escape $(THESIS).tex
	bibtex $(THESIS)
	pdflatex -shell-escape $(THESIS).tex
	pdflatex -shell-escape $(THESIS).tex
	$(MAKE) clean


$(THESIS).pdf: SB_0050_FO $(THESIS).bbl $(THESIS).tex
	pdflatex $(THESIS).tex -draftmode
	pdflatex $(THESIS).tex 

SB_0050_FO:
	@test -s SB_0050_FO_Pruefungsrechtliche_Erklaerung_und_Erklaerung_zur_Veroeffentlichung_der_Abschlussarbeit_public.pdf || { \
	echo ""; \
	echo "*************************************************************************************"; \
	echo "* You need to download, fill and save-as-pdf form SB_0050_FO from the Ohm intranet. *"; \
	echo "*************************************************************************************"; \
	echo "wget https://intern.ohmportal.de/fileadmin/Gelenkte_Doks/Abt/SZS/SB/SB_0050_FO_Pruefungsrechtliche_Erklaerung_und_Erklaerung_zur_Veroeffentlichung_der_Abschlussarbeit_public.pdf"; \
	echo ""; \
	exit 1; \
	}

$(THESIS).bbl: $(THESIS).aux
	bibtex $(THESIS).aux

$(THESIS).aux: refs.bib
	pdflatex $(THESIS).tex -draftmode
	pdflatex $(THESIS).tex -draftmode

clean:
	-del /s /q *.aux *.lof *.log *.lot *.lol *.bcf *.toc *.bbl *.blg *.run.xml *.out *.xmpi *.xmpdata *.minted