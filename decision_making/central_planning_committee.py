class CentralPlanningCommittee:
    def __init__(self, chosen_philosophy):
        self.small_line_break = "---------------------"
        self.big_line_break = "-=-=-=-=-=-=-=-=-=-=-"

        self.chosen_philosophy = chosen_philosophy

    def describe_committee(self):
        description = "The Central Planning Committee (hereafter abbreviated as CPC) is composed of the four founding members: " \
                      "Alex/Pompano, Tom/Tyler Mallory, Daniel/Eris Eto, and Pisspig/Lyle Dunham. " \
                      "Each member of the CPC would be a managing director with specific oversight over 1 divisions. " \
                      "The CPC is responsible for making ultimate decisions that would affect the corporation as whole " \
                      "(Examples: Deciding on corp goals, joining an alliance, bluing/redding a player group, buying a player owned station). " \
                      "The CPC would make decisions using the following voting process:"
        description = description + "\n" + self.small_line_break + "\n"
        description = description + "CPC VOTING SYSTEM: " \
                                    "At least 3 CPC members need to agree before a CPC decision can be made. " \
                                    "Person A is needed to come up with the idea. This idea must have a basic plan of execution. " \
                                    "Person A must propose to a second member (Person B). " \
                                    "If Person A and B both think it's a good idea, then they present it to the remaining members (Persons C and D). " \
                                    "After discussion, if 3 CPC members think it's a good idea, then the decision is made."
        description = description + "\n" + self.small_line_break + "\n"
        description = description + "CPC SUCCESSION: " \
                                    "If a CPC Member decides to take a break for less than 6 months, " \
                                    "then they remain a CPC Member and voting moves to 2-1 to make pass corp decisions. " \
                                    "If a CPC Member leaves the corp completely or takes a break for more than 6 months, " \
                                    "then that departing CPC Member has the option of nominating any corp member as their successor. " \
                                    "This 'CPC nominee' becomes a CPC Member UNLESS all 3 remaining CPC Members veto." \
                                    "If the departing CPC Member declines to declare a nominee, then the 3 remaining CPC Members will decide internally on their replacement."

        return description

