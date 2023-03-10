# load keywords
hashtags=(
    '#코로나바이러스'
    '#コロナウイルス'
    '#冠状病毒'
    '#covid19'
    '#corona'
    '#virus'
    '#flu'
    '#sick'
    '#cough'
    '#sneeze'
    '#hospital'
    '#nurse'
    '#doctor'
)
# make a folder to store results
cd ./; rm -rf visuals; mkdir "visuals"; mkdir ./visuals/"top_ten"
# for each hashtag, output its visualized result from .lang and one from .country

for hashtag in "${hashtags[@]}"; do
    echo "All languages " >> ./visuals/$hashtag.lang
   python3 ./src/visualize.py --input_path=./reduced.lang --key="$hashtag" >> ./visuals/$hashtag.lang 
  
   echo "Top ten languages ">> ./visuals/top_ten/ten$hashtag.lang 
  head -n 11 ./visuals/$hashtag.lang | tail -10  >>./visuals/top_ten/ten$hashtag.lang

  echo "All countries " >> ./visuals/$hashtag.country
   python3 ./src/visualize.py --input_path=./reduced.country --key="$hashtag" >> ./visuals/$hashtag.country 
 
   echo "Top ten countries " >> ./visuals/top_ten/ten$hashtag.country
   head -n 11 ./visuals/$hashtag.country | tail -10 >> ./visuals/top_ten/ten$hashtag.country 
 done;
