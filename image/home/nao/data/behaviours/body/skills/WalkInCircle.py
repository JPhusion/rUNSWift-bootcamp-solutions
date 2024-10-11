

from BehaviourTask import BehaviourTask
from util.actioncommand import walk
from util.CircularMotion import angular_velocity


class WalkInCircle(BehaviourTask):

    """
    Description:
    A skill to walk in a circle.
    """

    # f_p is final position
    def _tick(self, radius=750, forward=80, clockwise=True):
        turn = angular_velocity(radius, forward) * (-1 if clockwise else 1)

        self.world.b_request.actions.body = walk(forward, 0, turn)
