main:
	for name in proset s4set wreathset c4torsor c5torsor;\
	do \
		echo $$name;\
		rm -rf $$name;\
		mkdir -p $$name/fronts;\
		python $$name.py;\
	done