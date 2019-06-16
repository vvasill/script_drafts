cd ./images

for file in *.ps
do
	fn='./'$( echo $file | cut -d "." -f 1 )
	epstopdf $file 
	pdf270 $fn'.pdf' -o './out/'$fn'.pdf'
done
