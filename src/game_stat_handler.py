from constants.project_constants import GameState, HandSizeCategories
from constants.game_constants import DrawRelics

class GameStatHandler():
    def __init__(self):
        self.game_state: GameState = GameState.INIT
        self.draw_relics: list[DrawRelics] = []

        self.hand_size: int = 5
        self.hand_size_category = HandSizeCategories.LOW
        self.curr_turn: int = 0

    def set_hand_size(self, size):
        self.hand_size = size

        if size == 0:
            self.hand_size_category = HandSizeCategories.ZERO
        elif size <= 5:
            self.hand_size_category = HandSizeCategories.LOW
        elif size == 6:
            self.hand_size_category =  HandSizeCategories.SIX
        elif size == 7:
            self.hand_size_category = HandSizeCategories.SEVEN
        elif size == 8:
            self.hand_size_category =  HandSizeCategories.EIGHT
        elif size == 9:
            self.hand_size_category =  HandSizeCategories.NINE
        elif size == 10:
            self.hand_size_category = HandSizeCategories.TEN
        else:
            raise ValueError(f"Hand size out of range: {self}")


    def get_hand_size_factor(self, i)->tuple[int, int, int, int]:
        match self.hand_size_category:
            case HandSizeCategories.ZERO:
                raise Exception("Tried to take image of 0 size hand")
            
            case HandSizeCategories.LOW:
                low_base = .33
                first_card_factor = -(self.hand_size - 5) * .05
                i_factor = i * .093

                return (low_base + i_factor + first_card_factor, 0, 0, .05)
            
            case HandSizeCategories.SIX:
                six_base = .27
                i_factor = i * .096
                return (six_base + i_factor, 0, 0, .05)
            
            case HandSizeCategories.SEVEN:
                seven_base = .22
                i_factor = i * .095
                return (seven_base + i_factor, 0, 0, .05)
            
            case HandSizeCategories.EIGHT:
                eight_base = .2
                i_factor = i * .085
                return (eight_base + i_factor, 0, 0, .05)

            case HandSizeCategories.NINE:
                nine_base = .18
                i_factor = i * .08
                return (nine_base + i_factor, 0, 0, .05)            

            case HandSizeCategories.TEN:
                ten_base = .17
                i_factor = i * .075
                return (ten_base + i_factor, 0, 0, .05)
            
    def __repr__(self):
        return f"""GameStatHandler(
    game_state={self.game_state},
    hand_size={self.hand_size},
    hand_size_category={self.hand_size_category},
    draw_relics={self.draw_relics},
    curr_turn={self.curr_turn},
)"""

class FightHandler(GameStatHandler):
    def __init__(self):
        super.__init__()