main:
	for name in proset s4set wreathset c4torsor c5torsor wreathtorsor;\
	do \
		make one name=$$name;\
	done

one:
	echo $(name)
	rm -rf $(name)
	mkdir -p $(name)/fronts
	python $(name).py
	