class Node:
    def __init__(self, rule1=None, rule2=None, rule3=None, operator1=None, operator2=None, operator3=None, feature1=None, feature2=None, feature3=None ,threshold1=None, threshold2=None, threshold3=None, window=None, result=None):
        self.rule1 = rule1
        self.rule2 = rule2
        self.rule3 = rule3
        self.operator1 = operator1
        self.operator2 = operator2
        self.operator3 = operator3
        self.feature1 = feature1
        self.feature2 = feature2
        self.feature3 = feature3
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        self.threshold3 = threshold3
        self.window = window
        self.next = None
        self.result = result

    def run_state_machine(self, x):     
        tf = []
        
        if self.window is not True:
            value = self.feature[x]
            tf = [compare(value, self.operator1, self.threshold1), compare(value, self.operator2, self.threshold2), compare(value, self.operator3, self.threshold3)]
        else:
            for i in self.window:
                if x + i <= len(self.feature):
                    value = self.feature[x + i]
                else:
                    value = self.feature[len(self.feature)]
                tf.append(compare(value, self.operator1, self.threshold1), compare(value, self.operator2, self.threshold2), compare(value, self.operator3, self.threshold3))

                if all(tf) is not True:
                    break
    
        if all(tf):
            return self.next

        return self

def compare(value, operator, threshold):
    if operator == ">":
        return value > threshold
    elif operator == ">=":
        return value >= threshold
    elif operator == "=":
        return value == threshold
    elif operator == "!=":
        return value != threshold
    elif operator and value and threshold is None:
        return True
    else:
        raise ValueError('Unknown Opperator')

def state_machine_outline(ax, ay, az, vx, vy, altitude):
    idle = Node(rule1="Is the ay greater than 1.5?", rule2="Is the vy positive?", feature1=ay, feature2=vy, threshold1=1.5, threshold2= 0, operator1=">", operator2="=", result="Idle", window=20)
    powered_flight = Node(rule1="Is the ay", rule2="Is the vy", feature1=ay, feature2=vy, threshold1=None, threshold2=None, operator1= "<", operator2=">", result="Powered Flight", window=5)

    burnout = Node(rule1="Is current velcity less than previous velocity?", feature=vy, threshold= "previous", operator= "<", result="Burnout")
    coast = Node(rule1="Is the velcity equal to 0?", feature=vy, threshold= 0, operator= "==", result="Coast")
    apogee = Node(rule1="Is the velocity less than 0?", feature=vy, threshold= 0, operator= "<", result="Apogee")
    descent = Node(rule1="Is current acceleration greater than previous acceleration?", feature=vy, threshold= "previous", operator= ">", result="Descent")
    parachute = Node(rule1="Is the velocity equal to 0?", feature=vy, threshold= 0, operator= "==", result="Parachute")
    landed = Node(result="Landed")

    idle.next = powered_flight
    powered_flight.next = burnout
    burnout.next = coast
    coast.next = apogee
    apogee.next = descent
    descent.next = parachute
    parachute.next = landed

