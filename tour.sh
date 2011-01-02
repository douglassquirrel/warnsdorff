if [ $# -ne 3 ]
then
  echo "Usage: `basename $0` {output dir} {start board size} {end board size}"
  exit 255
fi

OUTPUT_DIR=$1
START_SIZE=$2
END_SIZE=$3

mkdir $OUTPUT_DIR

for (( i=$START_SIZE ; i<=$END_SIZE  ; i++ )) 
do 
  file=$OUTPUT_DIR/tour$i.txt
  python tour.py $i > $file
  gzip $file 
done
