(TeX-add-style-hook
 "hw2"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "paper=letter" "fontsize=11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("babel" "english")))
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
    "graphicx"
    "siunitx"
    "sectsty"
    "fancyhdr")
   (TeX-add-symbols
    '("ppfrac" 2)
    '("ddfrac" 2)
    '("horrule" 1)
    "dd")))

