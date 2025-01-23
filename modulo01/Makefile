install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

install-aws:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements-aws.txt

lint:
	python3 -m pylint --disable=R,C hello.py

format:
	black *.py

test:
	python3 -m pytest -vv --cov=hello test_hello.py