#!/bin/bash

# @Title: Subida de cambios a GitHub
# @Description: Para automatizar la subida, cada 5 min el sistema lanza
# el script y realiza una subida de los cambios que encuentra.
# @Author: Chunche

param=$1
echo "-------------------------------------------"
echo -e "\e[1;37m Estado de repositorio... \e"
echo "-------------------------------------------"
git status
sleep 3
echo "-----------------------------------------------------"
echo -e "\e[1;37m Añadiendo cambios a zona 'de envio'... \e"
echo "-----------------------------------------------------"
git add .
echo "-----------------------------------------------------"
echo -e "\e[1;37m  Añadiendo comentario a los cambios...  \e"
echo "-----------------------------------------------------"
if [ -z $param ]
then
	echo "=========================================================="
	echo -e "\e[0;31m Añadiendo comentario automático de sistema... \e"
	echo "=========================================================="
	comentario="Auto Commit - Eject Sys"
	git commit -m "$comentario"
else
	echo "===================================="
	echo -e "\e[0;31m Añadiendo su comentario \e"
	echo "===================================="
	git commit -m "$1"
fi
echo "---------------------------------"
echo -e "\e[1;37m Subiendo archivos... \e"
echo "--------------------------------"
git push origin master
echo "--------------------------------"
echo -e "\e[1;36m Archivos Subidos \t \e"
echo "--------------------------------"
sleep 5

#clear
