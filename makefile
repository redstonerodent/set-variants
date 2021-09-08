main:
	for name in proset s4set wreathset;\
	do \
		echo $$name;\
		mkdir -p $$name/fronts;\
		python $$name.py;\
	done