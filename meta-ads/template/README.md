# Brainsick ad templates

Three approved 4:5 (1080×1350) Meta ad layouts: **notification**, **post** and **them-vs-us split**.

## Add a new tee
1. Put the product photo (4:5, plain background) in this folder.
2. Add an entry to `TEES` in `gen.py`: the image, its background colour, and the copy for each layout.
3. Render:
   ```sh
   npm i playwright-core
   node render.js $(python3 gen.py)
   ```
   PNGs are written next to the HTML files as `final-<tee>-<layout>.png`.
