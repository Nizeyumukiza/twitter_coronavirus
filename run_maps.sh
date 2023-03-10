# script to run map.py for all files in /data-fast/twitter\ 2020 folder
path="/data/Twitter dataset"
path_to_run="/data/Twitter "
echo 'starting'>outputs/run.md
for file in `ls "$path"/geoTwitter20*.zip` ; do
    if [[ "$file" == "/data/Twitter" ]]; then
        continue
    fi
    echo 'running' "$path_to_run"$file>>outputs/run.md
    python3 ./src/map.py --input_path="$path_to_run"$file
 done;
 echo 'done mapping.'>>outputs/run.md
