#!/bin/bash

# @Title: Subida de cambios a GitHub
# @Description: Para automatizar la subida, cada 5 min el sistema lanza
# el script y realiza una subida de los cambios que encuentra.
# @Author: Chunche

param=$1
echo "-------------------------------------------"
echo -e "\e[1;32m Estado de repositorio... \n"
echo "-------------------------------------------"
git status
sleep 3
echo "-----------------------------------------------------"
echo -e "\e[1;32m Añadiendo cambios a zona 'de envio'... "
echo "-----------------------------------------------------"
git add .
echo "-----------------------------------------------------"
echo -e "\e[1;32m  Añadiendo comentario a los cambios..."
echo "-----------------------------------------------------"
if [ -z $param ]
then
	echo "=========================================================="
	echo -e "\e[0;31m Añadiendo comentario automático de sistema..."
	echo "=========================================================="
	comentario="Auto Commit - Eject Sys"
	git commit -m "$comentario"
else
	echo "===================================="
	echo -e "\e[0;31m Añadiendo su comentario"
	echo "===================================="
	git commit -m "$1"
fi
echo "---------------------------------"
echo -e "\e[1;32m Subiendo archivos..."
echo "--------------------------------"
git push origin master
echo "--------------------------------"
echo -e "\e[0;36m Archivos Subidos \t"
echo "--------------------------------"
sleep 5

#clear
