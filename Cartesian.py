import math

class LineFromPoints:
    """
    input one refers to the first given point
    input two refers to the second given point
    """
    #Initialization
    def __init__(self, input_one, input_two):
        self.input_one = input_one
        self.input_two = input_two
        self.__a = None
        self.__b = None
        self.__c = None
        self.__error = " "

    def LineFormula(self):
        """
        This function calculates the output line (in the form of AX + BY = C)
        :return:
        * output: None, in case of an error. otherwise: String
        * Error: None, when no error is detected, otherwise: String   
        """
        output_line = self.input_val()     
        if output_line:
            self.__a = self.input_one[1] - self.input_two[1]
            self.__b = self.input_two[0] - self.input_one[0]
            self.__c = (
                self.__a * self.input_one[0] + self.__b * self.input_one[1]
            )
        check = self.line_val()
        check2 = self.computation_val()
        if check is False or check2 is False:
            return "Error in inputs"
            
        if self.__a == 0:
          output_line = (
            f"The line passing through points input one and input two is: "
            f"{self.__b:f} * Y"
            )
        elif self.__b == 0:
            output_line = (
                f"The line passing through points input one and input two is: "
                f"({self.__a:f}) * X"
            )
        elif self.__b < 0:
            output_line = (
                f"The line passing through points input one and input two is: "
                f"({self.__a:f}) * X "
                f"- ({self.__b:f}) * Y "
                f"= {self.__c:f}"
            )
        else:
            output_line = (
                f"The line passing through points input one and input two is: "
                f"({self.__a:f}) * X "
                f"+ ({self.__b:f}) * Y "
                f"= {self.__c:f}"
              )
        return output_line

    def input_val(self) -> (bool):
        """
        This function check the validity of the inputs.
        It returns False if the inputs are not validated.
        """
        try:
            assert isinstance(self.input_one[0], int) or isinstance(
                self.input_one[0], float
            )
            assert isinstance(self.input_one[1], int) or isinstance(
                self.input_one[1], float
            )
            assert isinstance(self.input_two[0], int) or isinstance(
                self.input_two[0], float
            )
            assert isinstance(self.input_two[1], int) or isinstance(
                self.input_two[1], float
            )
            
        except AssertionError:
            print("Error: input type not valid")
            self.__error = "Error: input type not valid"
            return False
        else:
            return True
    def line_val(self) -> (bool):
        try:
            if (self.__a * (self.input_one[0]) + self.__b * (self.input_one[1])) != self.__c:
                raise ValueError
        except AssertionError as error:
            f"Error: This is not the corresponding line!"
            self.__error = "Error: This is not the corresponding line!"
            return False
        except ValueError:
            f"Please choose another point!"
            self.__error = "Please choose another point!"
            return False
        else:
            return True
    def computation_val(self) -> (bool):
        """
        This function check the computation of the variables.
        It returns False if the computation is not valid.
        """
        try:
            if self.__a == 0 and self.__b == 0:
                raise ValueError
        except AssertionError as error:
            print("Error: Both points have same Cartesian Coordinate!")
            self.__error = "Error: Both points have same Cartesian Coordinate!"
            return False
        except ValueError:
            print("Please choose another two points!")
            self.__error = "Please choose another two points!"
            return False
        else:
            return True

  