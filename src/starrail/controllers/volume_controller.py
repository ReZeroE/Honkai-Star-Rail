from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import psutil
import time

from ..utils.utils import Printer, aprint
from .star_rail_app import HonkaiStarRail

class VolumeController:
    def __init__(self, starrail_instance: HonkaiStarRail):
        self.starrail = starrail_instance
        

    def mute(self):
        pass
    
    def unmute(self):
        pass
    
    def set_volume(self, level: int):
        pass


    def activate_unfocus_mute(self):
        try:
            aprint(f"Auto-Mute: {Printer.to_lightgreen("ACTIVATED")}")
            
            while True:
                starrail_proc = self.starrail.get_starrail_process()
                if self.starrail.is_focused():
                    self.mute_pid(starrail_proc, mute=False)
                else:
                    self.mute_pid(starrail_proc, mute=True)
                time.sleep(1)
        except KeyboardInterrupt:
            aprint(f"Auto-Mute: {Printer.to_lightred("DEACTIVATED")}")
    

    def mute_pid(
        self, 
        starrail_proc: psutil.Process, 
        mute: bool
    ):
        # mute = True to mute
        # mute = False to unmute
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.ProcessId == starrail_proc.pid:
                
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMute(mute, None)
                
                return True
        return False