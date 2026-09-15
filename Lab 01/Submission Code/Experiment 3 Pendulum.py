import numpy
import math

#The Pendulum Experiment:

print("\n\nPendulum Experiment:\n")

#Calculated Raw Data

lengths_of_string = [36.4,36.3,36.4]
Diameters_of_bob = [1.2425,1.205,1.23]
radii_of_bob = [d/2 for d in Diameters_of_bob]
total_time_20_cycles = [23.91,23.98,24.19]
time_periods = [t/20 for t in total_time_20_cycles]



#Working On Radius
mean_radius_of_bob = numpy.mean(radii_of_bob)
print("\nThe Mean Radius of the Bob is: " + str(round(mean_radius_of_bob, 4)) + " cm")

standard_deviation_radius_of_bob = numpy.std(radii_of_bob, ddof = 1)
print("The Standard Deviation in the Radius of the Bob is: " + str(round(standard_deviation_radius_of_bob, 4)))

standard_error_radius_of_bob = standard_deviation_radius_of_bob/numpy.sqrt(len(radii_of_bob))
print("The Standard Error in the Radius of the Bob is: " + str(round(standard_error_radius_of_bob, 4)) + "\n\n")



#Working On String
print("\n\nWorking on the Length of the String:\n")
mean_length_of_string = numpy.mean(lengths_of_string)
print("\nThe Mean Length of the String is: " + str(round(mean_length_of_string, 4)) + " cm")

standard_deviation_length_of_string = numpy.std(lengths_of_string, ddof = 1)
print("The Standard Deviation is: " + str(round(standard_deviation_length_of_string, 4)))

standard_error_length_of_string = standard_deviation_length_of_string/numpy.sqrt(len(lengths_of_string))
print("Standard Error in Length: " + str(round(standard_error_length_of_string, 4)))



#Working On Total Length of the String
print("\n\nWorking on the Total Length of the String:\n")

total_length = mean_length_of_string + mean_radius_of_bob
standard_error_total_length = numpy.sqrt((pow(standard_error_radius_of_bob, 2) + pow(standard_error_length_of_string, 2)))
print("\nThe Total Length of the String is: " + str(round(total_length, 4)) + " cm")

standard_deviation_total_length_of_string = standard_error_total_length*numpy.sqrt(len(lengths_of_string))
print("The Standard Deviation in the Total length of the String is: " + str(round(standard_deviation_total_length_of_string, 4)))

print("The Standard Error in the Total Length of the String is: " + str(round(standard_error_total_length, 4)) + "\n\n")


#Working On Time Periods
print("\n\nWorking on the Time Periods:\n")

mean_time_period = numpy.mean(time_periods)
print("\nThe Mean Time Period is: " + str(round(mean_time_period, 4)) + " s")

standard_deviation_time_period = numpy.std(time_periods, ddof = 1)
print("The Standard Deviation in Time Period is: " + str(round(standard_deviation_time_period, 4)))

standard_error_time_period = standard_deviation_time_period/numpy.sqrt(len(time_periods))
print("The Standard Error in Time Period is: " + str(round(standard_error_time_period, 4)))

#Working with Mean Squared Time Period
Mean_Squared_Time_Period = pow(mean_time_period, 2)
standard_error_squared_time_period = 2*mean_time_period*standard_error_time_period
print("The Standard Error in the Square of the Time Period is: " + str(round(standard_error_squared_time_period, 4)))

ratio_length_to_time_period_squared = total_length/Mean_Squared_Time_Period

gravitational_acceleration = 4*math.pi*math.pi*ratio_length_to_time_period_squared


print("\n\nFinal Results\n\n\n")
print(f"The value of Gravitational Acceleration is: {round(gravitational_acceleration, 4)} cm/s^2")


#calculate the standard error in the mean value of Gravitational Acceleration

standard_error_gravitational_acceleration = (gravitational_acceleration*numpy.sqrt((pow(standard_error_total_length/total_length, 2) + pow((2*standard_error_time_period)/mean_time_period, 2))))
print("The Standard Error in the value of Gravitational Acceleration is: " + str(round(standard_error_gravitational_acceleration, 4)))


#finding percentage error in Gravitational acceleration.

percentage_error_gravitationalacceleration = (standard_error_gravitational_acceleration/gravitational_acceleration)*100
print("The Percentage Error in the value of Gravitational Acceleration is: " + str(round(percentage_error_gravitationalacceleration, 4)) + "%")

