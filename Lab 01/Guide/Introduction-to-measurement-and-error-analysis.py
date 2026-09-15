

import numpy
import math


#Putting length and width values in an array and in the beginning so that i can easily change the values in the future if needed
length = numpy.array([32.5,32.5,32.6,32.7,32.6]) # Length

width = numpy.array([22.7,22.8,22.6,22.8,22.7]) # width

#Mean Length
mean_value_length = numpy.mean(length)
print("\nLength:\n")
print("Mean Length is: " + str(mean_value_length))


#Standard Deviation in Length
standard_deviation_length = numpy.std(length, ddof = 2)
print("Standard Deviation is: " + str(round(standard_deviation_length, 4)))

#Standard Error in Length

standard_error_length = standard_deviation_length/numpy.sqrt(len(length))
print("Standard Error in Length: " + str(round(standard_error_length, 4)))

#Width


#Mean width
mean_value_width = numpy.mean(width)
print("\n\nWidth:\n")
print("Mean width is: " + str(mean_value_width))


#Standard Deviation in width
standard_deviation_width = numpy.std(width, ddof = 2)
print("Standard Deviation is: " + str(round(standard_deviation_width, 4)))

#Standard Error in width

standard_error_width = standard_deviation_width/numpy.sqrt(len(width))
print("Standard Error in width: " + str(round(standard_error_width, 4)))

#Perimeter

Perimeter = 2*(mean_value_length + mean_value_width)

standard_errorperimeter = numpy.sqrt((pow(standard_error_length, 2)+ pow(standard_error_width, 2)))

print("\nThe Perimeter is: " + str(Perimeter) + " ± " + str(round(standard_errorperimeter, 4)))

#Area

Area = mean_value_length * mean_value_width
standard_errorarea = numpy.sqrt((pow(standard_error_length, 2) * pow(mean_value_width, 2)) + (pow(standard_error_width, 2) * pow(mean_value_length, 2)))
print("\nThe Area is: " + str(Area) + " ± " + str(round((standard_errorarea), 4)))

