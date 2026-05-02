MODEL_CODENAME = DonerKebab
LANG = python3
PPM = pip

build:
	$(LANG) train.py config/train_echo.py

gensamples:
	$(LANG) sample.py --out_dir=out-whiterock

genvenv:
	$(LANG) -m venv venv

deps:
	$(PPM) install tiktoken numpy torch
