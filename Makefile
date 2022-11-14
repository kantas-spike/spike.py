DST_DIR=${HOME}/bin

install: spike.py
	mkdir -p ${DST_DIR}
	cp $< ${DST_DIR}
	chmod u+x ${DST_DIR}/$<
