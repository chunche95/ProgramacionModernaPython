#!/bin/bash

# @Title: Subida de cambios a GitHub
# @Description: Para automatizar la subida, cada 5 min el sistema lanza
# el script y realiza una subida de los cambios que encuentra.
# @Author: Chunche
param=$1


echo -e "\e[32m Estado de repositorio... \n"
git status
sleep 3
echo -e "\e[33m Añadiendo cambios a zona 'de envio'... "
git add .

echo -e "\e[34m  Añadiendo comentario a los cambios..."
if [ -z $param ]
then
	echo -e "\e[31m Añadiendo comentario automático de sistema..."
	comentario="Auto Commit - Eject Sys"
	git commit -m "$comentario"
else
	echo -e "\e[30m Añadiendo su comentario"
	git commit -m "$1"
fi

echo -e "e[35m Subiendo archivos..."
git push origin master

echo -e "\e[36m Archivos Subidos \t"
sleep 5

clear
