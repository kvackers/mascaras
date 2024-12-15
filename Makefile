build: clean
	mkdocs build && touch docs/.nojekyll

clean:
	rm -rf docs

.PHONY: clean build