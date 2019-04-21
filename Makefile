build:
	docker build -t brandonharrisoncode/nlp-qna .

run: build
	docker run -it -p 5000:5000 brandonharrisoncode/nlp-qna
