# Jaimin Kirankumar Kerai - 22718975
# The program below will determine the number of bees within a hive for a certain number of days given some imputs listed below 
# In the shell below run 'honeybee(HO, FO, L, w, m, n)' and follow the instructions to obtain the H, F, Hmax and Fmax
# Inputs are as :
# HO : Initial population of bees working in hive
# FO : Initial population of bees working outside the hive
# L : Queen bee's egg laying rate
# w : Rate at L(N/w+N) approaches L
# m : Bees' death rate
# n : Total number of days which need to be simuated

def honeybee(HO, FO, L, w, m, n):    
    # This will test the conditions of each of the entered values
    if HO<0:
        print("You have entered an invalid value for HO!")
        exit()
    else:
        if FO<0:
            print("You have entered an invalid value for FO!")
            exit()
        else:
            if L<0:
                print("You have entered an invalid value for L!")
                exit()
            else:
                if w<0:
                    print("You have entered an invalid value for w!")
                    exit()
                else:
                    if m<0:
                        print("You have entered an invalid value for m!")
                        exit()
                    else:
                        if n<0:
                            print("You have entered an invalid value for n!")
                            exit()
                        else:
                            # This is the initialisation of our created arrays
                            H = []
                            F = []
                            for i in range(n+1):
                                # This is the loop which will determine the values for each day
                                H.append(int(HO))
                                F.append(int(FO))
                                N = HO + FO
                                H_calc = HO + L*((N)/(w+N)) - HO*(0.25-0.75*((FO)/(N+0.001)))
                                F_calc = FO + HO*(0.25-0.75*((FO)/(N+0.001)))-m*FO
                                HO = round(H_calc,0)
                                FO = round(F_calc,0)
                            return "H =", H, "F =", F, "Hmax =", max(H), "Fmax =", max(F)
                            
                            
