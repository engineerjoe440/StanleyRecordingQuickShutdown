################################################################################
"""
Shut down and restore Audio PipeWire Configuration after a Recording Session.
"""
################################################################################

import subprocess

import pulsectl

def stop_easyeffects():
    subprocess.run(["killall", "easyeffects"], check=True)

def main():
    """Shut down Recording System."""
    stop_easyeffects()
    with pulsectl.Pulse('manager') as pulse:
        for stream in pulse.sink_input_list():
            if stream.name == "Playback":
                pulse.volume_set_all_chans(stream, 1)

if __name__ == "__main__":
    main()
