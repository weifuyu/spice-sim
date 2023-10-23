import math

class TaperPad:
    """calculate taper-pad parameters
    ref: https://www.electronics-tutorials.ws/attenuators/t-pad-attenuator.html
    """
    def __init__(self, dB, zs, zL) -> None:
        self.dB = dB
        self.zs = zs
        self.zL = zL

    @property
    def k(self):
        """k-factor, or impedance factor
        """
        return 10**(self.dB/20)
    
    @property
    def R3(self):
        """get R3 of taper-pad
        """
        return 2* math.sqrt(self.zs*self.zL) * self.k/(self.k**2 -1)

    @property
    def R1(self):
        """R1 of taper-pad
        """
        return self.zs*((self.k**2+1)/(self.k**2-1)) - self.R3
    
    @property
    def R2(self):
        """R2 of taper-pad
        """
        return self.zL*((self.k**2+1)/(self.k**2-1)) - self.R3
    
    def get_res(self):
        """Get taper-pad resistances
        """
        return [self.R1, self.R2, self.R3]

class BridgedTeePad:
    """calculate bridged Tee attenuator parameters
    ref: https://www.electronics-tutorials.ws/attenuators/bridged-t-attenuator.html
    """

    def __init__(self, dB, z0) -> None:
        self.dB = dB
        self.z0 = z0

    @property
    def k(self):
        """k-factor, or impedance factor
        """
        return 10**(self.dB/20)
    
    @property
    def R1(self):
        return self.z0
    
    @property
    def R2(self):
        return self.R1/(self.k - 1)
    
    @property
    def R3(self):
        return self.R1*(self.k - 1)

    def get_res(self):
        """Get taper-pad resistances
        """
        return [self.R1, self.R2, self.R3]

class PiPad:
    """calculate pi-attenuator parameters
    ref: https://www.electronics-tutorials.ws/attenuators/pi-pad-attenuator.html
    """

    def __init__(self, dB, zs, zL) -> None:
        self.dB = dB
        self.zs = zs
        self.zL = zL
        
    @property
    def k(self):
        """k-factor, or impedance factor
        """
        return 10**(self.dB/20)
    
    @property
    def R1(self):
        return self.zs * ((self.k**2 - 1)/(self.k**2 - 2*self.k * math.sqrt(self.zs/self.zL) + 1))
    
    @property
    def R2(self):
        return 1/2 * math.sqrt(self.zs * self.zL) * (self.k**2 -1) / self.k
    
    @property
    def R3(self):
        return self.zL * ((self.k**2 - 1)/(self.k**2 - 2*self.k / math.sqrt(self.zs/self.zL) + 1))
    
    def get_res(self):
        """Get taper-pad resistances
        """
        return [self.R1, self.R2, self.R3]
    

if __name__ == "__main__":

    # Taper-pad Attenuator with Unequal Impedances
    taper1 = TaperPad(10, 75, 50)
    print(taper1.k, taper1.get_res())

    # T-pad Attenuator with Equal Impedances
    tee1 = TaperPad(18, 600, 600)
    print(tee1.k, tee1.get_res())

    # example: to reduce the level of an 8Ω audio signal line by 4dB
    briged_tee1 = BridgedTeePad(4, 8)
    print(briged_tee1.k, briged_tee1.get_res())

    # example: attenuate a signal between a radio transmitter with an 
    # output impedance (source) of 75Ω and a power signal strength meter of impedance (load) 50Ω by 6dB.
    pi1 = PiPad(6, 75, 50)
    print(pi1.k, pi1.get_res())

    # balanced pi-pad can use the same unbalanced pi-pad formula for calculation
    # In reality the formula could be simplied by using zs=zL
    pi1_balanced = PiPad(10, 75, 75)
    print(pi1_balanced.k, pi1_balanced.get_res())
