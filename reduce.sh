echo "Started reducing lang." >> reduce.md
python3 ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang
echo "Done reducing lang." >> reduce.md
echo "Started reducing country." >> reduce.md
python3 ./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced.country
echo "Done reducing country." >> reduce.md
