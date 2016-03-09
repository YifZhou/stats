(TeX-add-style-hook
 "hw1"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "paper=letter" "fontsize=11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("babel" "english") ("listings" "procnames") ("xcolor" "dvipsnames")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "scrartcl"
    "scrartcl10"
    "fontenc"
    "times"
    "babel"
    "amsmath"
    "amsfonts"
    "amsthm"
    "bm"
    "enumitem"
    "graphicx"
    "natbib"
    "sectsty"
    "fancyhdr"
    "listings"
    "color"
    "xcolor")
   (TeX-add-symbols
    '("ddfrac" 2)
    '("gray" 1)
    '("horrule" 1)
    "epsi"
    "dd")
   (LaTeX-add-labels
    "eqn:binom"
    "sec:-3"
    "sec:-1")
   (LaTeX-add-bibliographies
    "ref")
   (LaTeX-add-color-definecolors
    "keywords"
    "comments"
    "red"
    "green")))

