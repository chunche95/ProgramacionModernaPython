#!/bin/bash

echo "------------------------------------------"
echo "		Actualización del repo		"
echo "------------------------------------------"
echo ""
git pull
sleep 3
clear
echo "------------------------------------------"
echo "		Subiendo cambios		"
echo "------------------------------------------"
echo ""
echo "-------------------------------------------"
echo ""
git README.md
git nota "Introduction for this project - Pau"
git sube
echo "-------------------------------------------"
echo ""
git add IntroductionToPythonAndProgrammingBasic-Cisco-master/*
git nota "IntroductionToPythonAndProgrammingBasic-Cisco-master"
git sube
echo "-------------------------------------------"
git add .
git nota "Files project"
git sube
echo "-------------------------------------------"
echo ""
git add up.sh
git nota "Update the repository in GitHub"
git sube
echo "-------------------------------------------"
echo ""
echo "+--------------------------------------------------+"
echo "| Fin de ejecución del script - Actualizando repo. |"
echo "+--------------------------------------------------+"
clear
echo "==================================================="
git status
echo "==================================================="
sleep 4
clear
sleep 3
echo ""
echo "					再见"
echo "			_________________________________"
echo "				 © Human Computing ® "
echo "				█║▌│█│║▌║││█║▌║▌║█║▌│█"
echo "			_________________________________"
echo ""