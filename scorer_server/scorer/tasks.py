from typing import Any, NamedTuple

from scorer.attack import Attack
from scorer.manager import TeamManager, AttackManager
from scorer.team import Team


class Update:
    def __init__(self, data: Any):
        self.data = data

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.data}>"


class AttackUpdate(Update):
    data: Attack

    def __init__(self, attack: Attack):
        super().__init__(attack)


class TeamUpdate(Update):
    data: Team

    def __init__(self, team: Team):
        super().__init__(team)


class ScoreTask(NamedTuple):
    team: Team
    attack: Attack

    @classmethod
    def from_id(cls, task_id, team_manager: TeamManager, attack_manager: AttackManager):
        team_id, attack_id = task_id.split('-')
        return ScoreTask(team=team_manager.team_from_id(team_id),
                         attack=attack_manager.attack_from_id(attack_id))
