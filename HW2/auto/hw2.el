(TeX-add-style-hook
 "hw2"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "paper=letter" "fontsize=11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("babel" "english") ("listings" "procnames") ("xcolor" "dvipsnames") ("pdfpages" "final")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl10"
    "fontenc"
    "fouriernc"
    "babel"
    "amsmath"
    "amsfonts"
    "amsthm"
    "bm"
    "graphicx"
    "siunitx"
    "sectsty"
    "fancyhdr"
    "listings"
    "color"
    "xcolor"
    "pdfpages")
   (TeX-add-symbols
    '("pfrac" 2)
    '("gaussian" 1)
    '("ppfrac" 2)
    '("ddfrac" 2)
    '("horrule" 1)
    "dd"
    "ux"
    "uy")
   (LaTeX-add-labels
    "fig:2b"
    "fig:Jacobian"
    "fig:Bayesian")
   (LaTeX-add-color-definecolors
    "keywords"
    "comments"
    "red"
    "green")))

