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
        starrail_proc = self.starrail.get_starrail_process()
        if starrail_proc == None:
            aprint(Printer.to_lightred(f"Honkai: Star Rail not running."))
            return False
        return self.mute_pid(starrail_proc, mute=True)
    
    
    def unmute(self):
        starrail_proc = self.starrail.get_starrail_process()
        if starrail_proc == None:
            aprint(Printer.to_lightred(f"Honkai: Star Rail not running."))
            return False
        return self.mute_pid(starrail_proc, mute=False)
    
    
    def set_volume(self, level: int):
        pass


    def activate_unfocus_mute(self, check_interval=0.3):
        try:
            aprint(f"Auto-Mute: {Printer.to_lightgreen("ACTIVATED")}")
            
            while True:
                starrail_proc = self.starrail.get_starrail_process()
                if starrail_proc == None:
                    aprint(f"Honkai: Star Rail not running.\nAuto-Mute {Printer.to_lightred("DEACTIVATED")}")
                    return
                
                res = False
                if self.starrail.is_focused():
                    res = self.mute_pid(starrail_proc, mute=False)
                else:
                    res = self.mute_pid(starrail_proc, mute=True)
                # if res == False:
                #     aprint("Failed to mute Honkai: Star Rail.")
                    
                time.sleep(check_interval)
        
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