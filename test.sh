#!/bin/sh

bin/nose
bin/pyflakes trolle
bin/pep8 --repeat --ignore E303,W391,E501 trolle
