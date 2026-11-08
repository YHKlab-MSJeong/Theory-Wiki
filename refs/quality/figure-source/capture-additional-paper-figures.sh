#!/usr/bin/env bash
set -euo pipefail

lee_pdf=${1:?usage: capture-additional-paper-figures.sh LEE_PDF OMM_PDF AFZALIAN_PDF CARRILLO_PDF DFTBPLUS_PDF OUTPUT_DIR}
omm_pdf=${2:?usage: capture-additional-paper-figures.sh LEE_PDF OMM_PDF AFZALIAN_PDF CARRILLO_PDF DFTBPLUS_PDF OUTPUT_DIR}
afzalian_pdf=${3:?usage: capture-additional-paper-figures.sh LEE_PDF OMM_PDF AFZALIAN_PDF CARRILLO_PDF DFTBPLUS_PDF OUTPUT_DIR}
carrillo_pdf=${4:?usage: capture-additional-paper-figures.sh LEE_PDF OMM_PDF AFZALIAN_PDF CARRILLO_PDF DFTBPLUS_PDF OUTPUT_DIR}
dftbplus_pdf=${5:?usage: capture-additional-paper-figures.sh LEE_PDF OMM_PDF AFZALIAN_PDF CARRILLO_PDF DFTBPLUS_PDF OUTPUT_DIR}
output_dir=${6:?usage: capture-additional-paper-figures.sh LEE_PDF OMM_PDF AFZALIAN_PDF CARRILLO_PDF DFTBPLUS_PDF OUTPUT_DIR}
temporary_dir=$(mktemp -d)
trap 'rm -rf "$temporary_dir"' EXIT
mkdir -p "$output_dir"

pdftoppm -f 5 -l 5 -singlefile -r 300 -png "$lee_pdf" "$temporary_dir/lee-page5"
convert "$temporary_dir/lee-page5.png" -crop 950x620+620+180 +repage \
  "$output_dir/lee-2018-fig5.png"

pdftoppm -f 6 -l 6 -singlefile -r 300 -png "$omm_pdf" "$temporary_dir/omm-page6"
convert "$temporary_dir/omm-page6.png" -crop 1460x1050+360+170 +repage \
  "$output_dir/omm-2023-fig2.png"

pdftoppm -f 2 -l 2 -singlefile -r 300 -png "$afzalian_pdf" "$temporary_dir/afzalian-page2"
convert "$temporary_dir/afzalian-page2.png" -crop 2040x1000+280+280 +repage \
  "$output_dir/afzalian-2021-fig1.png"

pdftoppm -f 3 -l 3 -singlefile -r 300 -png "$afzalian_pdf" "$temporary_dir/afzalian-page3"
convert "$temporary_dir/afzalian-page3.png" -crop 1106x459+150+872 +repage \
  "$output_dir/afzalian-2021-fig2.png"

pdftoppm -f 6 -l 6 -singlefile -r 300 -png "$carrillo_pdf" "$temporary_dir/carrillo-page6"
convert "$temporary_dir/carrillo-page6.png" -crop 1090x1030+160+310 +repage \
  "$output_dir/carrillo-nunez-2020-fig2.png"

pdftoppm -f 14 -l 14 -singlefile -r 300 -png "$dftbplus_pdf" "$temporary_dir/dftbplus-page14"
convert "$temporary_dir/dftbplus-page14.png" -crop 1060x740+160+790 +repage \
  "$output_dir/dftbplus-hourahine-2020-fig5-cd.png"

sha256sum \
  "$output_dir/lee-2018-fig5.png" \
  "$output_dir/omm-2023-fig2.png" \
  "$output_dir/afzalian-2021-fig1.png" \
  "$output_dir/afzalian-2021-fig2.png" \
  "$output_dir/carrillo-nunez-2020-fig2.png" \
  "$output_dir/dftbplus-hourahine-2020-fig5-cd.png"
