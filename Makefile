py:
	python3 main.py < input.txt > output.txt

java:
	java Main.java < input.txt > output.txt

cpp:
	g++ main.cpp -o output.out && ./output.out < input.txt > output.txt && rm *out