main(){
	for i in {a..z}
	do
        	echo ${1,,} | grep -qv $i && { echo "false"; exit 0; }
	done
	echo "true"
}

main "$@"
