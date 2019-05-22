#!/bin/bash

# @Title: Subida de cambios a GitHub
# @Description: Para automatizar la subida, cada 5 min el sistema lanza
# el script y realiza una subida de los cambios que encuentra.
# @Author: Chunche

param=$1
echo "-------------------------------------------"
echo -e "\e[1;35m Estado de repositorio... \e"
echo "-------------------------------------------"
echo ""
git status
sleep 3
echo "-----------------------------------------------------"
echo -e "\e[1;32m Añadiendo cambios a zona 'de envio'... \e"
echo "-----------------------------------------------------"
echo ""
git add .
echo "-----------------------------------------------------"
echo -e "\e[1;33m  Añadiendo comentario a los cambios...  \e"
echo "-----------------------------------------------------"
echo ""
if [ -z ${param} ]; then
	echo "=========================================================="
	echo -e "\e[0;31m Añadiendo comentario automático de sistema... \e"
	echo "=========================================================="
	echo ""
	comentario="Auto Commit - Eject Sys"
	git commit -m "$comentario"
else
	echo "===================================="
	echo -e "\e[0;31m Añadiendo su comentario \e"
	echo "===================================="
	echo ""
	git commit -m "$1"
fi
echo "---------------------------------"
echo -e "\e[1;34m Subiendo archivos... \e"
echo "--------------------------------"
echo ""
git push origin master
echo "--------------------------------"
echo -e "\e[1;36m Archivos Subidos  \e"
echo "--------------------------------"
echo ""
sleep 5

clear
