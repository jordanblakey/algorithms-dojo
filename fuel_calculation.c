#include <stdbool.h>
#include <math.h>

bool zero_fuel(double distance_to_pump, double mpg, double fuel_left)
{
		printf("Distance to pump: %f\nMPG: %f\nFuel left: %f\n",distance_to_pump, mpg, fuel_left);
    float coeff = distance_to_pump - (mpg * fuel_left);
    printf("Distance to pump - Distance drivable: %f\n", coeff);
    
    if (distance_to_pump > 0 && fuel_left == 0) {return false;}

    if (distance_to_pump == 0 || fabs(coeff) == INFINITY || coeff <= 0 || coeff != coeff) {
      return true;
    }
}
