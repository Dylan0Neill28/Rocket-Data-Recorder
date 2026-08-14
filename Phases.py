import math

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

def check_points(data, x, i):
    if x + i + 1 <= len(data):
                data[x + i + 1]
    else:
        if x + i <= len(data):
            data[x+i]
        else:
            data[x]

def state_machine_outline(x, i, ay, vy, altitude):
    idle = Node(rule1="Is the ay greater than 1.5?", rule2="Is the vy positive?", feature1=ay, feature2=vy, threshold1=1.5, threshold2= 0, operator1=">", operator2="=", result="Idle", window=20)
    powered_flight = Node(rule1="Is the ay less than 0.2", rule2="Is the vy greater than 0", feature1=ay, feature2=vy, threshold1=0.2, threshold2=0, operator1= "<", operator2=">", result="Powered Flight", window=20)
    burnout = Node(rule1="Is ay equal to 0", rule2="is vy greater than 0", feature1=ay, feature2=vy, threshold1=0, threshold2=0 ,operator1= "=", operator2=">", result="Burnout")
    coast = Node(rule1="Is the vy less than zero", rule2="Is the altitude less than previous altitude?", feature1=vy, feature2=altitude, threshold1= 0, threshold2=altitude[x - 1], operator1= "=", operator2=">=", result="Coast")
    apogee = Node(rule1="Is the velocity less -0.5 vy?", rule2="Altitude is decreasing", feature1=vy, feature2=altitude, threshold1= -0.5, threshold2= check_points(altitude, x, i), operator1= "<", operator2="<",window=10, result="Apogee")
    descent = Node(rule1="Altitude is decreasing", rule2="Abs of velocity is less than previous abs",feature1=altitude, feature2=abs(vy), threshold1=altitude[x-1], threshold2=abs(vy[x-1]) ,operator1= "<", operator2="<", result="Descent")
    parachute = Node(rule1="Is the vertical velocity less than 0.5?", rule2="Is the altitude consistent", feature1=abs(vy), feature2=altitude, threshold1=0.5, threshold2=math.trunc(altitude[x-1]), operator1= "<", operator2="=", window=30, result="Parachute")
    landed = Node(result="Landed")

    idle.next = powered_flight
    powered_flight.next = burnout
    burnout.next = coast
    coast.next = apogee
    apogee.next = descent
    descent.next = parachute
    parachute.next = landed

