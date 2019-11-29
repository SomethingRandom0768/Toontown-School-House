from direct.fsm.StatePush import StateVar
from otp.level.EntityStateVarSet import EntityStateVarSet
from toontown.cogdominium.CogdoEntityTypes import CogdoCraneGameSettings, CogdoCraneCogSettings
from CogdoUtil import VariableContainer, DevVariableContainer
from toontown.toonbase import ToontownGlobals

Settings = EntityStateVarSet(CogdoCraneGameSettings)
CogSettings = EntityStateVarSet(CogdoCraneCogSettings)
CranePosHprs = [(13.4 - 36.874, -136.6 + 113.682, 6, -45, 0, 0),
                (13.4 - 36.874, -91.4 + 113.682, 6, -135, 0, 0),
                (58.6 - 36.874, -91.4 + 113.682, 6, 135, 0, 0),
                (58.6 - 36.874, -136.6 + 113.682, 6, 45, 0, 0)]
MoneyBagPosHprs = [[10, 10, 6, 0, 0, 0],
                   [-10, 10, 6, 0, 0, 0],
                   [10, -10, 6, 0, 0, 0],
                   [-10, -10, 6, 0, 0, 0]]
IntroDurationSeconds = 24.0
MoneyBagsRespawnRate = 15.0
FinishDurationSeconds = 10.0
MoneyBagsJoinHeight = 70
SpotlightObstacleWait = 36
SpotlightStomperDamage = {
    ToontownGlobals.ToontownCentral: 5,
    ToontownGlobals.DonaldsDock: 10,
    ToontownGlobals.DaisyGardens: 15,
    ToontownGlobals.MinniesMelodyland: 18,
    ToontownGlobals.TheBrrrgh: 22,
    ToontownGlobals.DonaldsDreamland: 28,
}