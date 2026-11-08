#!/usr/bin/env bash
set -euo pipefail

lee_pdf=${1:?usage: capture-dielectric-paper-figures.sh LEE_PDF YIM_PDF OUTPUT_DIR}
yim_pdf=${2:?usage: capture-dielectric-paper-figures.sh LEE_PDF YIM_PDF OUTPUT_DIR}
output_dir=${3:?usage: capture-dielectric-paper-figures.sh LEE_PDF YIM_PDF OUTPUT_DIR}
temporary_dir=$(mktemp -d)
trap 'rm -rf "$temporary_dir"' EXIT
mkdir -p "$output_dir"

pdftoppm -f 4 -l 4 -singlefile -r 300 -png "$lee_pdf" "$temporary_dir/lee-page4"
convert "$temporary_dir/lee-page4.png" -crop 1620x600+620+1460 +repage \
  "$output_dir/lee-2018-fig4.png"

pdftoppm -f 3 -l 3 -singlefile -r 300 -png "$yim_pdf" "$temporary_dir/yim-page3"
convert "$temporary_dir/yim-page3.png" -crop 1140x700+1270+275 +repage \
  "$output_dir/yim-2015-fig4.png"

sha256sum "$output_dir/lee-2018-fig4.png" "$output_dir/yim-2015-fig4.png"
