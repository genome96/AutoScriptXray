#!/bin/bash
# color settings
BGreen='\e[1;32m'
BYellow='\e[1;33m'
BBlue='\e[1;34m'
BPurple='\e[1;35m'
NC='\e[0m'
MYIP=$(wget -qO- ipv4.icanhazip.com);
echo "Checking VPS"
clear
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m                 BANDWIDTH MONITOR                 \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "" 
echo -e "\e[1;35m 1 \e[0m View Total Remaining Bandwidth"
echo -e "\e[1;35m 2 \e[0m Table Usage every 5 Minutes"
echo -e "\e[1;35m 3 \e[0m Table Usage every Hour"
echo -e "\e[1;35m 4 \e[0m Table Usage every Day"
echo -e "\e[1;35m 5 \e[0m Table Usage every Month"
echo -e "\e[1;35m 6 \e[0m Table Usage every Year"
echo -e "\e[1;35m 7 \e[0m Highest Usage Table"
echo -e "\e[1;35m 8 \e[0m Hourly Usage Statistics"
echo -e "\e[1;35m 9 \e[0m View Current Active Usage"
echo -e "\e[1;35m 10 \e[0m View Current Active Traffic Usage [5s]"
echo -e "" 
echo -e "\e[1;34m 0 BACK TO MENU \e[0m"
echo -e "\e[1;34m x Exit \e[0m"
echo -e "" 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -p " Select menu: " opt
echo -e ""
case $opt in
1)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m          TOTAL SERVER BANDWIDTH REMAINING         \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

2)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m            TOTAL BANDWIDTH every 5 MINUTES         \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -5

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

3)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m              TOTAL BANDWIDTH every HOUR           \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -h

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

4)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m            TOTAL BANDWIDTH every DAY            \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -d

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

5)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m            TOTAL BANDWIDTH every MONTH         \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -m

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

6)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m            TOTAL BANDWIDTH every YEAR           \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -y

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

7)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m              HIGHEST BANDWIDTH USAGE            \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -t

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

8)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m           HOURLY USAGE STATISTICS          \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -hg

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

9)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m               CURRENT LIVE BANDWIDTH             \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m Press [ Ctrl+C ] To Exit \e[0m"
echo -e ""

vnstat -l

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

10)
clear 
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e "\e[1;34m           CURRENT LIVE TRAFFIC USAGE        \e[0m"
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""

vnstat -tr

echo -e ""
echo -e "\e[1;33m -------------------------------------------------\e[0m"
echo -e ""
read -n 1 -s -r -p "Press any key to return to the menu"
bw
;;

0)
sleep 1
m-system
;;
x)
exit
;;
*)
echo -e ""
echo -e "You pressed the wrong key"
sleep 1
bw
;;
esac
