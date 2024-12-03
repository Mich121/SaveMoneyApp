#colours of icons:
#bus FF0D0D /tshirt FF00E6 /cutlery 3BFF5B /phone 412BFF /home 7DFBFF /car B17DFF /money 1F8F36 /investment 255441
#good 1DAD49 /generate figure C26D3C /wrong E30000 /economy 3EE807

def leftGroup1():
    return"""
    QGroupBox {
        background-color: #F28416;
        border-radius: 15px;
        }
        """
 
def leftGroup2():
    return"""
    QGroupBox {
        background-color: #FF0D0D;
        border-radius: 15px;
        }
        """

def leftGroup3():
    return"""
    QGroupBox {
        background-color: #FF00E6;
        border-radius: 15px;
        }
        """

def leftGroup4():
    return"""
    QGroupBox {
        background-color: #3BFF5B;
        border-radius: 15px;
        }
        """

def leftGroup5():
    return"""
    QGroupBox {
        background-color: #412BFF;
        border-radius: 15px;
        }
        """

def leftGroup6():
    return"""
    QGroupBox {
        background-color: #B17DFF;
        border-radius: 15px;
        }
        """

def leftGroup7():
    return"""
    QGroupBox {
        background-color: #3EE807;
        border-radius: 15px;
        }
        """

def addRevenueButton():
    return"""
    QPushButton {
        font: Arial Bold;
        font-size: 18pt;
        color: green;
        border: 2px solid green;
        border-radius: 10px;
    }
    """

def addSpendingButton():
    return"""
    QPushButton {
        font: Arial Bold;
        font-size: 18pt;
        color: red;
        border: 2px solid red;
        border-radius: 10px;
    }
    """

def GenerateFigureSaldoButton():
    return"""
    QPushButton {
        font: Arial Bold;
        font-size: 18pt;
        color: green;
        border: 2px solid green;
        border-radius: 10px;
    }
    """

def addRevenueSubmitBtn():
    return"""
    QPushButton {
        font-size: 18pt;
        border: 2px solid white;
    }
    """

def addSpendingSubmitBtn():
    return"""
    QPushButton {
        font-size: 18pt;
        border: 2px solid white;
    }
    """

def LookForSpendBtn():
    return"""
    QPushButton {
        font-size: 18pt;
        color: white;
        background-color: green;
    }
    """