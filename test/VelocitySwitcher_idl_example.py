﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file VelocitySwitcher_idl_examplefile.py
 @brief Python example implementations generated from VelocitySwitcher.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import KanamuraRobotics, KanamuraRobotics__POA



class VelocitySwitcherService_i (KanamuraRobotics__POA.VelocitySwitcherService):
    """
    @class VelocitySwitcherService_i
    Example class implementing IDL interface KanamuraRobotics.VelocitySwitcherService
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # boolean getSwitch()
    def getSwitch(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # long setSwitch(in boolean flag)
    def setSwitch(self, flag):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = VelocitySwitcherService_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

