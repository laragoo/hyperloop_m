"""
UPDATED: 9/8/15
  >>> Added in Induced Drag, changed coefficients based on paper
  >>> This induced drag is based on numbers from a Swiss paper & NASA paper

I'm doing this in python because I don't know Matlab enough (nor do I care to)
to do it in that language. Thus Python.

NOTES:
------
  * Is distance traveled incrementative?


IDEAS:
------
  * Extend ability to add 'track' with positions for banking & otherwise
  * r_wheel for friction
  * Implement friction for air bearings

"""
# = = = = = = IMPORTS = = = = = = = #
import sys,os,time,math
import pandas as pd
import matplotlib.pyplot as plt


# = = = = = = = Function = = = = = = #
def calculate_airdrag(output_name="airdrag_calculations.csv",
                      sample_rate=1,    # Sample rate in Hz
                      sample_length=600,# number of steps to take
                      u_r=0.002,        # coefficient of friction on wheels
                      M_pod=5000,       # mass of pod
                      A_c=0.3,          # Cross sectional area [m]
                      r_wheel=0.15,     # Radius of wheels on pod
                      v_i=300,          # initial velocity [m/s]
                      wheel_thresh=100, # Default speed at which point wheels enter in
                      C_d=0.3669,       # Drag Coefficient
                      C_l=0.0980,       # Lift Coefficient for induced drag
                      AR=1.0,           # Aspect Ratio (nose cone divided by base)
                      e_ff=0.59,        # Efficiency Factor
                      P_air=99,         # Density of air in pascals
                      T_air=300,        # Temperature of the air in kelvins
                      M_air=28.97,      # Molar mass of the air
                      until_stop=False, # Calculate until the pod stops, if 
                                        # false then calculate the sample_length
                      output_file=True, # Output the readouts to a csv
                      plotting=True,    # Plot the results
                      ):
    """
    ASSUMPTIONS:
    - No air bearings take into account
    - No Compressor taken into account (assuming would mitigate drag)
    
    Read-Out on CSV:
    Time Step  |  Velocity of the Pod  |  Deceleration due to drag  |  Distance Traveled in Meters

    OUTLINE:
    -------
    acc = dependent on circumstances
    
    a_fric is friction on the wheels
        a_fric = -g*u_r/r
        * Not dependent on velocity?
        * Occurs at speeds less than V <= wheel_thresh (defaults to 100 m/s)

    a_slippers is the friction on the air slippers
        * TO-DO...
    
    a_drag is friction due to drag. Dependent on speed
        a_drag = (rho * V^2 * C_d * A_c)/(2*m_pod)
        V here will change depending on the speed of the pod at that time
        
    a_lift is induced friction. Dependent, again, on speed.
        a_lift = C_l^2 / (pi * e * AR)
        AR is length of nose cone divided by base diameter (for cones/cylinders)
            AR = 1 for now?
        pi is 3.14159
        e is efficiency, 0.59 for bullets (will use to expendiency)
    
    rho is also calculated via:
        rho = P_air/(R_air * T_air)
        R_air = R / M_air

    Distance is found via:
        v_f^2 = v_i^2 + 2*acc*d
        d = (v_f^2 - v_i^2)/(2*acc)

    Deleceration is found via:
        acc = (v_f - v_i)/t
        acc * t + v_i = v_f
        acc * (1/sample_rate) + v_i = v_f
    """

    print("Starting...\n");
    start_time = time.time()

    # Calculate some constants
    R_air = 8.31451 / M_air       # Specific Gas Constant of Air
    rho = P_air/(R_air * T_air)   # Density of air
    g = 9.80665                   # Gravity
    pi = 3.14159                  # Self-Explanatory
    V = v_i                       # Velocity starts at the initial velocity
    outputs = []                  # To hold output rows
    distance = 0                  # Distance
    time_step = 1                 # Initial Time
    stamp = 0                     # Time Stamp

    if until_stop==True:
        sample_length = sys.maxsize - 1;
    
    for i in range(sample_length):
        
        acc = -(rho * V**2 * C_d * A_c)/(2*M_pod)   # Negative sign b/c its deceleration

        # Check for additional friction from wheels
        if V <= wheel_thresh:
            acc += (-g * u_r)/r_wheel
            if stamp==0:
                stamp = i;

        acc += (C_l**2) / (pi * e_ff * AR)   # Lift Drag

        row = [time_step,V,acc,distance]
        outputs.append(row);
        print(row);

        time_step += 1;
        V_prior = V
        V = acc * (1/sample_rate) + V_prior
        distance =  distance + ((V**2 - V_prior**2)/(2*acc))  # Do I take into consideration the previous distance?

        if until_stop==True:
            if V <= 0:
                print("It took %.2f seconds to go %f meters." % (float(i/sample_rate),distance));
                print("In Miles: %f" % (distance/1609.34));
                break;
            

    if output_file==True:
        df = pd.DataFrame(outputs);
        df.columns = ['Time Step', 'Velocity', 'Acceleration', 'Distance Traveled'];
        df.to_csv(output_name);
        print("Done! Outputted to " + output_name);

    if plotting==True:
        plt.scatter(df['Time Step'], df['Velocity']);
        plt.title("Velocity Over Time");
        plt.ylabel("Velocity [m/s]");
        plt.xlabel("Time Step");
        plt.show()

        plt.scatter(df['Time Step'], df['Acceleration']);
        plt.title("Acceleration Over Time");
        plt.ylabel("Acceleration [m/s^2]");
        plt.xlabel("Time Step");
        plt.show()

    print("Wheels Were Deployd at %d" % stamp);
    print(" - - It took %f seconds to compute - - " % (time.time() - start_time));

    
