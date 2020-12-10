version="1.1.5"

build:
	docker build -t pandas:$(version) .

drop:
	docker rmi pandas:$(version)