all: build

.PHONY: build clean heaptest profile test

build:
	python setup.py build_ext --inplace

clean:
	rm -rf build
	rm -rf *.so
	rm -rf *~
	rm -rf .*~
	rm -rf .*.swp
	rm -rf $(patsubst %.pyx,%.c,$(wildcard *.pyx))

test: build
	python test_nanoclock.py
