
printf "\n \n \n"
echo -e "\e[1;34m Checking file permissions \e[0m"
ls -l hw.py
ls -l hw2.py
ls -l hw3.py
ls -l draw_shape.py
ls -l triangle.py
ls -l rectangle.py
ls -l circle.py
ls -l shapes.py
ls -l midpoint.py
ls -l bisection.py


printf "\n \n \n"
echo -e "\e[1;34m Running homeworks 1,2,3 \e[0m"
python hw.py
python hw2.py Sample_text
python hw3.py
python hw3.py Carl
python hw3.py Carl Des
python hw3.py Carl Des Ghana
printf "\n \n \n"
echo -e "\e[1;34m Running triangle example, expect 0.433 \e[0m"
python triangle.py 1 1 1 
printf "\n \n \n"
echo -e "\e[1;34m Running rectangle example, expect 15 \e[0m"
python rectangle.py 5 3
printf "\n \n \n"
echo -e "\e[1;34m Running rectangle example, expect 25 2\e[0m"
python rectangle.py 5
printf "\n \n \n"
echo -e "\e[1;34m Running circle, expect 12.56 example \e[0m"
python circle.py 2
printf "\n \n \n"
echo -e "\e[1;34m Checking basic shapes \e[0m"
python basic_shapes.py
printf "\n \n \n"
echo -e "\e[1;34m Checking shapes \e[0m"
python shapes.py
python shapes.py OCTAGON 1.5
python shapes.py TRIANGLE 17
python shapes.py SQUARE 8
python shapes.py CIRCLE 6
printf "\n \n \n"
echo -e "\e[1;34m Checking render_shapes \e[0m"
python render_shapes.py
python render_shapes2.py
printf "\n \n \n"
echo -e "\e[1;34m Checking try_root and try_integrator \e[0m"
python try_root.py
python try_integrator.py


printf "\n \n \n"
echo -e "\e[1;34m hw.py \e[0m"
cat hw.py
printf "\n \n \n"
echo -e "\e[1;34m hw2.py \e[0m"
cat hw2.py
printf "\n \n \n"
echo -e "\e[1;34m hw3.py \e[0m"
cat hw3.py
printf "\n \n \n"
echo -e "\e[1;34m triangle.py \e[0m"
cat triangle.py
printf "\n \n \n"
echo -e "\e[1;34m rectangle.py \e[0m"
cat rectangle.py
printf "\n \n \n"
echo -e "\e[1;34m circle.py \e[0m"
cat circle.py
printf "\n \n \n"
echo -e "\e[1;34m shapes.py \e[0m"
cat shapes.py
printf "\n \n \n"
echo -e "\e[1;34m draw_shape.py \e[0m"
cat draw_shape.py
printf "\n \n \n"
echo -e "\e[1;34m midpoint.py \e[0m"
cat midpoint.py
printf "\n \n \n"
echo -e "\e[1;34m bisection.py \e[0m"
cat bisection.py

