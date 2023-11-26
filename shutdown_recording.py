#!/user/bin/python3
################################################################################
"""
Shut down and restore Audio PipeWire Configuration after a Recording Session.
"""
################################################################################

import subprocess

import pulsectl

def stop_easyeffects():
    """Kill the EasyEffects Application."""
    try:
        subprocess.run(["killall", "easyeffects"], check=True)
    except subprocess.CalledProcessError:
        print("easyeffects already stopped.")

def restore_audio_levels():
    """Shut down Recording System."""
    with pulsectl.Pulse('manager') as pulse:
        for stream in pulse.sink_input_list():
            if stream.name == "Playback":
                pulse.volume_set_all_chans(stream, 1)

if __name__ == "__main__":
    stop_easyeffects()
    restore_audio_levels()
