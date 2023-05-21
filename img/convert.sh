for f in */000001.jpg
do
	newf="${f//000001.jpg/1.jpg}"  
	convert $f -resize 200x200 $newf
done
