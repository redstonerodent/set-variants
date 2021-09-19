main:
	for name in proset s4set wreathset c4torsor c5torsor wreathtorsor;\
	do \
		echo;\
		echo $$name;\
		make one name=$$name;\
	done

one:
	rm -rf $(name)
	mkdir -p $(name)/fronts
	python $(name).py
	