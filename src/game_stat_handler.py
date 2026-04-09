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
        elif size <= 10:
            self.hand_size_category = HandSizeCategories.HIGH
        else:
            raise ValueError("Hand size out of range")


    def get_hand_size_factor(self, i)->tuple[int, int, int, int]:

        match self.hand_size_category:
            case HandSizeCategories.ZERO:
                return (0, 0, 0, 0)
            
            case HandSizeCategories.LOW:
                i_factor = i * .073
                return (.33 + i_factor, 0, 0, .05)
            
            case HandSizeCategories.HIGH:
                i_factor = i * .073
                return (.26 + i_factor, 0, 0, .05)
            
    def __repr__(self):
        return f"GameStatHandler(game_state={self.game_state}, hand_size={self.hand_size}, draw_relics={self.draw_relics})"

class FightHandler(GameStatHandler):
    def __init__(self):
        super.__init__()