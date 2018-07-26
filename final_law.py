"""

The main thing we want to accomplish here is deciding on the best way to govern the corp for long-term stability.

Currently, we are a communist corp.
The tangible benefits of this is that we can share isk and put up almost all harvested resources in sell orders.
This increases the amount of isk we can earn as a group above merely fulfilling existing buy orders.

Main questions to answer/issues to address:
How should we handle instances when someone wants to leave the corp?
How should we handle instances when someone wants to join the corp?
How should we allocate funds?
How should we determine group goals?

Key concepts:
Laws work because everyone agrees to follow them, not because they are perfectly fair (ex: trial by ordeal).
Laws that get too complicated are bad because it's too much to remember and too much like work.
Corps live according group activity, enthusiasm, and trust (cohesion) and die according to group drama, apathy, and distrust (discord).
Members stay in corps because they like being there and because they derive some individual benefit.
An institution is an organization/idea that can exist beyond the departure of a single individual/group of individuals.

Therefore, corp laws should do the following:
Be as simple as possible.
Encourage group cohesion.
Discourage group discord.
Promote corp longevity as an institution.

"""


class FinalLaw:
    def __init__(self, chosen_philosophy="communist",
                 tax_rate=100, encourage_outside_recruitment=False, personal_goals="", group_goals=""):
        self.small_line_break = "---------------------"
        self.big_line_break = "-=-=-=-=-=-=-=-=-=-=-"
        self.possible_philosophy_values = ["communist", "socialist"]

        # NOTE: These are free-form goals determined by the individual, this might help explain why you want what you want
        self.personal_goals = personal_goals
        self.group_goals = group_goals

        self.tax_rate = tax_rate
        self.encourage_outside_recruitment = encourage_outside_recruitment

        self.chosen_philosophy = chosen_philosophy
        self.benefits = []
        self.detriments = []

        self.communist_benefits = [
            "Unique organization",
            "Engenders trust",
            "Harvested resources/precursor material can be pooled, so large projects can be completed more easily",
            "Isk is pooled, so goods can be sold on the market via sell orders instead of fulfilling buy order; this increases overall isk intake",
            "Larger group isk pool"
        ]
        self.communist_detriments = [
            "Difficult to recruit new members since they might suspect a scam/ruse",
            "Difficult to know when and how much shared isk can be used for personal use, such as buying a battleship",
            "Additional work needed to determine new member's trustworthiness",
            "More work needed for deciding which group goals to pursue"
        ]

        self.socialist_benefits = [
            "Closer to what Eve players expect, so recruit would be easier",
            "Easier to manage"
        ]
        self.socialist_detriments = [
            "Less top-down control",
            "Smaller group isk pool"
        ]

    def validate_law(self):
        law_is_valid = True

        if self.chosen_philosophy not in self.possible_philosophy_values:
            print("Invalid philosophy")
            print(self.small_line_break)
            law_is_valid = False
        if self.tax_rate > 100 or self.tax_rate < 0:
            print("Invalid tax rate")
            print(self.small_line_break)
            law_is_valid = False

        return law_is_valid

    def print_law(self):
        is_law_valid = self.validate_law()

        if is_law_valid is True:

            if self.personal_goals != "":
                print(self.big_line_break)
                print("These are things I want to do for myself: ")
                print(self.personal_goals)
            if self.group_goals != "":
                print(self.big_line_break)
                print("these are goals that I want our corp to accomplish: ")
                print(self.group_goals)

            print(self.big_line_break)

            print("I want a " + self.chosen_philosophy + " corporation.")

            if self.chosen_philosophy == "communist":
                print("This means that all/almost all resources and isk are shared and available for communal use.")
                self.benefits = self.communist_benefits
                self.detriments = self.communist_detriments
            elif self.chosen_philosophy == "socialist":
                print("This means that a pre-decided portion of resources and isk are shared and available for communal use.")
                print("This is closer to how most Eve corporations operate.")
                self.benefits = self.socialist_benefits
                self.detriments = self.socialist_detriments

            print(self.big_line_break)
            print("BENEFITS:")
            print(self.small_line_break)
            for benefit in self.benefits:
                print(benefit)

            print(self.big_line_break)
            print("DETRIMENTS:")
            print(self.small_line_break)
            for detriment in self.detriments:
                print(detriment)

            print(self.big_line_break)


final = FinalLaw(chosen_philosophy="communist",
                 personal_goals="I want to do small gang PvP",
                 group_goals="I want the corp to get our own station")

# final = FinalLaw(chosen_philosophy="socialist",
#                  personal_goals="I want to make isk",
#                  group_goals="I want the corp to get our own station")


final.print_law()

