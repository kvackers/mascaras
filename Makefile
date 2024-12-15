build: clean
	mkdocs build

clean:
	rm -rf docs

.PHONY: clean build