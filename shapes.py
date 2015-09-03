#!/usr/bin/python
import sys
import math

def figure_check(figure_name,figure_area):
 

      if figure_name=='TRIANGLE':
          #find side
          side=math.sqrt( float(figure_area*4) /float( math.sqrt(3) ) )
          print('\nEquilateral TRIANGLE, area', figure_area,',side:',side,'.....\n')
          values=[figure_area,side]
          return side

      elif figure_name=='SQUARE':
          #find side
          side=math.sqrt(float(figure_area))
          print('\nSQUARE, area', figure_area,',side:',side,'.....\n')
          values=[figure_area,side]
          return side
 
      elif figure_name=='CIRCLE':
          radius=math.sqrt(float(figure_area)/math.pi)
          print('\nCIRCLE, area', figure_area,',radius:',radius,'.....\n')
          values=[figure_area,radius]
          return radius 

      else:
          pass
          print('\n ... error indicating unknown shape... \n')


if __name__=="__main__":
    
      if len(sys.argv)==1:
       
       print('\n....error indicating no input....\n')

      else:
           figure_check(sys.argv[1],sys.argv[2])
