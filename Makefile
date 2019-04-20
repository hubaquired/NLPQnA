build:
	docker build -t brandonharrisoncode/nlp-qna .

run: build
	docker run -it brandonharrisoncode/nlp-qna
