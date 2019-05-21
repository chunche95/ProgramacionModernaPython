#!/bin/bash

# @Title: Subida de cambios a GitHub
# @Description: Para automatizar la subida, cada 5 min el sistema lanza 
# el script y realiza una subida de los cambios que encuentra.
# @Author: Chunche

git status

git add .

git commit -m "$1"

git push origin master

echo -e "\e[33m Archivos Subidos \m"
